#GUI4
#Teacher page
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
import teacher_database as db

#Font ...............
font=("arial",14,"bold")

#Root 4 ...............
root4 = Tk()
root4.title("Teacher Page")
root4['bg']='white'

#Form dimensions ...............
w = 915
h = 600
screenwidth=root4.winfo_screenwidth()
screenhight=root4.winfo_screenheight()
x=int((screenwidth-w)/2)
y=int((screenhight-h)/2)
root4.geometry(f"{w}x{h}+{x}+{y}")
root4.resizable('false','false')

#icon ...............
root4.iconbitmap('C:/Users/HP/Downloads/center project/icon/teacher.ico')

#Images ...............
img=PhotoImage(file="C:/Users/HP/Downloads/center project/photo/h.png")

#Image lablel ...............
#lbl=tkinter.Label(root4) 
lbl=tkinter.Label(root4,image=img) 

lbl.pack()


#Frame of Content ...............
frame4_con = tkinter.Frame(root4,bg='white')
frame4_con.place(x=10,y=150)

#Frame of Table ...............
frame4_tabel = tkinter.Frame(root4,bg='white')
frame4_tabel.place(x=450,y=150)

#Frame of Buttons ...............
frame4_btn = tkinter.Frame(root4,bg='white',padx=100)
frame4_btn.place(x=5,y=500)

#Gender Redio button ...............
rbtn4_var=StringVar()
rbtn4_var.set("Female")#Default value

#Teacher Table ...............
tr=Treeview(frame4_tabel,columns=("name","age","Phone number","id","gender","subject","salary"),show="headings",selectmode='browse',height=5  )
tr.heading("name",text="Name")
tr.heading("age", text= "Age")
tr.heading("Phone number", text= "Phone number")
tr.heading("id", text="ID")
tr.heading("gender", text= "Gender")
tr.heading("subject", text= "Subject")
tr.heading("salary", text= "Salary")

tr.column("name", width=60)
tr.column("age", width=40)
tr.column("Phone number", width=100)
tr.column("id", width=30)
tr.column("gender", width=70)
tr.column("subject", width=70)
tr.column("salary", width=70)


'''
scrollbar=Scrollbar(frame4_tabel,orient='vertical',command=tr.yview())
tr.configure(yscroll=Scrollbar.set)
scrollbar.grid(row=8,column=2,sticky='ns')

'''

#Teacher Name ...............
name_lbl = tkinter.Label(frame4_con,text="Name           ",bg='white',fg = "black",font=("Tahoma",15))
name_lbl.grid(row=0,column=0,pady=5)
name_entry =  tkinter.Entry(frame4_con,width=27)
name_entry.grid(row=0,column=1,pady=5)
 
#Teacher Age ...............
age_lbl = tkinter.Label(frame4_con,text="Age             ",bg='white',fg = "black",font=("Tahoma",15))
age_lbl.grid(row=1,column=0,pady=5)
age_entry =  tkinter.Entry(frame4_con,width=27)
age_entry.grid(row=1,column=1,pady=5)

#Teacher Phone ...............
phone_lbl =  tkinter.Label(frame4_con,text="    Phone number  ",bg='white',fg = "black",font=("Tahoma",15))
phone_lbl.grid(row=3,column=0,pady=5)
phone_entry =tkinter.Entry(frame4_con,width=27)
phone_entry.grid(row=3,column=1,pady=5)

#Teacher ID ...............
id_lbl =  tkinter.Label(frame4_con,text="ID             ",bg='white',fg = "black",font=("Tahoma",15))
id_lbl.grid(row=4,column=0,pady=5)
id_entry = Entry(frame4_con,width=27)
id_entry.grid(row=4,column=1,pady=5)

#Teacher Gender ...............
gender_lbl =  tkinter.Label(frame4_con,text=" Gender         ",bg='white',fg = "black",font=("Tahoma",15))
gender_lbl.grid(row = 5,column=0,pady=5)
#Female radio button ...............
rbtn1=tkinter.Radiobutton(frame4_con,text="Female",bg='white',value="Female",variable=rbtn4_var)
#rbtn1.grid(row=5,column=1,pady=5)
rbtn1.place(x=180,y=165)
#Male radio button ...............
rbtn2=tkinter.Radiobutton(frame4_con,text="Male",bg='white',value="Male",variable=rbtn4_var)
#rbtn2.grid(row=5,column=2,pady=5)
rbtn2.place(x=300.,y=165)

