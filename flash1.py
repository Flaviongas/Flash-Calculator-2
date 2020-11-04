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
  height=5,
  width=12,
  command = top
)
boton1.pack()
boton1.place(x=0, y=150)


boton2 = tkinter.Button(
  miFrame,
  text = "JG",
  height=5,
  width=12,
  command = jg
)
boton2.pack()
boton2.place(x=120, y=150)


boton3 = tkinter.Button(
  miFrame,
  text = "MID",
  height=5,
  width=12,
  command = mid
)
boton3.pack()
boton3.place(x=240, y=150)


boton4 = tkinter.Button(
  miFrame,
  text = "ADC",
  height=5,
  width=12,
  command = adc
)
boton4.pack()
boton4.place(x=360, y=150)


boton5 = tkinter.Button(
  miFrame,
  text = "SUPP",
  height=5,
  width=12,
  command = supp
)
boton5.pack()
boton5.place(x=480, y=150)




raiz.mainloop()
