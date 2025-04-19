from tkinter import *
from time import strftime
import datetime

root = Tk()
root.title("Digital Clock")
root.geometry("600x300")
root.configure(bg="#f0f4f8")

def clock():
    current_time = strftime("%I:%M:%S %p")
    current_date = datetime.datetime.now().strftime("%A, %d %B %Y")
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    location_label.config(text="📍 New Delhi, India")
    time_label.after(1000, clock)

font_family = "Segoe UI"

time_label = Label(root, font=(font_family, 55, "bold"), fg="#2c3e50", bg="#f0f4f8")
time_label.pack(anchor="center", pady=(30, 10))

date_label = Label(root, font=(font_family, 20), fg="#34495e", bg="#f0f4f8")
date_label.pack(anchor="center", pady=5)

location_label = Label(root, font=(font_family, 16), fg="#2980b9", bg="#f0f4f8")
location_label.pack(anchor="center", pady=5)

clock()
mainloop()
