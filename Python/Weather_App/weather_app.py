from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather Forecast Application")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    try:
        city = search_location.get()
    
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        lon = str(location.longitude)
        lat = str(location.latitude)
    
    
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
    
        #weather
        api = "https://api.openweathermap.org/data/2.5/weather?lat="+ lat +"&lon="+ lon +"&appid=4a98440f905b7643d7992b17457cac68"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
    
        temp_lbl.config(text=(temp,"°C"))
        condition_lbl.config(text=(condition,"|","FEELS","LIKE",temp,"°C"))
    
        wind_data.config(text=wind)
        humidity_data.config(text=humidity)
        description_data.config(text=description)
        pressure_data.config(text=pressure)
        
    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!! Please Enter a City")
    
    
#search box
search_image = PhotoImage(file="images\search_bar.png")
search_bar = Label(image=search_image)
search_bar.place(x=20,y=20)

search_location = tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
search_location.place(x=50,y=40)
search_location.focus() 

search_icon = PhotoImage(file="images\search_icon.png")
search_icon_btn = Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
search_icon_btn.place(x=400,y=34)

#logo
logo_image = PhotoImage(file="images\weather_logo.png")
weather_logo = Label(image=logo_image)
weather_logo.place(x=150,y=100)

#Bottom Box with Forecast Information
frame_image = PhotoImage(file="images\data_box.png")
data_box = Label(image=frame_image)
data_box.pack(padx=5,pady=5,side=BOTTOM)

#time
name = Label(root,font=("arial"))
name.place(x=30,y=100)
clock = Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#Individual labels with forecast data 
wind_lbl = Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
wind_lbl.place(x=120,y=400)

humidity_lbl = Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
humidity_lbl.place(x=250,y=400)

description_lbl = Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
description_lbl.place(x=430,y=400)

pressure_lbl = Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
pressure_lbl.place(x=650,y=400)

temp_lbl = Label(font=("arial",70,"bold"),fg="#ee666d")
temp_lbl.place(x=400,y=150)
condition_lbl = Label(font=("arial",15,"bold"))
condition_lbl.place(x=400,y=250)

wind_data = Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
wind_data.place(x=120,y=430) 

humidity_data = Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
humidity_data.place(x=280,y=430) 

description_data = Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
description_data.place(x=450,y=430) 

pressure_data = Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
pressure_data.place(x=670,y=430) 


















root.mainloop()