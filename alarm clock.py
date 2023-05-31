# import datetime
# s=input("j")
# time=datetime.datetime.strptime(s,"%H:%M:%S")
# # print(time.hour)
# print(datetime.datetime.now().time().strftime("%H:%M:%S")) 
import tkinter as tk
from tkinter import *
from datetime import datetime
from playsound import playsound
window=Tk()
window.geometry("600x700")
window.title("alarm clock")
window.config(bg="pink")

alarm=Label(window,text="enter alarm time : ",bg="pink",font=20)
alarm.place(x="90",y="100")

text_label=Label(window,text="",bg="pink")
text_label.place(x="300",y="100")

alarm_e=Entry(window)
alarm_e.place(x="240",y="100")


def check_time():
    try:
        time_user=alarm_e.get()
        time_user=datetime.strptime(time_user,"%H:%M:%S")
        if time_user==datetime.now().time().strftime("%H:%M:%S"):
            playsound("City Lights.mp3")
    except:
        text_label.config(text="invalid")
        
        
def set_alarm():        
    try:
        datetime.strptime(time_user,"%H:%M:%S")
        text_label.config(text="alarm successfull")
        while True:
            window.update()
            check_time()
    except ValueError:
        text_label.config(text="Invalid alarm time!")
                
Button(window,text="alarm",command=set_alarm).place(x="280",y="200")        
window.mainloop()