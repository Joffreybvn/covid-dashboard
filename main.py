
from os import environ
import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np

st.set_option("deprecation.showfileUploaderEncoding", False)
st.beta_set_page_config(
    page_title="Belgium Coronavirus Data",
    layout="wide"
)


# Loading map data
@st.cache(persist=True)
def load_data(nrows):
    # data = pd.read_csv(DATA_URL, nrows=nrows)
    df = pd.DataFrame(np.random.randn(10000, 2) / [50, 50] + [50.5010789, 4.4764595], columns=['lat', 'lng'])
    return df


data = load_data(100000)


def display_map(dataframe: pd.DataFrame):
    """Display a 3D aggregation map from given data."""

    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v10',
        initial_view_state=pdk.ViewState(
            longitude=4.4764595,
            latitude=50.45,
            zoom=8,
            min_zoom=1,
            max_zoom=15,
            pitch=40.5,
            bearing=15,
            height=580),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=dataframe,
                get_position=["lng", "lat"],
                auto_highlight=True,
                elevation_scale=20,
                pickable=True,
                elevation_range=[0, 3000],
                extruded=True,
                coverage=1,
            )
        ],
    ))


# Top section
row1_1, row1_2 = st.beta_columns((2, 3))

with row1_1:
    st.title("Belgium Coronavirus Data")
    week_selected = st.slider("Display covid cases at any given time", 0, 23)

with row1_2:
    st.write("""
    ##
    Examining how Uber pickups vary over time in New York City's and at its major regional airports.
    By sliding the slider on the left you can view different slices of time and explore different transportation trends.
    """)

display_map(data)
