

import textwrap
from datetime import datetime

from NLP import *
from crop_pred import *
from rain_pred import *

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import tkinter as tk
import tkinterpp
import requests
import time
import numpy as np

bot = ChatBot("my bot")

conv = [
    'hello',
    'hi there',
    'what is your name ?',
    'My name is bot ',
    'how are you?',
    'I am doing great these days ',
    ' thank you',
    'In which city you live ?',
    'I live in pune',
    'In which language you talk ?',
    'I mostly talk in english'
]

trainer = ListTrainer(bot)
trainer.train(conv)

root = Tk()
root.config(bg="#7dcfb6")
root.geometry('410x600+400+100')


canvas = Canvas(root, width=200, height=200,bg="white")
canvas.grid(row=0,column=0,columnspan=2)
canvas.place(x=10, y=10, width=390, height=530)

root.resizable(False, False)

img = PhotoImage(file="farm.png")

root.iconphoto(False, img)
root.title("AgroBot")

# photoL = Label(root, image=img)
#
# photoL.pack(pady=5)

# label = Label(root, text = "Ask your queries", height = 1, width =40 , font=12)
# label.pack(pady=5)

bubbles = []

#class BotBubble:

def botbubble(self,master,message=""):
        self.master = master
        self.frame = Frame(master,bg="light green")
        self.i = self.master.create_window(70,490,window=self.frame)

        Label(self.frame,text=datetime.now().strftime("%d-%m-%Y %X"),font=("times new roman", 7),bg="light green").grid(row=0,column=0,sticky="w",padx=5)
        Label(self.frame, text=textwrap.fill(message, 25), font=("times new roman", 9),bg="light green").grid(row=1, column=0,sticky="w",padx=5,pady=3)
        root.update_idletasks()
        self.master.create_polygon(self.draw_triangle(self.i), fill="light green", outline="light green")


def draw_triangle(self,widget):
        x1, y1, x2, y2 = self.master.bbox(widget)
        return x1, y2 - 10, x1 - 15, y2 + 10, x1, y2

# def send_message():
#     if bubbles:
#         canvas.move(ALL, 0, -80)
#     a = BotBubble(canvas,message=entry.get())
#     bubbles.append(a)

def search(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            return True
    return False

def ask_from_bot():
    # if bubbles:
    #     canvas.move(ALL, 0, -80)
    #     a = BotBubble(canvas,message=entry.get())
    #     bubbles.append(a)

    query = entry.get()

    if query== "":
        msgs.insert(END , "You:    " + query)
        msgs.insert(END, "AgriBot:    " + "Please Enter Something!!")

    elif query[0:2] != "./":
        msgs.insert(END,"You:    " + query)
        state, district, subdivison, crop, year, month, rainfall, crp , new_state_word , IsK= NLP_main(query)
        if (crop != None and rainfall):
            a, b= crop_prediction(crop.capitalize())
            msgs.insert(END, "AgriBot:    " + "Required Rainfall " + str(a))
            splits = np.array_split(b, 3)
            msgs.insert(END, "AgriBot:    " + "Suitable States "+ str(splits[0]), str(splits[1]), str(splits[2]))

        elif (rainfall != None and month != None and (subdivison or state)):
            msgs.insert(END, "AgriBot:    " + str(rain_prediction(subdivison.upper(), month[0:3].upper())))

        elif (state and crp and IsK):
            c, d = state_prediction(state.capitalize())
            flag = 0
            if crop.capitalize() in d:
                flag = 1
            else:
                flag = 0

            if flag==1:
                msgs.insert(END, "AgriBot:    " + " Yes!!. It is grown in " + state)
            else:
                msgs.insert(END, "AgriBot:    " + " No. It is not grown in " + state)


        elif (state and crp):
            c, d = state_prediction(state.capitalize())
            splits = np.array_split(d, 3)
            msgs.insert(END, "AgriBot:    " + "Crops " + str(splits[0]), str(splits[1]), str(splits[2]))
            msgs.insert(END, "AgriBot:    " + "Average Rainfall - " + str(c))



        elif (new_state_word!=None and crp):
            c, d = crop_prediction(crop.capitalize())
            splits = np.array_split(d, 3)
            msgs.insert(END, "AgriBot:    " + "Suitable States " + str(splits[0]), str(splits[1]), str(splits[2]))


        elif (state and rainfall):
            e, f = state_prediction(state.capitalize())
            msgs.insert(END, "AgriBot:    " + "Average Rainfall of this state " + str(e))

        else:
            msgs.insert(END, "AgriBot:    " + "Sorry. I didn't get you. Please try to ask something relevant.")
        #answer_from_bot = bot.get_response(query)


        # msgs.insert(END, "bot: " + str(answer_from_bot))

        entry.delete(0, END)
    elif query[0:2] == "./":
        city = query[2:]
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06c921750b9a82d8f5d1294e1586276f"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
        sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

        final_info = condition + ": " + str(temp) + "°C" +"          "+ "Wind Speed: " + str(wind)
        final_data1 = "\n" + "Min Temp: " + str(min_temp) + "°C" +"          "+ "Max Temp: " + str(max_temp) + "°C"
        final_data2 = "Pressure: " + str(pressure) + "          " + "Humidity: " + str(
            humidity)

        final_data3 =  "Sunrise: " + sunrise + "          " + "Sunset: " + sunset


        msgs.insert(END,"\n"+"You:    " + query)
        msgs.insert(END, "AgriBot:    " + str(final_info) , str(final_data1), str(final_data2), str(final_data3))
        entry.delete(0, END)
        #
    else:
        print("Wrong input")

sc = Scrollbar(root)
msgs = Listbox(canvas, width=150, height=15,yscrollcommand = sc.set, fg='#00b2ca')
msgs.insert(1, "AgriBot:     Ask your queries here")
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)

sc.config( command = msgs.yview )

entry = Entry(root,width=26, font=("FarmerBot", 10))
entry.place(x=10, y=550, width=290, height=40)


#buton
#img = PhotoImage(file="6532019.png")
buton = Button(root, width=8, height=2, relief='raised',state='active',command=ask_from_bot)
buton.config(text='Send', bg='#00b2ca', font='Verdana 8 bold')
buton.place(x=310, y=550)
#root.wm_attributes('-transparentcolor', '')
label = Label(root, text = "Please Enter ./cityname for live weather", height = 1, width =80,fg='blue',bg='#7dcfb6')
label.pack()

root.mainloop()