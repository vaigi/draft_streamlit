print('try')
print("------------")

import streamlit as st

if st.button('Balloons!'):
    st.balloons()
    st.write('1')
number = st.number_input("Insert a number", value=None, placeholder="Type a number...")
st.write('The current number is ', number)
