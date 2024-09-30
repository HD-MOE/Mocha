# 2.2.2 Stateful button

import streamlit as st 

#Example: Stateful button
#If you want a clicked button to continue to be True, 
#create a value in st.session_state and 
#use the button to set that value to True in a callback.

if 'clicked' not in st.session_state: 
	st.session_state.clicked = False 
	
def click_button(): 
	st.session_state.clicked = True 
	
st.button('Click me', on_click = click_button)  #on_click is always true
st.session_state.clicked

if st.session_state.clicked: 
	# The message and nested widget will remain on the page 
	st.write('Button clicked!') 
	st.slider('Select a value')
