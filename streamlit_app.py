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

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function=get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()


streamlit.header("The fruit_load_list contains:")
def get_fruit_load_list():
  with my_cur as my_cnx.cursor():
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()

if streamlist.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows=get_fruit_load_list()
  streamlit.dataframe(my_data_rows)
streamlit.stop()
# Allow user to add a fruit at the end
fruit_add = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('Thanks for adding', fruit_add)
my_cur.execute("insert into fruit_load_list values('from streamlit')")
