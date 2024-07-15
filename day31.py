import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px

# Load geographical data
@st.cache
def load_geo_data():
    gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    return gdf

# Load sample data
@st.cache
def load_data():
    data = pd.DataFrame({
        'country': ['China', 'India', 'United States', 'Indonesia', 'Pakistan'],
        'value': [1403500365, 1366417754, 331883986, 273523621, 220892331]
    })
    return data

# Main function to run the Streamlit app
def main():
    st.title("Choropleth Map Example")

    # Load data
    geo_data = load_geo_data()
    data = load_data()

    # Merge geographical data with sample data
    merged_data = geo_data.merge(data, how='left', left_on='name', right_on='country')

    # Plotly choropleth map
    fig = px.choropleth(merged_data,
                        geojson=merged_data.geometry,
                        locations=merged_data.index,
                        color='value',
                        hover_name='name',
                        color_continuous_scale=px.colors.sequential.Plasma,
                        projection="natural earth")

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
