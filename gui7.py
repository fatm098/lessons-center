#GUI7
#Student Search Gui
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
import  students as db

#font ...............
font=("arial",24,"bold")
font1=("arial",8,"bold")

#root 7 ...............
root7 = Tk()
root7.title("Student Search")
root7.resizable('false','false')

#icon ...............
root7.iconbitmap('C:/Users/HP/Downloads/center project/icon/search.ico')

#images ...............
img=PhotoImage(file="C:/Users/HP/Downloads/center project/photo/jk.png")

#image lablel ...............
#image_lbl = tkinter.Label(root7,text="Welcome to our ",background='white') 
image_lbl = tkinter.Label(root7,text="Welcome to our ",background='white',image=img) 

image_lbl.pack()

#Form dimensions ...............
w=540
h=625
screenwidth=root7.winfo_screenwidth()
screenhight=root7.winfo_screenheight()
x=int((screenwidth-w)/2)
y=int((screenhight-h)/2)
root7.geometry(f"{w}x{h}+{x}+{y}")

'''
#frame6
frame6_tabel=tkinter.Frame(root8,bg='white')
frame6_tabel.place(x=150,y=100)
'''

#frame content ...............
frame7_con = tkinter.Frame(root7,bg='white')
frame7_con.place(x=150,y=150)#x=50,y=200

#label of id ...............
id_lbl=tkinter.Label(frame7_con,text=" Enter ID ",bg='white',fg='black',font=font)#lbl.grid(row=1,column=1)
id_lbl.grid(row = 1,column=0,padx=5,pady=5) 

#enter id ...............
id_entry=tkinter.Entry(frame7_con,width=35)
#id_entry.place(x=50,y=20)
id_entry.grid(row = 5,column=0,padx=10,pady=10)

#search function ...............
def search_fun():
    
   
    data= db.search_student(id_entry.get())
    tr.delete(*tr.get_children())
    for i in data:
        tr.insert("",END,values=i)
    db.show_all_students()


#Back function ...............
#move to gui4 ...............
def back_fun():
    root7.destroy()
    import gui3
    
#search button
search_btn=tkinter.Button(frame7_con,text="Search",bg='#00a6fb',fg='black',font=font1,height=2,width=15,command=search_fun)
#back_btn.place(x=100,y=100)  
search_btn.grid(row=6,column=0)

#d62828
##4895ef 
#ffc6ff

#Back button
back_btn=tkinter.Button(root7,text="Back",bg='#00a6fb',height=1,width=10,command=back_fun)
back_btn.place(x=100,y=530)
               
#Frame Table
frame7_tabel = tkinter.Frame(root7,bg='white')
frame7_tabel.place(x=95,y=300)

#Show Tabel
tr=Treeview(frame7_tabel,columns=("id","name","age","acadimic year","gender","subject"),show="headings")
tr.heading("id", text="ID")
tr.heading("name",text="Name")
tr.heading("age", text= "Age")
tr.heading("acadimic year", text= "Acadimic Year")
tr.heading("gender", text= "Gender")
tr.heading("subject", text= "Subject")

tr.column("id", width=40)
tr.column("name", width=70)
tr.column("age", width=50)
tr.column("acadimic year", width=90)
tr.column("gender", width=70)
tr.column("subject", width=70)
tr.grid(row=8,column=0)

root7.mainloop()

'''

'''