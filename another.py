from tkinter import * 
import sqlite3
rt=Tk()

rt.geometry("500x200")
rt.title("heekk")

def submit():
	# connet database 
	con=sqlite3.connect("hello.db")
	curs=con.cursor()
##	curs.execute("create table moha1 (ID int,NAME text)")
	curs.execute("insert into moha1 values(:id_entry, :name_entry)",{'id_entry':id_entry.get(),'name_entry':name_entry.get()})
	con.commit()
	con.close()
	id_entry.delete(0,END)
	name_entry.delete(0,END)

def show_quary():
	con2=sqlite3.connect("hello.db")
	curs=con2.cursor()
	curs.execute("select *, oid from moha1")
	records=curs.fetchall()
	print(records)
	
	print_records=''
	for record in records:
		print_records += str(record) + "\n" 
	qurr=Label(rt,text=print_records)
	qurr.grid(row=6,column=2)
	con2.commit()
	con2.close()


def delete_quary():
	con2=sqlite3.connect("hello.db")
	curs=con2.cursor()
	curs.execute("select *, oid from moha1 ")
	con2.commit()
	con2.close()



id_label=Label(rt,text="Please Enter Your ID:",font=20)
id_label.grid(row=1,column=1,padx=5,pady=5)
id_entry=Entry(rt,font=20,width=30)
id_entry.grid(row=1,column=2,columnspan=2,padx=5,pady=5)

name_label=Label(rt,text="Please Enter Your Name:",font=20)
name_label.grid(row=2,column=1,padx=5,pady=5)
name_entry=Entry(rt,font=20,width=30)
name_entry.grid(row=2,column=2,columnspan=2,padx=5,pady=5)

# tell_label=Label(rt,text="Please Enter Your Tell:",font=20)
# tell_label.grid(row=3,column=1)
# tell_entry=Entry(rt,font=20,width=30)
# tell_entry.grid(row=3,column=2,columnspan=2)


submit_btn=Button(rt,text="Enter Record",font=30,width=12,command=submit)
submit_btn.grid(row=4,column=1,columnspan=4,pady=10,padx=10, ipadx=100)

show=Button(rt,text="Show quary",font=30,width=12,command=show_quary)
show.grid(row=5,column=1,columnspan=4,padx=10,pady=10,ipadx=100)

show=Button(rt,text="delete records",font=30,width=12,command=delete_quary)
show.grid(row=6,column=1,columnspan=4,padx=10,pady=10,ipadx=100)

rt.mainloop()
