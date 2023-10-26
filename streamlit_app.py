import streamlit
import pandas as pd

streamlit.title("I love turtle")
streamlit.text("Turtles are green and live in a ponds and lakes")

fruits = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits = fruits.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(fruits.index), ['Avocado', 'Banana'])
fruits_to_show = fruits.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
