#GUI1
#Welcome page
#...............
    
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import Image, PhotoImage
from tkinter.font import Font
from tkinter.ttk import *
from types import FrameType
import webbrowser
from tkinter import PhotoImage

#font ...............
font=("arial",14,"bold")

#root1 ...............
root1 =Tk()
root1.title("Welcome page")
root1['bg']='white'

#Form dimensions ...............
w=520
h=670
screenwidth=root1.winfo_screenwidth()
screenhight=root1.winfo_screenheight()
x=int((screenwidth-w)/2)
y=int((screenhight-h)/2)
root1.geometry(f"{w}x{h}+{x}+{y}")
root1.resizable('false','false')

#icon ...............
root1.iconbitmap('C:/Users/HP/Downloads/center project/icon/welcomeicon.ico')

#images ...............
img=PhotoImage(file="C:/Users/HP/Downloads/center project/photo/op15.png")

#Frame 1 ...............
frame = tkinter.Frame(root1)
frame.place(anchor="center",relx=0.5,rely=0.5)

#Image lablel ...............
#lbl = tkinter.Label(frame,text="Welcome to our center ",background='white') 
lbl = tkinter.Label(frame,text="Welcome to our center ",background='white',image=img) 

#lbl.image=img
lbl.pack()

#move to gui2 ...............
def Next():     
    root1.destroy()
    import gui2

#next button ...............
btn = tkinter.Button(root1,text="Next",command=Next,fg="#fdfffc",bg="#1d3557",font=("Tahoma",14,'bold'),width=12,relief='flat') 
btn.pack(side= "top")

root1.mainloop()