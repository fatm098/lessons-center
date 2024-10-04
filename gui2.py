#GUI2
#Login page
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

#Font  ...............
font=("arial",18,"bold")
fon=("arial",12,"bold")

#Root 2 ...............
root2=Tk()
root2.title("Login")

#Form dimensions ...............
w=500
h=730
screenwidth=root2.winfo_screenwidth()
screenhight=root2.winfo_screenheight()
x=int((screenwidth-w)/2)
y=int((screenhight-h)/2)
root2.geometry(f"{w}x{h}+{x}+{y}")
#root2.resizable('false','false')

#icon ...............
root2.iconbitmap('C:/Users/HP/Downloads/center project/icon/icon.ico')

#image ...............
img=PhotoImage(file="C:/Users/HP/Downloads/center project/photo/op21.png")

#image label ...............
img_lbl=tkinter.Label(root2,image=img)
img_lbl.pack()

#Frame 2 ...............
frame2=tkinter.Frame(root2,bg='white')
frame2.place(anchor='center',relx=.5,rely=.5)

#icon ...............
#root2.iconbitmap('C:/Users/DELL/Desktop/icon.ico')

#Back function...............
def back():
    root2.destroy()
    import gui1
    
#function of Login button ...............
def check_validation ():
   valid_user="koky"
   valid_password="0123"
   
   #check correctness of username and password ...............
   if email.get()==valid_user and password.get()==valid_password:
      root2.destroy()
      import gui3
  
   #incorrect email or password ...............
   else:
        messagebox.showerror('Error','Invalid information')



       
#E-mail ...............
lbl_email=tkinter.Label(frame2,text="E-mail    ",fg='#03045e',font=font,bg='white')
lbl_email.grid(column=0,row=0,padx=1,pady=30)
#lbl_email.place(x=0,y=25)
email=tkinter.Entry(frame2,width=25,font=fon)
email.grid(column=1,row=0,pady=30)
#email.place(x=10,y=25)

#Password ...............
lbl_password=tkinter.Label(frame2,text="Password",fg='#03045e',font=font,bg='white')
lbl_password.grid(column=0,row=1,padx=1,pady=30)
#lbl_password.place(x=0,y=50)
password=tkinter.Entry(frame2,show="*",width=25,font=fon)
password.grid(column=1,row=1,padx=15,pady=30)
#password.place(x=10,y=50)

#login Button ...............
login_btn=tkinter.Button(frame2,text="  Login  ",font=font,bg='#fb3640',fg='white',command=check_validation,height=1,width=10)
login_btn.grid(column=0,row=8,padx=20,pady=30,columnspan=3)


#back Button ...............
back_btn=tkinter.Button(root2,text=" Back ",font=fon,bg='#fb3640',fg='white',command=back,height=2,width=10)
#back_btn.grid(column=0,row=8,padx=50,pady=50)
back_btn.place(x=100,y=650)

root2.mainloop()
    





