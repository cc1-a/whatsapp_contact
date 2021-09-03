#!/usr/bin/env python
# imoprts 
from tkinter import Label,Button,Tk, Canvas, Entry, PhotoImage
from PIL import Image, ImageTk
from twilio_api import send_message




# meta

root=Tk()
root.resizable(False, False)

canvas=Canvas(root,width=100, height=100)
canvas.grid(columnspan=3, rowspan=3)

# functions
def make(val_1,val_2,val_3):
    body='Hellow Sir!\nWe have a new scout \n Name:'+str(val_1)+'\n School:'+str(val_3)+'\n Contact_no:'+str(val_2)
    send_message(body, val_2)
# gui
logo=  Image.open('logo.png')
resized_image= logo.resize((300,300), Image.ANTIALIAS)
logo= ImageTk.PhotoImage(resized_image)


Logo_label= Label(image=logo)

Logo_label.image=logo
Logo_label.grid(column=1, row=0)
btn_img= PhotoImage(file='index.png')


e1 = Entry(root, font='Times 20 italic ')

e1.insert(0, "Enter Name")
e1.grid(column=1,row=2, pady=5)



e2 = Entry(root, font='Times 20 italic ')

e2.insert(0, "Enter Phone number")
e2.grid(column=1,row=3, pady=5)



e3 = Entry(root, font='Times 20 italic ')
e3.insert(0, "Enter  School")
e3.grid(column=1,row=4, pady=5)




btn_1= Button(root, image=btn_img, command=lambda:make(val_1=e1.get(), val_2=e2.get(),val_3=e3.get()))
btn_1.grid(column=1,row=5, pady=5)


root.mainloop()