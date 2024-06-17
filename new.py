import streamlit as st
import random
import pyperclip

spchar = "~!@#$%^&*()<>?'{}[]\-_+-*./"
char = "qwertyuiopasdfghjklzxmnbvc"
Nuchar = "123456789010ASDFGHJKLPOIUYTREQXCVBNMZ"

st.title("Password Generator")

col1, col2 = st.columns(2)

with col1:
    is_device = st.checkbox("Password Create", value=True)
    length = st.slider('Password Length', value=10, max_value=15)

# Function  
def generate_password(length):
    all_chars = char + Nuchar + spchar
    password = ''.join(random.sample(all_chars, length))
    return password

if st.button('Generate Password'):
    generated_password = generate_password(length)
    st.session_state.generated_password = generated_password
    
# pyperclip for copy password
if 'generated_password' in st.session_state:
    st.text_input("Generated Password", value=st.session_state.generated_password, key='generated_password_display')

    if st.button('Copy Password'):
        pyperclip.copy(st.session_state.generated_password)
        st.success('Password copied to clipboard:)')

# Instructions
st.write("""
- Click On "Generate Password " and Password Generate for you
- Click "copy Password" Password is Password copied to clipboard!
- every time click on Generated Password button new password is create 
""")
