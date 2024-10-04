# the module of database teacher named(teacher_database)
import sqlite3
db=sqlite3.connect("center.db")
cr=db.cursor()
cr.execute("create table if not exists teachers(name text not null,age integer,phone_numder integer not null,id integer primary key,gender text,subject text not null,salary integer not null)")
 

'''
cr.execute("ALTER TABLE teachers ADD )
db.commit()
db.close()  
'''


    


def add_teacher(name,age,phone_numder,id,gender,subject,salary):
    db=sqlite3.connect("center.db")
    cr=db.cursor()
    cr.execute("insert into teachers values(?,?,?,?,?,?,?)",(name,age,phone_numder,id,gender,subject,salary))
    db.commit()
    db.close()


def show_all_teacher():
    db=sqlite3.connect("center.db")
    cr=db.cursor()
    data=cr.execute("select * from teachers")
    db.commit()
    return data
def delete_teacher(id):
    db=sqlite3.connect("center.db")
    cr=db.cursor()
    cr.execute(f"delete from teachers where id ={id}")
    db.commit()
    db.close()

def update_teacher(name,age,phone_numder,id,gender,subject,salary):
    db=sqlite3.connect("center.db")
    cr=db.cursor()
    cr.execute("update teachers set name=?,age=?,phone_numder=?,gender=?,subject=?,salary=? where id=?",(name,age,phone_numder,gender,subject,salary,id))
    db.commit()
    db.close()
    
def search_teacher(id):
    db=sqlite3.connect("center.db")
    cr=db.cursor()
    data=cr.execute(f"select * from teachers where id={id}")
    return data
    db.commit()
    db.close()