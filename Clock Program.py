from tkinter import *
from time import *

def update():
    #strftime kütüphanesinin çeşitli yazım özellikleri mevcut.
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)
    window.after(1000,update)
    #her 1000 milisaniyede bir update fonksiyonunu çağırır.


window = Tk()
window.title("This is a Clock Program")
time_label = Label(window,font=("Verdana",50),fg="#00FF00",bg="black")
time_label.pack()

day_label = Label(window,font=("Consolas",25))
day_label.pack()

date_label = Label(window,font=("Ink Free",25))
date_label.pack()

update()


#window.geometry("500x500")
window.mainloop()