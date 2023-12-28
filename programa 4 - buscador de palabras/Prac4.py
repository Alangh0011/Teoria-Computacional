
from tkinter import*

archivo = open("Datos6.txt", "r")

web = [ ] #
website = [ ] #
webpage = [ ] #
webmaster = [ ] #
webhome = [ ] #
coin = [ ] #

ebay = [ ]

email = [ ] #
electronic = [ ] #


contador = 0
estado = 1

palabras = archivo.read()

for letra in palabras:

    contador = contador + 1

    if (estado == 1):
        if (letra == "w"):
            estado = 2
        elif (letra == "e"):
            estado = 21
        elif(letra == "c"):
            estado = 22
        else:
            estado = 1
        continue

    if (estado == 2):
        if (letra == "w"):
            estado = 2
        elif (letra == "e"):
            estado = 3
        elif(letra == "c"):
            estado = 22
        else:
            estado = 1
        continue

    if (estado == 3):       #e
        if (letra == "w"):
            estado = 2
        elif(letra == "e"):
            estado = 3
        elif(letra == "c"):
            estado = 22
        elif(letra == "b"):
            estado = 4
            #print ("web")
            web.append(contador-3) #por el tamaño de la palabra web recorremos 3 caracteres para obtener el incio
        else:
            estado = 1
        continue

    if (estado == 4):
        
        if (letra == "w"):
            estado = 2
        if (letra == "e"):
            estado = 21
        elif(letra == "s"):
            estado = 5
        elif(letra == "m"):
            estado = 9
        elif(letra == "h"):
            estado = 131
        elif(letra == "p"):
            estado = 15
        else:
            estado = 1

        continue

    if (estado == 5):
        if (letra == "w"):
            estado = 2
        elif(letra == "e"):
            estado = 21
        elif(letra == "c"):
            estado = 22
        elif(letra == "i"):
            estado = 6
        else:
            estado = 1
        continue

    if (estado == 6):
        if (letra == "w"):
            estado = 2
        elif(letra == "e"):
            estado = 21
        elif(letra == "c"):
            estado = 22
        elif(letra == "t"):
            estado = 7
        else:
            estado = 1
        continue

    if (estado == 7):
        if (letra == "w"):
            estado = 2
        elif(letra == "c"):
            estado = 22
        elif(letra == "e"):
            #print ("website")
            ebay.append(contador-7) 
            estado = 8
        else:
            estado = 1
        continue

    if (estado == 8):
        if (letra == "w"):
            estado = 2
        elif(letra == "e"):
            estado = 21
        elif(letra == "c"):
            estado = 22
        else:
            estado = 1
        continue

    if (estado == 9): #m
        if (letra == "w"):
            estado = 2
        elif(letra == "e"):
            estado = 21
        elif(letra == "c"):
            estado = 22
        elif(letra == "a"):
            estado = 10
        else:
            estado = 1
        continue

    if (estado == 10):
        if (letra == "s"):
            estado = 11
        elif(letra == "g"):
            estado = 13
        else:
            estado = 1
        continue

    if (estado == 11):
        if (letra == "w"):
            estado = 2
        elif(letra == "e"):
            estado = 21
        elif(letra == "c"):
            estado = 22
        elif(letra == "t"):
            estado = 12
        else:
            estado = 1
        continue

    if (estado == 12):
        if (letra == "w"):
            estado = 2
        elif(letra == "c"):
            estado = 22
        elif(letra == "e"):
            estado = 13
        else:
            estado = 1
        continue

    if (estado == 13):
        if (letra == "w"):
            estado = 2
        elif(letra == "e"):
            estado = 21
        elif(letra == "c"):
            estado = 22
        elif(letra == "r"):
            #print ("webmaster")
            webmaster.append(contador-9)
            estado = 14
        else:
            estado = 1
        continue

    if (estado == 14):
        if (letra == "w"):
            estado = 2
        elif(letra == "e"):
            estado = 21
        elif(letra == "c"):
            estado = 22
        else:
            estado = 1
        continue
    
    if (estado == 131):
        if (letra == "w"):
            estado = 2
        elif(letra == "e"):
            estado = 21
        elif(letra == "c"):
            estado = 22
        elif(letra == "o"):
            estado = 141
        else:
            estado = 1
        continue
    
    if (estado == 141):
        if (letra == "w"):
            estado = 2
        elif(letra == "e"):
            estado = 21
        elif(letra == "c"):
            estado = 22
        elif(letra == "m"):
            estado = 151
        else:
            estado = 1
        continue
    
    if (estado == 151):
        if (letra == "w"):
            estado = 2
        elif(letra == "c"):
            estado = 22
        elif(letra == "e"):
         #print ("webhome")
         webhome.append(contador-7)
         estado = 21
        else:
            estado = 1
        continue
    
    if (estado == 15):
        if (letra == "w"):
            estado = 2
        elif(letra == "e"):
            estado = 21 
        elif(letra == "c"):
            estado = 22
        elif(letra == "a"):
            estado = 16
        else:
            estado = 1
        continue

    if (estado == 16):
        if (letra == "w"):
            estado = 2
        elif(letra == "e"):
            estado = 21
        elif(letra == "c"):
            estado = 22
        elif(letra == "g"):
            estado = 17
        else:
            estado = 1
        continue

    if (estado == 17):
        if (letra == "w"):
            estado = 2
        elif(letra == "e"):
            #print ("webpage")
            webpage.append(contador-7)
            estado = 21
        elif(letra == "c"):
            estado = 22
        else:
            estado = 1
        continue
    
    if (estado == 19):
        if (letra == "w"):
            estado = 2
        elif(letra == "c"):
            estado = 22
        elif(letra == "y"):
            #print ("ebay")
            ebay.append(contador-4)
            estado = 14
        else:
            estado = 1
        continue
    
    if (estado == 20):
        if (letra == "w"):
            estado = 2
        elif(letra == "c"):
            estado = 22
        elif(letra == "a"):
            estado = 19
        else:
            estado = 1
        continue

    if (estado == 21):
        if (letra == "w"):
            estado = 2
        elif(letra == "c"):
            estado = 22
        elif(letra == "b"):
            estado = 20
        else:
            estado = 1
        continue

    if (estado == 21):
        if (letra == "w"):
            estado = 2
        elif(letra == "e"):
            estado = 22
        elif(letra == "b"):
            estado = 12
        elif(letra == "m"):
            estado = 5
        elif(letra == "l"):
            estado = 6
        else:
            estado = 1
        continue

    if (estado == 22):
        if (letra == "w"):
            estado = 2
        elif(letra == "e"):
            estado = 21
        elif(letra == "o"):
            estado = 23
        else:
            estado = 1
        continue

    if (estado == 23):
        if (letra == "w"):
            estado = 2
        elif(letra == "e"):
            estado = 22
        elif(letra == "i"):
            estado = 24
        else:
            estado = 1
        continue

    if (estado == 24):
        if (letra == "w"):
            estado = 2
        elif(letra == "e"):
            estado = 22
        elif(letra == "n"):
            #print ("coin")
            coin.append(contador-4)
            estado = 14
        else:
            estado = 1
        continue

