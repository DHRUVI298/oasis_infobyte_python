                    # DABHI DHRUVI R
                    # Weather APP
                    # task 4
                    
                    
                    
                    
                
import tkinter
from tkinter import *
import requests
from tkinter import messagebox
from PIL import Image,ImageTk
import ttkbootstrap
# windows =ttkbootstrap.tk
windows = ttkbootstrap.Window(themename="morph")
windows.title("Weather App")
windows.geometry('550x550')

# Function  use the open weather api
def all_infoweather(area):
    API_KEY = "8e44a61cc2a8f4eaf0c599737ca7a49d"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={area}&appid={API_KEY}"
    # url = f"https://api.openweathermap.org/data/2.5/weather?q={area}&appid={API_KEY}"
    req = requests.get(url)
    if req.status_code == 404:
        messagebox.showerror("Error","City Not Found☹")
        return None
    
    # jason file 
    # MAIN LOGIC 
    weather = req.json()
    # global weather ,image,tempe,info,location_label,country
    try:
        image = weather['weather'][0]['icon']
        tempe = weather['main']['temp'] - 273.15
        info = weather['weather'][0]['description']
        # description
        humidity = weather['main']['humidity']
        windspeed = weather['wind']['speed']
        area =  weather['name']
        country = weather['sys']['country']
    except:
        pass
    
    # THIS URL SO THE IMAGE ON ScREEN
    weather_icon_url = f"https://openweathermap.org/img/wn/{image}@2x.png"
    
    return(weather_icon_url,image,tempe,info,area,country,humidity,windspeed)

def serach():
    area = name.get()
    output = all_infoweather(area)
    if output is None:
        return
    # Getting result
    
    
    weather_icon_url,image,tempe,info,area,country,windspeed,humidity = output
    area_lebal.config(text=f"{area},{country}")
    
   
            # ALL ABOUT Weather ICON ,description and humidity and windspeed display on screen
    
    image_res = requests.get(weather_icon_url, stream=True)
    ico_display = Image.open(image_res.raw)
    icon_photo = ImageTk.PhotoImage(ico_display)
    imagelabel.config(image=icon_photo)
    imagelabel.image = icon_photo
    # 
    
    temp.config(text=f"Temperature: {tempe:.2f}°C")
    info_label.config(text=f"Description: {info}")
    hu_label.config(text=f"Humidity:{humidity}%")
    wi_label.config(text=f"Wind Speed:{windspeed} m/s")
   

    # temp.configure(text=f"Temperature:{tempe:.2f}.°C")
    # info_label.configure(text=f"Description:{info}")
    
    
    
# For Search Or user enter city name for this 
La = ttkbootstrap.Label(windows,text="Enter City OR Country Name  ",font=('Times New Roman',19),foreground="black").pack(side="top")
name = ttkbootstrap.Entry(windows,font=('Times New Roman',19),foreground="black")
name.pack()

# from display the information 
searchbtn = ttkbootstrap.Button(windows,text="Search",command=serach)
searchbtn.pack(pady=15)


# For enter City or country name
area_lebal = ttkbootstrap.Label(windows,font=('Times New Roman',22),foreground="black")
area_lebal.pack()

# Image
imagelabel = ttkbootstrap.Label(windows)
imagelabel.pack()

# Show temp
temp = Label(windows,foreground="black",font=('Times New Roman',22))
temp.pack()



# Weather info
info_label = Label(windows,foreground="black",font=('Times New Roman',18))
info_label.pack()

# for humididty
hu_label = Label(windows,font=('Times New Roman',18),foreground="black")
hu_label.pack()

# wind 
wi_label = Label(windows,font=('Time new Roman',18),foreground="black")
wi_label.pack()

windows.mainloop()
