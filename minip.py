import random
import string
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

top = Tk()
top.title("CAPTCHA")
top.state('zoomed')

bimg = ImageTk.PhotoImage(Image.open('bgi.jpeg'))
bg = Label(top, image=bimg)
bg.place(x=0, y=0)

captcha_text = ""
capi = None  # Global variable to hold the Label widget

# Generate text captcha
def cap():
    global captcha_text
    letterset = string.ascii_lowercase + string.ascii_uppercase
    captcha_text = "".join(random.choice(letterset) for i in range(5))

def capshow():
    from captcha.image import ImageCaptcha
    image = ImageCaptcha(width=280, height=90)
    image.generate(captcha_text)
    image.write(captcha_text, 'CAPTCHA.png')
    img = ImageTk.PhotoImage(Image.open("CAPTCHA.png"))
    
    global capi
    if capi:
        # Update the existing Label with the new image
        capi.configure(image=img)
        capi.image = img
    else:
        # Create a new Label for the first time
        capi = Label(image=img)
        capi.pack(pady=30)

cap()
capshow()

l = Label(text="ENTER THE CAPTCHA", bg='black')
l.pack(pady=10)

userip = StringVar()
userentry = Entry(textvariable=userip, bg='black')
userentry.pack()

import tkinter.messagebox as tmsg

def getval():
    if userip.get() == captcha_text:
        tmsg.showinfo('OK', "USER VERIFIED")
    else:
        tmsg.showerror("NO", "WRONG CAPTCHA, Please retry")
        cap()  # Call cap() to generate a new captcha_text
        capshow()  # Call capshow() to generate and display a new captcha image

b1 = Button(top, text="SUBMIT", command=getval, bg='black', fg='red', borderwidth=0)
b1.pack(pady=20)

top.mainloop()
