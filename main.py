from NLP import *
from crop_pred import *
from rain_pred import *






from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import tkinter as tk
import requests
import time

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


main = Tk()
main.geometry("500x650")
main.title("AgriBot")


def ask_from_bot():
    query = textF.get()

    if query[0:2] != "./":
        msgs.insert(END, "you: " + query)
        state, district, subdivison, crop, year, month, rainfall, crp = NLP_main(query)
        if (crop != None and rainfall):
            a, b= crop_prediction(crop.capitalize())
            msgs.insert(END, "bot: " + "Required Rainfall " + str(a))
            msgs.insert(END, "bot: " + "Suitable States "+str(b))

        elif (rainfall != None and month != None and subdivison):
            msgs.insert(END, "bot: " + str(rain_prediction(subdivison.upper(), month[0:3].upper())))
        elif (state and crp):
            c, d = state_prediction(state.capitalize())
            msgs.insert(END, "bot: " + "Crops "+str(d))
            msgs.insert(END, "bot: " + "Average Rainfall of this state " + str(c))
        elif (state and rainfall):
            e, f = state_prediction(state.capitalize())
            msgs.insert(END, "bot: " + "Average Rainfall of this state " + str(e))

        else:
            msgs.insert(END, "bot: " + "Sorry. I didn't get you. Please try to ask something relevant.")
        #answer_from_bot = bot.get_response(query)


        # msgs.insert(END, "bot: " + str(answer_from_bot))

        textF.delete(0, END)
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


        msgs.insert(END, "you: " + query)
        msgs.insert(END, "bot: " + str(final_info) , str(final_data1), str(final_data2), str(final_data3))
        textF.delete(0, END)
        #
    else:
        print("Wrong input")


frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()

textF = Entry(main, font=("Times New Roman", 18))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask", font=("Times New Roman", 18), command=ask_from_bot)
btn.pack()
main.mainloop()