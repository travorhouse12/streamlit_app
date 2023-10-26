import streamlit
import pandas as pd

#streamlit.title("I love turtle")
#streamlit.text("Turtles are green and live in a ponds and lakes")

#fruits = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#fruits = fruits.set_index('Fruit')

#all_fruits = fruits.index.unique().tolist()

#fruits_selected = streamlit.multiselect("Pick some fruits:", list(fruits.index), all_fruits)
#fruits_to_show = fruits.loc[fruits_selected]
##streamlit.dataframe(fruits_to_show)

import streamlit as st
import pandas as pd

st.title("I love turtle")
st.text("Turtles are green and live in ponds and lakes")

# Load data and set 'Fruit' as index
fruits = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits = fruits.set_index('Fruit')

# Get all unique fruits from the index
all_fruits = fruits.index.unique().tolist()

# Add 'Select All' option
options = ['Select All'] + all_fruits

# Create a multiselect widget for the fruits
fruits_selected = st.multiselect("Pick some fruits:", options, [])

# If 'Select All' is selected, select all fruits
if 'Select All' in fruits_selected:
    fruits_selected = all_fruits

# Show the selected fruits' data
fruits_to_show = fruits.loc[fruits_selected]
st.dataframe(fruits_to_show)
