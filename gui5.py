#GUI5
#Student page
#...............

from tkinter import *
from tkinter.ttk import Combobox,Treeview
import tkinter
from tkinter import messagebox
from tkinter import Image, PhotoImage
from tkinter.font import Font
from tkinter.ttk import *
from types import FrameType
import webbrowser
from tkinter import PhotoImage
import  students as db

#font ...............
font=("arial",14,"bold")

#Root 5 ...............
root5 = Tk()
root5.title("Student Page")
root5.resizable('false','false')
root5['bg']='white'

#Form dimensions ...............
w=899
h=650
screenwidth=root5.winfo_screenwidth()
screenhight=root5.winfo_screenheight()
x=int((screenwidth-w)/2)
y=int((screenhight-h)/2)
root5.geometry(f"{w}x{h}+{x}+{y}")

#icon ...............
root5.iconbitmap('C:/Users/HP/Downloads/center project/icon/student.ico')

#images ...............
img=PhotoImage(file="C:/Users/HP/Downloads/center project/photo/kk.png")

#Image lablel ...............
#image_lbl= tkinter.Label(root5)
image_lbl= tkinter.Label(root5,image=img)
 
image_lbl.pack()

#Frame of content ...............
frame_con = tkinter.Frame(root5,bg='white')
frame_con.place(x=10,y=200)

#Frame of Table ...............
frame_tabel = tkinter.Frame(root5,bg='white')
frame_tabel.place(x=450,y=200)

#Frame of Buttons ...............
frame_btn = tkinter.Frame(root5,bg='white')
frame_btn.place(x=10,y=500)

#Gender radio button ...............
rbtn_var=StringVar()
rbtn_var.set("Female")#Default value

#Student Table ...............
tr=Treeview(frame_tabel,columns=("id","name","age","acadimic year","gender","subject"),show="headings",selectmode='browse')
tr.heading("id", text="ID")
tr.heading("name",text="Name")
tr.heading("age", text= "Age")
tr.heading("acadimic year", text= "Acadimic Year")
tr.heading("gender", text= "Gender")
tr.heading("subject", text= "Subject")

tr.column("id", width=30)
tr.column("name", width=80)
tr.column("age", width=40)
tr.column("acadimic year", width=100)
tr.column("gender", width=80)
tr.column("subject", width=80)


#Student name ...............
name_lbl = tkinter.Label(frame_con,text=" Name          ",bg='white',fg = "black",font=("Tahoma",15))
name_lbl.grid(row=0,column=0,pady=5)
name_entry =  tkinter.Entry(frame_con,width=27)
name_entry.grid(row=0,column=1,pady=5)
 
#Student Age ...............
age_lbl = tkinter.Label(frame_con,text="Age           ",bg='white',fg = "black",font=("Tahoma",15))
age_lbl.grid(row=1,column=0,pady=5)
age_entry =  tkinter.Entry(frame_con,width=27)
age_entry.grid(row=1,column=1,pady=5)

#Acadimic year ...............
acadimic_year_lbl =  tkinter.Label(frame_con,text="     Acadimic year ",bg='white',fg = "black",font=("Tahoma",15))
acadimic_year_lbl.grid(row=3,column=0,pady=5)
acadimic_year_entry =  tkinter.Entry(frame_con,width=27)
acadimic_year_entry.grid(row=3,column=1,pady=5)

#Student ID ...............
id_lbl =  tkinter.Label(frame_con,text="ID          ",bg='white',fg = "black",font=("Tahoma",15))
id_lbl.grid(row=4,column=0,pady=5)
id_entry = Entry(frame_con,width=27)
id_entry.grid(row=4,column=1,pady=5)

#Student Gender ...............
gender_lbl =  tkinter.Label(frame_con,text="Gender      ",bg='white',fg = "black",font=("Tahoma",15))
gender_lbl.grid(row = 5,column=0,pady=5)
#Female radio button ...............
rbtn1=tkinter.Radiobutton(frame_con,text="Female",bg='white',value="Female",variable=rbtn_var)
rbtn1.place(x=175,y=165)
#rbtn1.grid(row=5,column=1,pady=5)
#Male radio button ...............
rbtn2=tkinter.Radiobutton(frame_con,text="Male",bg='white',value="Male",variable=rbtn_var)
rbtn2.place(x=280,y=165)
#rbtn2.grid(row=5,column=2,pady=5)

