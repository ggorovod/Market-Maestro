import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import bcrypt
from streamlit_chat import message
from dotenv import load_dotenv
from streamlit_option_menu import option_menu
from Modules import Trading
from Modules import Sentiment
from Modules import CryptoScanner
from Modules import OpenAI

#function for user authentication and options after the success login
def main():

    if 'generated' not in st.session_state:
        st.session_state['generated'] = []
    if 'past' not in st.session_state:
        st.session_state['past'] = []

    if "temp" not in st.session_state:
        st.session_state["temp"] = ""

    with open('login.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
    )
    #login screen on the main page
    name, authentication_status, username = authenticator.login('Login', 'main')

    #condition for successful login
    if st.session_state["authentication_status"]:
    
        st.write(f'Welcome *{st.session_state["name"]}*')

    #input text for user input 
        user_input = st.text_input("You", key="input")

        if st.button("clear"):
            st.session_state['generated'] = []
            st.session_state['past'] = []

    #sidebar menu options 
        with st.sidebar:
            selected2 = option_menu(
            menu_title="Main Menu", 
            options=["Trading", "Sentiment", "OpenAI", "Crypto Scanner", "Algorithmic Trading", "logout"],
            icons=["currency-dollar", "newspaper", "cpu", "currency-bitcoin" , "code-square", "box-arrow-left" ]
        )

    #action for main screen for the sidebar selection 

        if selected2 == "Trading":
            if user_input:
                output=Trading.generate_trade(user_input)
                st.session_state['past'].append(user_input)
                st.session_state['generated'].append(output)

            if st.session_state['generated']:
                for i in range(len(st.session_state['generated'])-1, -1, -1):
                    message(st.session_state["generated"][i], key=str(i))
                    message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

        if selected2 == "Sentiment":
            if user_input:
                output=Sentiment.generate_sentiment(user_input)
                st.session_state['past'].append(user_input)
                st.session_state['generated'].append(output)

            if st.session_state['generated']:
                for i in range(len(st.session_state['generated'])-1, -1, -1):
                    message(st.session_state["generated"][i], key=str(i))
                    message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            
        if selected2 == "OpenAI":
            if user_input:
                output=OpenAI.generate_response(user_input)
                st.session_state['past'].append(user_input)
                st.session_state['generated'].append(output)
            
            if st.session_state['generated']:
                for i in range(len(st.session_state['generated'])-1, -1, -1):
                    message(st.session_state["generated"][i], key=str(i))
                    message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

        if selected2 == "Crypto Scanner":
            if user_input:
                output=CryptoScanner.crypto_query(user_input)
                st.session_state['past'].append(user_input)
                st.session_state['generated'].append(output)
            
            if st.session_state['generated']:
                for i in range(len(st.session_state['generated'])-1, -1, -1):
                    message(st.session_state["generated"][i], key=str(i))
                    message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

        if selected2 == "Algorithmic Trading":
            st.write("Future work!")

        if selected2 == "logout":
            authenticator.logout('Logout', 'main') 

    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')

    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')