import streamlit as st
from deep_translator import GoogleTranslator

# Placeholder for an actual user management system
# WARNING: This is for demonstration purposes only!
if 'user_db' not in st.session_state:
    st.session_state.user_db = {'admin': 'password'}  # Default user

# Check if the user is logged in
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Login Form
def show_login_page():
    st.sidebar.header("Login")
    username = st.sidebar.text_input("Username", key="login_username")
    password = st.sidebar.text_input("Password", type="password", key="login_password")
    
    if st.sidebar.button("Login"):
        if username in st.session_state.user_db and st.session_state.user_db[username] == password:
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.sidebar.error("Incorrect Username/Password")

# Sign Up Form
def show_signup_page():
    st.sidebar.header("Sign Up")
    new_username = st.sidebar.text_input("New Username", key="signup_username")
    new_password = st.sidebar.text_input("New Password", type="password", key="signup_password")
    
    if st.sidebar.button("Sign Up"):
        if new_username in st.session_state.user_db:
            st.sidebar.error("Username already exists.")
        else:
            st.session_state.user_db[new_username] = new_password
            st.sidebar.success("User created successfully. Please log in.")

if not st.session_state.logged_in:
    # Toggle between Login and Sign Up pages
    page = st.sidebar.radio("Page", ['Login', 'Sign Up'])
    
    if page == 'Login':
        show_login_page()
    else:
        show_signup_page()
else:
    # Main App
    st.title('Mini Translator')

    col1, col2 = st.columns(2)

    with col1:
        st.header('Text to Translate')
        input_text = st.text_area("", value="Type your text in here", height=250)

    with col2:
        st.header('Translation')
        placeholder = st.empty()

    # Sidebar for language selection
    st.sidebar.header('Translation Settings')
    # Assuming getList and land_dict are defined as before
    langs, lang_codes = getList(land_dict)
    output_langs = st.sidebar.selectbox("Choose your output language", langs, index=langs.index('english'))

    if len(input_text) > 0:
        if len(input_text) > 5000:
            st.warning("You are going over 5000 characters. Only the first 5000 characters will be processed.")
            input_text = input_text[:4999]

        translated = GoogleTranslator(source='auto', target=land_dict[output_langs]).translate(input_text)
        placeholder.text_area("Translated Text", value=translated, height=250, key="translated")
        st.download_button('Download the Text', data=translated, file_name='translated.txt')
    else:
        placeholder.text_area("Translated Text", value="Translation will appear here.", height=250, key="translated")
