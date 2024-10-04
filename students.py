# the module of database student named(students)

import sqlite3
db=sqlite3.connect("center.db")
cr=db.cursor()
cr.execute("create table if not exists students(id integer primary key autoincrement not null,name text not null,age integer not null,semester text not null,gender text ,subjects text not null )")
db.commit()
db.close()    




"""def teacher_data():
    db=sqlite3.connect("center.db")
    cr=db.cursor()
    cr.execute("create table if not exists teachers(name text not null,age integer,subject text not null,salary real,id integer primary key,gender text,number integer not null )")
    db.commit()
    db.close()"""
    


def add_student(id,name,age,semester,gender,subjects):
    db=sqlite3.connect("center.db")
    cr=db.cursor()
    cr.execute("insert into students values(?,?,?,?,?,?)",(id,name,age,semester,gender,subjects))
    db.commit()
    db.close()


def show_all_students():
    db=sqlite3.connect("center.db")
    cr=db.cursor()
    data=cr.execute("select * from students")
    db.commit()
    return data
def delete_student(id):
    db=sqlite3.connect("center.db")
    cr=db.cursor()
    cr.execute(f"delete from students where id ={id}")
    db.commit()
    db.close()

def update_student(id,name,age,semester,gender,subjects):
    db=sqlite3.connect("center.db")
    cr=db.cursor()
    cr.execute("update students set name=?,age=?,semester=?,gender=?,subjects=? where id=?",(name,age,semester,gender,subjects,id))
    db.commit()
    db.close()
    
def search_student(id):
    db=sqlite3.connect("center.db")
    cr=db.cursor()
    data=cr.execute(f"select * from students where id={id}")
    return data
    db.commit()