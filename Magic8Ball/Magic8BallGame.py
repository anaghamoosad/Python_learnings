#!/usr/bin/env python
#Written by Tom Brough and Paul Sutton
# -*- coding: utf-8 -*-
#!/usr/bin/env python

#Please not I have used the code written by the authors above as a guideline for me to learn more about python.
#There are some modifications to the original code to include some additional features that I am learning.

import random
import tkinter
from tkinter import *
from PIL import Image
import tkinter.messagebox
import glob


window =Tk()
window.title('Magic 8 Game')
window.geometry("500x400")
window.configure(background='white')
window.resizable(False,False)


RESPONSES = [r"C:\\Users\\anagh\\Desktop\\Magic8Ball\\m1.png",
            r"C:\\Users\\anagh\\Desktop\\Magic8Ball\\m2.png",
            r"C:\\Users\\anagh\\Desktop\\Magic8Ball\\m3.png",
            r"C:\\Users\\anagh\\Desktop\\Magic8Ball\\m4.png",
             r"C:\\Users\\anagh\\Desktop\\Magic8Ball\\m5.png",
              r"C:\\Users\\anagh\\Desktop\\Magic8Ball\\m6.png",
               r"C:\\Users\\anagh\\Desktop\\Magic8Ball\\m7.png",
                r"C:\\Users\\anagh\\Desktop\\Magic8Ball\\m8.png",
                 r"C:\\Users\\anagh\\Desktop\\Magic8Ball\\m9.png",
                  r"C:\\Users\\anagh\\Desktop\\Magic8Ball\\m10.png",
                    r"C:\\Users\\anagh\\Desktop\\Magic8Ball\\m11.png",
                     r"C:\\Users\\anagh\\Desktop\\Magic8Ball\\m12.png",
                      r"C:\\Users\\anagh\\Desktop\\Magic8Ball\\m13.png",
                       r"C:\\Users\\anagh\\Desktop\\Magic8Ball\\m14.png",
                        r"C:\\Users\\anagh\\Desktop\\Magic8Ball\\m15.png",
                         r"C:\\Users\\anagh\\Desktop\\Magic8Ball\\m16.png",
                          r"C:\\Users\\anagh\\Desktop\\Magic8Ball\\m17.png",
                           r"C:\\Users\\anagh\\Desktop\\Magic8Ball\\m18.png",
                            r"C:\\Users\\anagh\\Desktop\\Magic8Ball\\m19.png",
                             r"C:\\Users\\anagh\\Desktop\\Magic8Ball\\m20.png"] 



def response():
    msg ="error :there must be a text value"
    i =questionstb.get()
    y =i.isdigit()
    l =len(i)

    if y== True or l ==0:
        #questionstb.insert(0,(msg))
        tkinter.messagebox.showwarning("Error","Please enter a question!")
    else:
        x= random.choice(RESPONSES) 
         
        imgupdate = PhotoImage(file =x)
        img1 =imgupdate.subsample(2,2)
        m8img.photo=img1
        m8img.configure(image=img1)
       
       
questionslb =Label(window, text ="Write your question below")
questionslb.place(x = 10, y = 10)
questionslb.pack()
#answerslb =Label(window, text ="Answers :")
#answerslb.place(x = 10, y = 30)
#answerslb.pack()

questionsVar =StringVar()
questionstb =Entry(window)
questionstb.place(x = 70, y = 10,width =400)
questionstb.pack()

#answersVar =StringVar()
#answerstb =Entry(window)
#answerstb.place(x = 70, y = 30 ,width =200)
#answerstb.pack()

responsebtn =Button(window ,text ="Response",command =response)
responsebtn.place(x = 10, y = 100)
responsebtn.pack()
#exitbtn =Button(window ,text ="Exit" ,command =exit)
#exitbtn.place(x = 100, y = 100)

#Add image
photo=PhotoImage(file= r"C:\Users\anagh\Desktop\Magic8Ball\mb.png")
photoimage = photo.subsample(2,2) 
m8img =Label(window, image=photoimage)
#m8img.place(anchor="center")
m8img.pack()


window.mainloop()