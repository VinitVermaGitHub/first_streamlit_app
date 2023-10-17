import streamlit
streamlit.title('My New Healthy Diner')
streamlit.header('Breakfast menu')
streamlit.text('🫕 Classic: two scrambled eggs with smoked apple sausages and toast')
streamlit.text('🥬 omlette with three eggs, feta cheese, olives, and spinach')
streamlit.text('🫒 Mexican omlette with three eggs, refried beans, avacado, and tabasco sauce')
streamlit.text('🥪 toast')
streamlit.header('🍎🍐 Build your own fruit smoothies 🍉🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
