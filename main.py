from tkinter import*
screen=Tk()
screen.geometry("680x600")
screen.title("temprature convert🌡")
screen.config(background="MediumPurple1")
def convert_temp():
    temp=float(put.get())
    real=str(((temp) * 9/5) + 32)
    aswer.config(text=real)
title=Label(screen,text="celcius to farenheight converter",bg="CadetBlue1",fg="MediumPurple1",font=("Lola",15,"bold"))
title.grid(row=1,column=1,padx=140,pady=50)
enter=Label(screen,text="enter the temprature in celcius you want to convert",bg="CadetBlue1",fg="MediumPurple1",font=("Lola",15,"bold"))
enter.grid(row=2,column=1,padx=0,pady=50)
put=Entry(screen)
put.grid(row=2,column=2,padx=0,pady=50)
submit=Button(screen,text="Submit",bg="CadetBlue1",fg="MediumPurple1",font=("Lola",15,"bold"),command=convert_temp)
submit.grid(row=3,column=1,padx=90,pady=50)
aswer=Label(screen,bg="MediumPurple1",fg="CadetBlue1",font=("Lola",15,"bold"))
aswer.grid(row=4,column=1,padx=100,pady=50)
screen.mainloop()
#makelabels and buttons n stuff
#Complete the Layout for the temp convertor
#Make a function that gets the number you enter inside the entry box to enter the temp in Celsius and use the below formula to convert it to Farenheit
#temp_fahrenheit = (float(temp_celsius) * 9/5) + 32