#web
print ("Web's encontrados:")
print (len(web))

print("En las posiciones")
for elementos in web:
    print (elementos,end=",")

#website
print ("\n\nWebsite's encontrados:")
print (len(website))

print("En las posiciones")
for elementos in website:
    print (elementos,end=",")

#webmaster
print ("\n\nwebmaster's encontrados:")
print (len(webmaster))

print("En las posiciones")
for elementos in webmaster:
    print (elementos,end=",")

#webhome
print ("\n\nWebhome's encontrados:")
print (len(webhome))

print("En las posiciones")
for elementos in webhome:
    print (elementos,end=",")

#ebay
print ("\n\nEbay's encontrados:")
print (len(ebay))

print("En las posiciones")
for elementos in ebay:
    print (elementos,end=",")
    
#webpage
print ("\n\nWebpage's encontrados:")
print (len(webpage))

print("En las posiciones")
for elementos in webpage:
    print (elementos,end=",")
    
#coin
print ("\n\nCoin's encontrados:")
print (len(coin))

print("En las posiciones")
for elementos in coin:
    print (elementos,end=",")



archivo.close()


##############

#Gráficos

ventana = Tk()
canv = Canvas(ventana,width=1500,height=1500)
ventana.geometry("1500x1500")
ventana.title('Automata Palabras')

