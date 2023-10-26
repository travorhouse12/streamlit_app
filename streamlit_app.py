import streamlit
import pandas as pd

streamlit.title("I love turtle")
streamlit.text("Turtles are green and live in a ponds and lakes")

fruits = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(fruits)
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
