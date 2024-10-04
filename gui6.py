#GUI6
#Teacher Search Gui
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
import teacher_database as db

#font ...............
font=("arial",24,"bold")
font1=("arial",8,"bold")

#root 6 ...............
root6 = Tk()
root6.title("Teacher Search")
root6.resizable('false','false')

#icon ...............
root6.iconbitmap('C:/Users/HP/Downloads/center project/icon/search.ico')

#images ...............
img=PhotoImage(file="C:/Users/HP/Downloads/center project/photo/jk.png")

#image lablel ...............
#image_lbl = tkinter.Label(root6,text="Welcome to our ",background='white')
image_lbl = tkinter.Label(root6,text="Welcome to our ",background='white',image=img) 
 
image_lbl.pack()

#Form dimensions ...............
w=540
h=625
screenwidth=root6.winfo_screenwidth()
screenhight=root6.winfo_screenheight()
x=int((screenwidth-w)/2)
y=int((screenhight-h)/2)
root6.geometry(f"{w}x{h}+{x}+{y}")

'''
#frame6
frame6_tabel=tkinter.Frame(root8,bg='white')
frame6_tabel.place(x=150,y=100)
'''

#frame content ...............
frame6_con = tkinter.Frame(root6,bg='white')
frame6_con.place(x=150,y=150)#x=50,y=200

#label of id ...............
id_lbl=tkinter.Label(frame6_con,text=" Enter ID ",bg='white',fg='black',font=font)#lbl.grid(row=1,column=1)
id_lbl.grid(row = 1,column=0,padx=5,pady=5) 

#enter id ...............
id_entry=tkinter.Entry(frame6_con,width=35)
#id_entry.place(x=50,y=20)
id_entry.grid(row = 5,column=0,padx=10,pady=10)

#search function ...............
def search_fun():
     
    data= db.search_teacher(id_entry.get())
    tr.delete(*tr.get_children())
    for i in data:
        tr.insert("",END,values=i)


    

#Back function ...............
#move to gui4 ...............
def back_fun():
    root6.destroy()
    import gui3
    
#search button
search_btn=tkinter.Button(frame6_con,text="Search",bg='#00a6fb',fg='black',font=font1,height=2,width=15,command=search_fun)
#back_btn.place(x=100,y=100)  
search_btn.grid(row=6,column=0)

#d62828
##4895ef 
#ffc6ff

#Back button
back_btn=tkinter.Button(root6,text="Back",bg='#00a6fb',height=1,width=10,command=back_fun)
back_btn.place(x=100,y=530)
               
#Frame Table
frame6_tabel = tkinter.Frame(root6,bg='white')
frame6_tabel.place(x=95,y=300)

#Show Tabel
#name   age   phone  id  gender subject  salary
tr=Treeview(frame6_tabel,columns=("name","age","Phone number","id","gender","subject","salary"),show="headings")
tr.heading("id", text="ID")
tr.heading("name",text="Name")
tr.heading("age", text= "Age")
tr.heading("Phone number", text= "Phone number")
tr.heading("gender", text= "Gender")
tr.heading("subject", text= "Subject")
tr.heading("salary", text= "Salary")

tr.column("id", width=35)
tr.column("name", width=65)
tr.column("age", width=45)
tr.column("Phone number", width=90)
tr.column("gender", width=55)
tr.column("subject", width=55)
tr.column("salary", width=45)

tr.grid(row=8,column=0)

root6.mainloop()

'''

'''