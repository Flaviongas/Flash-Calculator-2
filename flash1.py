import time
import tkinter
from tkinter import messagebox
raiz = tkinter.Tk()

raiz.title("Flash Calculator")
raiz.resizable(False, False)
raiz.geometry("650x350")

miFrame = tkinter.Frame()
miFrame.pack()
miFrame.config(width="650", height="350")
miFrame.config(bd=35)
miFrame.config(relief="groove")

miLabel = tkinter.Label(miFrame, text="Flash Calculator 2", font=("Helvetica", 30)).place(x=140, y=10)


def top():
        time.sleep(5)
        tkinter.messagebox.showinfo(message="FLASH", title="El top tiene flash")

def jg():
    time.sleep(5)
    tkinter.messagebox.showinfo(message="FLASH", title="El jg tiene flash")

def mid():
    time.sleep(5)
    tkinter.messagebox.showinfo(message="FLASH", title="El mid tiene flash")

def adc():
    time.sleep(5)
    tkinter.messagebox.showinfo(message="FLASH", title="El adc tiene flash")

def supp():
    time.sleep(5)
    tkinter.messagebox.showinfo(message="FLASH", title="El supp tiene flash")

boton1 = tkinter.Button(
  miFrame,
  text = "TOP",
  command = top
)
boton1.pack()
boton1.place(x=290, y=290)




raiz.mainloop()
