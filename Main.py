import streamlit as st
from streamlit_option_menu import option_menu
st.title("my live application")
with st.sidebar:
  data = option_menu{
  menu_title = "my app"
  option=["home","about","services"]
  }
