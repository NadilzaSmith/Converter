import tkinter

from tkinter import *

screen = tkinter.Tk()


def miles_kms():
    miles = float(input1.get())
    km = round(miles * 1.609)
    text3.config(text=f"{km}")


screen.title(" Mile to Km Converter ")
screen.minsize(width=300, height=200)
screen.config(padx=60, pady=60)

input1 = Entry(width=10, )
input1.grid(column=1, row=0)

text1 = Label(text="Miles")
text1.grid(column=2, row=0)

text2 = Label(text="is equal to")
text2.grid(column=0, row=1)

text3 = Label(text="0")
text3.grid(column=1, row=1)

text4 = Label(text="Km")
text4.grid(column=2, row=1)

botao = Button(text="Calculete", command=miles_kms)
botao.grid(column=1, row=2)

screen.mainloop()


