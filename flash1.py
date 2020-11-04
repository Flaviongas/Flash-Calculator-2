import time
import tkinter

raiz = tkinter.Tk()

raiz.title("Flash Calculator")
raiz.resizable(False,False)
raiz.geometry("650x350")

miFrame = tkinter.Frame()
miFrame.pack()
miFrame.config(width="650", height="350")
miFrame.config(bd=35)
miFrame.config(relief="groove")

miLabel = tkinter.Label(miFrame, text="Flash Calculator 2", font=("Helvetica",30)).place(x=140,y=10)
miLabel2 = tkinter.Label(miFrame, text="¿Quien gastó flash?",font=18).place(x=220,y=170)

Linea = tkinter.Entry(miFrame)
Linea.place(x=220,y=200)


raiz.mainloop()


flashtop = input(str)

flash_1 = 0
flash_2 = 0
flash_3 = 0
flash_4 = 0
flash_5 = 0

if flashtop == "top":
    for i in range(0, 285, +1):
        print(i)
        time.sleep(0.0001)
elif flashtop == "jg":
    for i in range(0, 285, +1):
        print(i)
        time.sleep(0.0001)
elif flashtop == "mid":
    for i in range(0, 285, +1):
        print(i)
        time.sleep(0.0001)
elif flashtop == "adc":
    for i in range(0, 285, +1):
        print(i)
        time.sleep(0.0001)
elif flashtop == "supp":
    for i in range(0, 285, +1):
        print(i)
        time.sleep(0.0001)
else:
    print("Pon una linea en minusculas pelotudo")






if (flash_1 == 285):
    print('Toplaner tiene flash, saco wea')
elif (flash_2 == 285):
    print('El Jungler tiene flash, saco wea')
elif (flash_3 == 285):
    print('Midlaner tiene flash, saco wea')
elif (flash_4 == 285):
    print('El Adcarry tiene flash, saco wea')
elif (flash_5 == 285):
    print('El Support tiene flash, saco wea')
