import time

flashtop=input(str("¿Quien gastó flash?"))

flash_1 = 285
flash_2 = 285
flash_3 = 285
flash_4 = 285
flash_5 = 285

if flashtop=="top":
    for i in range(0,285,+1):
        print (i)
        time.sleep(0.0001)
elif flashtop=="jg":
    for i in range(0,285,+1):
        print (i)
        time.sleep(0.0001)
elif flashtop=="mid":
    for i in range(0,285,+1):
        print (i)
        time.sleep(0.0001)
elif flashtop=="adc":
    for i in range(0,285,+1):
        print (i)
        time.sleep(0.0001)
elif flashtop=="supp":
    for i in range(0,285,+1):
        print (i)
        time.sleep(0.0001)
else: print("Pon una linea en minusculas pelotudo")


if(flash_1==285):
    print('Toplaner tiene flash, saco wea')
elif(flash_2==285):
    print('El Jungler tiene flash, saco wea')
elif(flash_3==285):
    print('Midlaner tiene flash, saco wea')
elif(flash_4==285):
    print('El Adcarry tiene flash, saco wea')
elif(flash_5==285):
    print('El Support tiene flash, saco wea')
