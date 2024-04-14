import streamlit as st
from deep_translator import GoogleTranslator

# Placeholder for an actual authentication system
# WARNING: This is for demonstration purposes only!
USER_NAME = "7aaffssaa"
PASSWORD = "19371937"

# Check if the user is logged in
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Login Form
def show_login_page():
    st.sidebar.header("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    
    if st.sidebar.button("Login"):
        if username == USER_NAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.sidebar.error("Incorrect Username/Password")

if not st.session_state.logged_in:
    show_login_page()
else:
    # Improved layout with columns and better use of space
    st.title('Mini Translator')

    col1, col2 = st.columns(2)

    with col1:
        st.header('Text to Translate')
        input_text = st.text_area("", value="Type your text in here", height=250)

    with col2:
        st.header('Translation')
        # Dynamically display the translated text or a placeholder
        placeholder = st.empty()

    # Sidebar for language selection
    st.sidebar.header('Translation Settings')

    def getList(dict):
        return list(dict.keys()), list(dict.values())

    land_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-CN', 'chinese (traditional)': 'zh-TW', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'kinyarwanda': 'rw', 'korean': 'ko', 'kurdish': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'tatar': 'tt', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'turkmen': 'tk', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
     # Truncated for brevity

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
