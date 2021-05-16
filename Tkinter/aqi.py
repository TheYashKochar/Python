# Program to Show Air Quality Index using AirNow API
# Color changes according to the Air Quality
# Please Generate Your API key to run the program
from tkinter import *
from PIL import ImageTk,Image
import requests
import json
root = Tk()
root.title('Air Quality Index')
root.geometry('400x100')
#root.configure(background= 'green')
# https://www.airnowapi.org/aq/observation/zipCode/historical/?format=application/json&zipCode=89129&date=2021-05-08T00-0000&distance=5&API_
key=r'Paste Your Here'

def ziplookup():
    '''
    zipcode.get()
    ziplabel = Label(root,text=zipcode.get())
    ziplabel.grid(row=1,column=0,columnspan=2)
    '''

    try:
        api_request = requests.get('https://www.airnowapi.org/aq/observation/zipCode/historical/?format=application/json&zipCode='+ zipcode.get() +'&date=2021-05-08T00-0000&distance=5&API_KEY=' +key) #')
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality= api[0]['AQI']
        category=  api[0]['Category']['Name']
        if category == 'Good':
            weather_color = '#0C0'
        elif category == 'Moderate':
            weather_color = '#FFFF00'
        elif category == 'Unhealthy for Sensitive Groups':
            weather_color = '#FF9900'
        elif category == 'Unhealthy':
            weather_color = '#FF0000'
        elif category == 'Very Unhealthy':
            weather_color = '#990066'
        elif category == 'Hazardous':
            weather_color = '#660000'
        root.configure(background= weather_color)
        my_label= Label(root,text=city + " Air Quality " + str(quality) + " " + category, font=('Helvetica',20),background=weather_color) #'green')
        my_label.grid(row=1,column=0, columnspan=2)

    except Exception as e:
        api = 'Error...'


zipcode = Entry(root)
zipcode.grid(row=0,column=0,stick = W+E+N+S)

zipbutton = Button(root,text='Lookup Zipcode', command=ziplookup)
zipbutton.grid(row=0,column=1,stick = W+E+N+S)

root.mainloop()