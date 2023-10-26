import streamlit
import pandas as pd

streamlit.title("I love turtle")
streamlit.text("Turtles are green and live in a ponds and lakes")

fruits = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits = fruits.set_index('Fruit')

streamlit.multiselect("Pick some fruits:", list(fruits.index), ['Avocado', 'Strawberries'])
streamlit.dataframe(fruits)
