import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My New Healthy Diner')
streamlit.header('Breakfast menu')
streamlit.text('🫕 Classic: two scrambled eggs with smoked apple sausages and toast')
streamlit.text('🥬 omlette with three eggs, feta cheese, olives, and spinach')
streamlit.text('🫒 Mexican omlette with three eggs, refried beans, avacado, and tabasco sauce')
streamlit.text('🥪 toast')
streamlit.header('🍎🍐 Build your own fruit smoothies 🍉🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])

#display the table on the page
#streamlit.dataframe(my_fruit_list)
#display only selected fruit
fruits_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# streamlit.text(fruityvice_response.json())  # removed this line later
# take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it on the screen as a table
streamlit.dataframe(fruityvice_normalized)
streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit_load_list contains:")
streamlit.dataframe(my_data_rows)
# Allow user to add a fruit at the end
fruit_add = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('Thanks for adding', fruit_add)
my_cur.execute("insert into fruit_load_list values('from streamlit')")
