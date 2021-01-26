

import pickle
from typing import List, Tuple
import streamlit as st
import pydeck as pdk
import pandas as pd
import time
import cv2


st.set_option("deprecation.showfileUploaderEncoding", False)
st.beta_set_page_config(
    page_title="Belgium Coronavirus Data",
    layout="wide"
)


# Load custom CSS
def local_css(file_name):

    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Loading datasets

@st.cache(persist=True)
def load_map_data() -> Tuple[List[pd.DataFrame], int]:
    """Load and return the covid cases dataset."""

    with open('./datasets/clean/week_cases_location.p', 'rb') as handle:
        cases_dfs = pickle.load(handle)

    return cases_dfs, len(cases_dfs) - 1


cases, weeks = load_map_data()


def get_map(dataframe: pd.DataFrame) -> pdk.Deck:
    """Display a 3D aggregation map from given data."""

    return pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v10',
        initial_view_state=pdk.ViewState(
            longitude=4.4764595,
            latitude=50.45,
            zoom=7.7,
            min_zoom=1,
            max_zoom=15,
            pitch=40.5,
            bearing=15,
            height=580),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=dataframe,
                get_position=["lat", "lng"],
                auto_highlight=True,
                elevation_scale=20,
                pickable=True,
                elevation_range=[0, 1000],
                extruded=True,
                coverage=1,
            )
        ],
    )


# Header section
row1_1, row1_2 = st.beta_columns((2, 4))

with row1_1:
    st.title("Belgium Coronavirus Data")

with row1_2:
    st.write("""
    ##
    Examining how Uber pickups vary over time in New York City's and at its major regional airports.
    By sliding the slider on the left you can view different slices of time and explore different transportation trends.
    """)

# Content section
row2_1, row2_2 = st.beta_columns((4, 2))

with row2_1:

    # Create placeholders
    slider_ph = st.empty()  # Slider
    button_ph = st.empty()  # Button
    map_ph = st.empty()  # Map

    # Set a default slider
    slider_text = f"Covid cases for week: "
    value = slider_ph.slider(slider_text, 1, len(cases), 1, 1)
    map_ph.pydeck_chart(get_map(cases[value - 1]))

    # On click to "Animate", loop to refresh the map and iterate the slider
    if button_ph.button('Run the animation'):

        for _ in range(weeks):
            time.sleep(.5)

            value = slider_ph.slider(slider_text, 1, len(cases), value + 1, 1)
            map_ph.pydeck_chart(get_map(cases[value - 2]))

with row2_2:

    # create a variable for each graph
    March2020 = cv2.imread('graph/MARCH2020.png')
    April2020 = cv2.imread('graph/APRIL2020.png')
    May2020 = cv2.imread('graph/May2020.png')
    June2020 = cv2.imread('graph/June2020.png')
    July2020 = cv2.imread('graph/July2020.png')
    August2020 = cv2.imread('graph/August2020.png')
    September2020 = cv2.imread('graph/September2020.png')
    October2020 = cv2.imread('graph/October2020.png')
    November2020 = cv2.imread('graph/November2020.png')
    December2020 = cv2.imread('graph/December2020.png')
    January2020 = cv2.imread('graph/Janauary2020.png')
     
    # create a list that contains all variables with graph 
    months = [March2020,
             April2020,
             May2020,
             June2020,
             July2020,
             August2020,
             September2020,
             October2020,
             November2020,
             December2020,
             January2020]

    month_selected = st.slider("Chose the month to know where the province with more and less cases", 0, 10)
    
    # display the graph according to the slider value
    st.image(months[month_selected])



# Load the custom CSS -- Keep at the very end of the file !
local_css('./assets/style.css')
