import streamlit as st
from streamlit_option_menu import option_menu

st.title("My Live Application")

with st.sidebar:
    selected = option_menu(
        menu_title="My App", 
        options=["Home", "About", "Services"],
        icons=["house", "info-circle", "gear"], # Optional icons
        menu_icon="cast",                      # Optional menu icon
        default_index=0                        # Default selected option
    )

# Use the 'selected' variable to control page content
if selected == "Home":
    st.write("Welcome to the Home page!")
elif selected == "About":
    st.write("Learn more about us here.")
elif selected == "Services":
    st.write("Check out our services.")