canv.create_line(35, 190, 105, 100, width=2, fill='black')

canv.create_line(150, 85, 850, 85, width=2, fill='black')
canv.create_line(50, 215, 500, 215, width=2, fill='black')


canv.create_line(30, 240, 25, 450, width=2, fill='black')

canv.create_line(10, 465, 400, 465, width=2, fill='black')

#q0
canv.create_oval(10,190,60,240, fill="blue")

#website
canv.create_oval(100,60,150,110, fill="blue")

canv.create_oval(220,60,270,110, fill="blue")
canv.create_oval(225,65,265,105, fill="blue")

canv.create_oval(340,60,390,110, fill="blue")
canv.create_oval(460,60,510,110, fill="blue")
canv.create_oval(580,60,630,110, fill="blue")
canv.create_oval(700,60,750,110, fill="blue")

canv.create_oval(820,60,870,110, fill="blue")
canv.create_oval(825,65,865,105, fill="blue")

#ebay
canv.create_oval(140,190,190,240, fill="blue")
canv.create_oval(260,190,310,240, fill="blue")
canv.create_oval(380,190,430,240, fill="blue")
canv.create_oval(500,190,550,240, fill="blue")

canv.create_oval(505,195,545,235, fill="blue")



#email
canv.create_oval(140,440,190,490, fill="blue")
canv.create_oval(260,440,310,490, fill="blue")
canv.create_oval(380,440,430,490, fill="blue")
canv.create_oval(10,440,60,490, fill="blue")



n1= Label(ventana,text="w").place(x=50,y=120)

n1= Label(ventana,text="e").place(x=180,y=45)
n1= Label(ventana,text="b").place(x=300,y=45)
n1= Label(ventana,text="s").place(x=420,y=45)
n1= Label(ventana,text="i").place(x=540,y=45)
n1= Label(ventana,text="t").place(x=660,y=45)
n1= Label(ventana,text="e").place(x=780,y=45)


n1= Label(ventana,text="e").place(x=100,y=180)
n1= Label(ventana,text="b").place(x=220,y=180)
n1= Label(ventana,text="a").place(x=340,y=180)
n1= Label(ventana,text="y").place(x=460,y=180)







n1= Label(ventana,text="n").place(x=460,y=430)
n1= Label(ventana,text="c").place(x=140,y=335)

n1= Label(ventana,text="o").place(x=220,y=430)
n1= Label(ventana,text="i").place(x=340,y=430)




p0= Label(ventana,text="q1").place(x=25,y=205)

p0= Label(ventana,text="q2").place(x=115,y=75)
p0= Label(ventana,text="q3").place(x=235,y=75)
p0= Label(ventana,text="q4").place(x=355,y=75)
p0= Label(ventana,text="q5").place(x=475,y=75)
p0= Label(ventana,text="q6").place(x=595,y=75)
p0= Label(ventana,text="q7").place(x=715,y=75)
p0= Label(ventana,text="q8").place(x=835,y=75)


p0= Label(ventana,text="q9").place(x=155,y=205)
p0= Label(ventana,text="q10").place(x=275,y=205)
p0= Label(ventana,text="q11").place(x=395,y=205)
p0= Label(ventana,text="q12").place(x=515,y=205)



p0= Label(ventana,text="q22").place(x=155,y=455)
p0= Label(ventana,text="q23").place(x=275,y=455)
p0= Label(ventana,text="q24").place(x=395,y=455)
p0= Label(ventana,text="q27").place(x=20,y=455)


#lineas
#0-1

canv.place(x=0,y=0)
ventana.mainloop()