#Subject ...............
subject_lbl =  tkinter.Label(frame_con,text="Subject     ",bg='white',fg = "black",font=("Tahoma",15))
subject_lbl.grid(row = 6,column=0,pady=5)
subjects=["Arabic","Science","English","Math","date","geograohy"]
combo=Combobox(frame_con,values=subjects,state="readonly",width=27)
combo.grid(row=6,column=1,pady=10)

#move to gui3  ...............
def back_fun():
      root5.destroy()
      import gui3
      
#move to gui6 ...............
def search_fun():
    root5.destroy()
    import gui7
    
def add():
    db.add_student(id_entry.get(),name_entry.get(),age_entry.get(),acadimic_year_entry.get(),rbtn_var.get(),combo.get())
    tr.insert("",END,values=(id_entry.get(),name_entry.get(),age_entry.get(),acadimic_year_entry.get(),rbtn_var.get(),combo.get()))

    id_entry.delete(0,END)
    name_entry.delete(0,END)
    age_entry.delete(0,END)
    acadimic_year_entry.delete(0,END)
    rbtn_var.set("Female")
    combo.set('')
    
def get_values(event):
    id_entry.delete(0,END)
    name_entry.delete(0,END)
    age_entry.delete(0,END)
    acadimic_year_entry.delete(0,END)
    rbtn_var.set("Female")
    combo.set('')
    
    
    
    selectitem=tr.selection()[0]
   # select=tr.set(row_id)
    id_entry.insert(0,tr.item(selectitem) ['values'][0])
    name_entry.insert(0,tr.item(selectitem) ['values'][1] )
    age_entry.insert(0, tr.item(selectitem) ['values'][2])
    acadimic_year_entry.insert(0,tr.item(selectitem) ['values'][3] )
    rbtn_var.set(tr.item(selectitem) ['values'][4])
    combo.set( tr.item(selectitem) ['values'][5])


def show_all():
     data=db.show_all_students()
     tr.delete(*tr.get_children())
     for i in data:
         tr.insert("",END,values=i)

   
def update():
    db.update_student(id_entry.get(),name_entry.get(),age_entry.get(),acadimic_year_entry.get(),rbtn_var.get(),combo.get())  
    show_all()
    
    
def delete():
    db.delete_student(id_entry.get())
    db.show_all_students()

def close():
    root5.destroy()

#Back button  ...............
back_btn= tkinter.Button(frame_btn,text="Back",fg="white",relief='flat',bg="#ff595e",font=("Tahoma",15),width=8,command=back_fun)
back_btn.grid(row=7,column=0,padx=7,pady=2)

#Add button ...............
add_btn= tkinter.Button(frame_btn,text="Add",command=add,fg="white",relief='flat',bg="#ff595e",font=("Tahoma",15),width=8)
add_btn.grid(row=7,column=1,padx=7,pady=2)

#Delete button ...............
delete_btn= tkinter.Button(frame_btn,text="Delete",command=delete,fg="white",relief='flat',bg="#ff595e",font=("Tahoma",15),width=8)
delete_btn.grid(row=7,column=2,padx=7,pady=2)

#Update button ...............
update_btn= tkinter.Button(frame_btn,text="Update",command=update,fg="white",relief='flat',bg="#ff595e",font=("Tahoma",15),width=8)
update_btn.grid(row=7,column=3,padx=7,pady=2)

#Search button ...............
search_btn= tkinter.Button(frame_btn,text="Search",command=search_fun,fg="white",relief='flat',bg="#ff595e",font=("Tahoma",15),width=8)
search_btn.grid(row=7,column=4,padx=7,pady=2)

#select all button ...............
select_btn= tkinter.Button(frame_btn,text="Select all",command=show_all,fg="white",relief='flat',bg="#ff595e",font=("Tahoma",15),width=8)
select_btn.grid(row=7,column=5,padx=7,pady=2)

tr.grid(row=8,column=0)
tr.bind("<<TreeviewSelect>>",get_values)

root5.mainloop()