#Subject ...............
subject_lbl =  tkinter.Label(frame4_con,text="Subject       ",bg='white',fg = "black",font=("Tahoma",15))
subject_lbl.grid(row = 6,column=0,pady=5)
subjects=["Arabic","Science","English","Math","Histoty","geograohy"]
combo=Combobox(frame4_con,values=subjects,state="readonly",width=27)
combo.grid(row=6,column=1,pady=10)

#Teacher Salary ...............
salary_lbl = tkinter.Label(frame4_con,text="Salary       ",bg='white',fg = "black",font=("Tahoma",15))
salary_lbl.grid(row=7,column=0,pady=5)
salary_entry =  tkinter.Entry(frame4_con,width=30)
salary_entry.grid(row=7,column=1,pady=5)

#move to gui3   ...............
def back_fun():
      root4.destroy() 
      import gui3
      
#move to gui6 ...............
def search_fun():
    root4.destroy()   
    import gui6
  
def select_all():
    data=db.show_all_teacher()
    tr.delete(*tr.get_children())
    for i in data:
        tr.insert("",END,values=i)

def add():
    db.add_teacher(name_entry.get(),age_entry.get(),phone_entry.get(),id_entry.get(),rbtn4_var.get(),combo.get(),salary_entry.get())
    tr.insert("",END,values=(name_entry.get(),age_entry.get(),phone_entry.get(),id_entry.get(),rbtn4_var.get(),combo.get(),salary_entry.get()))

    name_entry.delete(0,END)
    age_entry.delete(0,END)
    phone_entry.delete(0,END)
    id_entry.delete(0,END)
    salary_entry.delete(0,END)
    rbtn4_var.set("Female")
    combo.set('')
def get_values(event):
    name_entry.delete(0,END)
    age_entry.delete(0,END)
    phone_entry.delete(0,END)
    id_entry.delete(0,END)
    salary_entry.delete(0,END)
    rbtn4_var.set("Female")
    combo.set('')
    
    selectitem=tr.selection()[0]
    
    name_entry.insert(0,tr.item(selectitem) ['values'][0])
    age_entry.insert(0,tr.item(selectitem) ['values'][1])
    phone_entry.insert(0,tr.item(selectitem) ['values'][2])
    id_entry.insert(0,tr.item(selectitem) ['values'][3])
    rbtn4_var.set(tr.item(selectitem) ['values'][4])
    combo.set(tr.item(selectitem) ['values'][5])
    salary_entry.insert(0,tr.item(selectitem) ['values'][6])

def  update():
    db.update_teacher(name_entry.get(), age_entry.get(), phone_entry.get(), id_entry.get(), rbtn4_var.get(), combo.get(),salary_entry.get())
    select_all()

def delete():
    db.delete_teacher(id_entry.get())
    show_all_teacher()

#Back button ...............
back_btn= tkinter.Button(frame4_btn,text="Back",fg="white",relief='flat',bg="#ff595e",font=("Tahoma",15),width=10,command=back_fun)
back_btn.grid(row=7,column=0,padx=7,pady=2)

#Add button ...............
add_btn= tkinter.Button(frame4_btn,text="Add",fg="white",command=add,relief='flat',bg="#ff595e",font=("Tahoma",15),width=10)
add_btn.grid(row=7,column=1,padx=7,pady=2)

#Delete button ...............
delete_btn= tkinter.Button(frame4_btn,text="Delete",fg="white",command=delete,relief='flat',bg="#ff595e",font=("Tahoma",15),width=10)
delete_btn.grid(row=7,column=2,padx=7,pady=2)

#Update button ...............
update_btn= tkinter.Button(frame4_btn,text="Update",fg="white",relief='flat',command=update,bg="#ff595e",font=("Tahoma",15),width=10)
update_btn.grid(row=7,column=3,padx=7,pady=2)

#Search button ...............
search_btn=tkinter.Button(frame4_btn,text="Search",fg="white",relief='flat',bg="#ff595e",font=("Tahoma",15),command=search_fun,width=10)
search_btn.grid(row=7,column=4,padx=7,pady=2)

#select all button ...............
select_btn= tkinter.Button(frame4_btn,text="Select all",fg="white",command=select_all,relief='flat',bg="#ff595e",font=("Tahoma",15),width=10)
select_btn.grid(row=7,column=5,padx=7,pady=2)

tr.grid(row=8,column=0)
tr.bind("<<TreeviewSelect>>",get_values)
root4.mainloop()