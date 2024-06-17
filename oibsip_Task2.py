#               DABHI DHRUVI R
#              BMI  Calculator
# Task2






import random
import tkinter
from tkinter import *
import tkinter.messagebox
from PIL import Image,ImageTk
# import ttkbootstrap
# from ttkbootstrap import *


# windows = tkinter.Tk()
windows = tkinter.Tk()
# windows = tkinter.Wind.ow(themename="morph")
windows.title("BMI  Calculator")
windows.geometry("550x550+610+130")
windows.config(bg='black')
windows.resizable(False,False)

# Function to calculate BMI
def BMI():
    try:
        height_value = float(height.get())
        weight_value = float(weight.get())
        result = weight_value / (height_value / 100) ** 2
        
        if result < 16:
            result_text = "Severely underweight"
        elif result >= 16 and result < 18.5:
            result_text = "Underweight"
        elif result >= 18.5 and result < 25:
            result_text = "Healthy"
        elif result >= 25 and result < 30:
            result_text = "Overweight"
        else:
            result_text = "Obese"
        
        Ans.config(text=f"{result_text}:BMI:{result:2f}")
    except:
        tkinter.messagebox.showerror("Invalied input  only numeric vlues allowed")
    

# For image 
def visual():
    try:
        image = Image.open("BMI.png")
        image_image = ImageTk.PhotoImage(image)
        image_View = tkinter.Toplevel(windows)
        image_View.title("BMI Visualization")
        image_View.geometry("400x400")
        image_View.config(bg="black")
        label = tkinter.Label(image_View, image=image_image, bg="black")
        label.image = image_image  # keep a reference!
        label.pack(pady=10)
        image_Close = tkinter.Button(image_View,text="Close",command=image_View.destroy)
        image_Close.pack()
    except:
        tkinter.messagebox.showerror("Image not found")
    
# label = Label(windows,text='BMI  Calculator',font=('Times New Roman',16),bg="black",fg='white').pack(side='top')
# label = Label(windows,text="For convert Your height In to cm example(5)[foot]*(30.48)=152.4",font=('Times New Roman',11,),fg="red").place(x=30,y=10)
# 
label = Label(windows,text='Enter Your Height in Cm',font=('Times New Roman',16),bg="black",fg='White').place(x=120,y=60)

height = tkinter.Entry(windows, font=('Times New Roman', 18), bd=4, fg="Black", bg="white")
height.place(x=120, y=110)

welabel =Label(windows, text='Enter Your Weight in Kg', font=('Times New Roman', 16), bg="black", fg='White')
welabel.place(x=120, y=170)

weight = tkinter.Entry(windows, font=('Times New Roman', 18), bd=4, fg="Black", bg="white")
weight.place(x=120, y=230)

# Viewbtn = ttkbootstrap.Button(windows, text="Check Your BMI", command=BMI)
# Viewbtn.place(x=120, y=230)
Viewbtn = tkinter.Button(windows, text="Check Your BMI",border=2,bg="Green",fg="White",font=('Times New Roman', 16), command=BMI)
Viewbtn.place(x=120, y=290)

Ans = tkinter.Label(windows, text="you get Your BMI",bg="Green",fg="White", font=('Times New Roman', 16))
Ans.pack(side="bottom")


view = tkinter.Button(windows, text="BMI Visualisation",bg="black",fg="white", font=('Times New Roman', 16),command=visual)
view.pack(side="bottom")



windows.mainloop()
