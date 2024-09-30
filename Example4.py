# 2.2.3.2 Logic used in a callback

import streamlit as st 
import pandas as pd 

# Callbacks are a clean way to modify st.session_state. 
# Callbacks are executed as a prefix to the script rerunning, 
# so the position of the button relative to accessing data is not important.

if 'name' not in st.session_state: 
	st.session_state['name'] = 'John Doe' 
	
def change_name(name): 
	st.session_state['name'] = name 
	
st.header(st.session_state['name']) 

st.button('Jane', on_click=change_name, args=['Jane Doe']) #args: to pass to the callback.
st.button('John', on_click=change_name, args=['John Doe']) 

st.header(st.session_state['name'])

print("hello world")