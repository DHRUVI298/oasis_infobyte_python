#                   DABHI DHRUVI R
#                   Password Generator     


import random
import tkinter
from tkinter import *
import tkinter.messagebox
import streamlit as st
import threading
import subprocess
import os


def tkinter_app():
    window = tkinter.Tk()
    window.title("Password Generator")
    window.geometry("410x450+510+130")
    window.resizable(False,False)
    window.config(bg="#576CB3")

    label = Label(window,text='Password Generator',font=('Times New Roman',21),bg="black",fg='#00ffff').pack(side='top')

    frame = Frame(window,width=420,height=45,bg="white").place(x=0,y=50)
    Result = Entry(frame,width=18,font=('Times New Roman',),bd=0)
    Result.place(x=77,y=55)
    Result.focus()

    clen1 = IntVar()
    clen2 = IntVar()
    clen3 = IntVar()
    clen4 = IntVar()

    def password_click(lenth):
        try:
            validchar = "(qwertyui!&_-/opasdfghjklzxcvbnm1234567890ASDFGHJKLPOIUYTREWQZXCVBNM@#$)"
            password = "".join(random.sample(validchar,lenth))
            Result.delete(0,tkinter.END)
            Result.insert(0,password)
        except:
            pass

    def checkbox_click():
        if clen1.get()==6:
            password_click(6)
        elif clen2.get()==8:
            password_click(8)
        elif clen3.get()==10:
            password_click(10)
        elif clen4.get()==12:
            password_click(12)
        else:
            password_click(15)

    def copy_text():
        password = Result.get()
        if password:
            window.clipboard_clear()
            window.clipboard_append(password)  
            tkinter.messagebox.showinfo(f"Password Copy{password}")
        else:
            tkinter.messagebox.showwarning(f"Oops Password is Not Copy{password}")

    Clenone = tkinter.Radiobutton(text=' 6 character   ',font=('Times New Roman',),fg="#00ffff",bg="black",variable=clen1,value=6)
    Clenone.place(x=77,y=98)
    Clentwo = tkinter.Radiobutton(text='8 character    ',font=('Times New Roman',),fg="#00ffff",bg="black",variable=clen2,value=8)
    Clentwo.place(x=77,y=150)
    Clenthree = tkinter.Radiobutton(text='10 character ',font=('Times New Roman',),fg="#00ffff",bg="black",variable=clen3,value=10)
    Clenthree.place(x=77,y=200)
    Clenfour = tkinter.Radiobutton(text='12 character  ',font=('Times New Roman',),fg="#00ffff",bg="black",variable=clen4,value=12)
    Clenfour.place(x=77,y=250)

    password = tkinter.Button(text='Generate password:)',font=('Times New Roman',21),bg="black",fg="white",command=checkbox_click)
    password.pack(side='bottom')
    label = Label(window,text='Without clicked checkbox then 15 letter strong password generate',fg="lightgreen",bg="Red",font=('times new roman',11,))
    label.pack(side='bottom')
    btn = Button(frame,text='Copy',font=('Times New Roman',),width=5,bg="black",fg="#00ffff",bd=0,command=copy_text)
    btn.place(x=340,y=55)

    window.mainloop()
    
# Streamlit logic write in new.py  so user select this then this file excuted in my language 
def streamlit_app():
    subprocess.run(["streamlit", "run", "new.py"])



# This is Main bec inthis i ask user in which mode they see there View as per choice function call
def main():
    choice = input("Enter 'tkinter' to run the Tkinter app or 'streamlit' to run the Streamlit app Enter Any one : ").strip().lower()
    if choice == 'tkinter':
        tkinter_app()
    elif choice == 'streamlit':
        streamlit_app()
    else:
        print("Invalid choice. Please enter 'tkinter' or 'streamlit'.")

if __name__ == "__main__":
    main()


# New.py
# import streamlit as st
# import random
# import pyperclip

# spchar = "~!@#$%^&*()<>?'{}[]\-_+-*./"
# char = "qwertyuiopasdfghjklzxmnbvc"
# Nuchar = "123456789010ASDFGHJKLPOIUYTREQXCVBNMZ"

# st.title("Password Generator")

# col1, col2 = st.columns(2)

# with col1:
#     is_device = st.checkbox("Password Create", value=True)
#     length = st.slider('Password Length', value=10, max_value=15)

# # Function  
# def generate_password(length):
#     all_chars = char + Nuchar + spchar
#     password = ''.join(random.sample(all_chars, length))
#     return password

# if st.button('Generate Password'):
#     generated_password = generate_password(length)
#     st.session_state.generated_password = generated_password
    
# # pyperclip for copy password
# if 'generated_password' in st.session_state:
#     st.text_input("Generated Password", value=st.session_state.generated_password, key='generated_password_display')

#     if st.button('Copy Password'):
#         pyperclip.copy(st.session_state.generated_password)
#         st.success('Password copied to clipboard:)')

# # Instructions
# st.write("""
# - Click On "Generate Password " and Password Generate for you
# - Click "copy Password" Password is Password copied to clipboard!
# - every time click on Generated Password button new password is create 
# """)
