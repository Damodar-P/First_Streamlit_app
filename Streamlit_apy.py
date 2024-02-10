import streamlit
streamlit.title('My parents new healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & BlueBerry oatmeal')
streamlit.text('🥗kale,Spainch & Rocket Smoothie')
streamlit.text('🐔Hard-boiled free-Range Egg ')
streamlit.text('🥑🍞Avocado Toast ')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list=pandas.read.CSV("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_Fruit_list)
