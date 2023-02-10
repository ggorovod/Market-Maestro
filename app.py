import streamlit as st
from Modules import Home

#Css styling 
# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#Title on the main page
st.title("Market Maestro 🤖")

#Landing page
Home.main()

#Additional css styling to hide streamlit defauly hamburger Menu and footer note
hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        footer:after{
            content: 'Made by Group 3";
            display:block;
            position: relative;
            color:tomato;
            padding:5px;
            top:3px;
        }
        input.st-c0 {
        color: black;
        }
        div.css-1qkvcga {
        color: black;
        }

        </style>
        """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

