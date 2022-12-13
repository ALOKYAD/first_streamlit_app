import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🎂 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 🥪 Kale ,Spinanch & Rocket smoothie')
streamlit.text('🥘 Hard-Boiled Free-range Egg')


import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
