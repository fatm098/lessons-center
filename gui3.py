#GUI3
#selection page
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

#Font ...............
font=("arial",14,"bold")

#Root 3 ...............
root3=Tk()
root3.title("Center page")

#Form dimensions ...............
w=500
h=700
screenwidth=root3.winfo_screenwidth()
screenhight=root3.winfo_screenheight()
x=int((screenwidth-w)/2)
y=int((screenhight-h)/2)
root3.geometry(f'{w}x{h}+{x}+{y}' )
root3['bg']='#ecebe4'
root3.resizable('false','false')

#icon ...............
root3.iconbitmap('C:/Users/HP/Downloads/center project/icon/images-_1_.ico')
#image ...............
img=PhotoImage(file="C:/Users/HP/Downloads/center project/photo/ch (1).png")

#image label ...............
#img_lbl=tkinter.Label(root3)
img_lbl=tkinter.Label(root3,image=img)
img_lbl.grid()

#frame 3 ...............
frame3=tkinter.Frame(root3,bg='white')
frame3.place(anchor="center",relx=0.5,rely=0.5)
    
#move to gui4 (Teacher page) ...............
def teacher_():
    root3.destroy()
    import gui4

#move to gui5 (Student page) ...............
def student_():
    root3.destroy()
    import gui5
    
#Teacher button ...............
teacher_btn1=tkinter.Button(frame3,text="Teacher ",font=font,bg='#e7bb41',fg='#6f1d1b',height=2,command=teacher_,width=25)
teacher_btn1.grid(column=0,row=1,padx=10,pady=10)

#Student button ...............
student_btn2=tkinter.Button(frame3,text="student ",height=2,font=font,fg='#6f1d1b',bg='#e7bb41',command=student_,width=25)
student_btn2.grid(column=0,row=3,padx=5,pady=5)

#move to gui2  ...............
def back():
      root3.destroy()
      import gui2
      
#back button ..................
back_btn=tkinter.Button(root3,text="  Back  ",command=back,width=10,height=2,font=font,bg='#6f1d1b',fg='white')
back_btn.place(x=300,y=550)
     
root3.mainloop()