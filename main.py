from tkinter import *
from tkinter import ttk, messagebox
from db import Database

db = Database("employee.db")


root = Tk()
root.geometry("1310x510+0+0")
root.title("Emplyee Management System")
root.resizable(False,False)
root.config(bg="#011426")


name1 = StringVar()
age1 = StringVar()
job1 = StringVar()
gender1 = StringVar()
email1 = StringVar()
phone1 = StringVar()



######__Entries Frame__######
entry_frame = Frame(root,bg="#011426").place(x=1, y=1, width=360, height=510)
title = Label(entry_frame, text="Company Employees", font="calibri 18 bold" ,bg="#011426", fg="white")
title.place(x=10, y=1)

name = Label(entry_frame, text="Name",bg="#011426",fg="white", font="calibri 16").place(x=10, y=50)
txtName= Entry(entry_frame, width=20, font="calibri 16", textvariable=name1)
txtName.place(x=120, y=50)

job = Label(entry_frame, text="Job",bg="#011426",fg="white", font="calibri 16").place(x=10, y=90)
txtjob= Entry(entry_frame, width=20, font="calibri 16",textvariable=job1)
txtjob.place(x=120, y=90)

gender = Label(entry_frame, text="Gender",bg="#011426",fg="white", font="calibri 16").place(x=10, y=130)
combogender = ttk.Combobox(entry_frame, width=18, state="readonly" ,font="calibri 16",textvariable=gender1)
combogender['values'] = ('Male', 'Female')
combogender.place(x=120, y=130)

age = Label(entry_frame, text="Age",bg="#011426",fg="white", font="calibri 16").place(x=10, y=170)
txtage= Entry(entry_frame, width=20, font="calibri 16",textvariable=age1)
txtage.place(x=120, y=170)

email = Label(entry_frame, text="Email",bg="#011426",fg="white", font="calibri 16").place(x=10, y=210)
txtEmail= Entry(entry_frame, width=20, font="calibri 16",textvariable=email1)
txtEmail.place(x=120, y=210)

phone = Label(entry_frame, text="Phone",bg="#011426",fg="white", font="calibri 16").place(x=10, y=250)
txtphone= Entry(entry_frame, width=20, font="calibri 16", textvariable=phone1)
txtphone.place(x=120, y=250)

add = Label(entry_frame, text="Address",bg="#011426",fg="white", font="calibri 16").place(x=10, y=290)
txtadd = Text(entry_frame, width=30, height=2, font="calibri 16")
txtadd.place(x=10, y=330)


#===========_Fun_==========#
def hide():
    root.geometry("360x510")
def show():
    root.geometry("1310x510")

btn_hide = Button(entry_frame, text="Hide", cursor="hand2", bg="#e63946", fg='white', bd=1, relief=SOLID, command=hide).place(x=270, y=4)
btn_show = Button(entry_frame, text="Show", cursor="hand2", bg="#e63946",fg='white', bd=1, relief=SOLID, command=show).place(x=320, y=4)


def getData(e):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data['values']
    name1.set(row[1])
    age1.set(row[2])
    job1.set(row[3])
    email1.set(row[4])
    gender1.set(row[5])
    phone1.set(row[6])
    txtadd.delete(1.0, END)
    txtadd.insert(END, row[7])

def DisplayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END, values=row)

def delete():
   db.remove(row[0])
   clear()
   DisplayAll()

def clear():
    name1.set("")
    age1.set("")
    job1.set("")
    gender1.set("")
    email1.set("")
    phone1.set("")
    txtadd.delete(1.0, END)

def add_emp():
    if txtName.get() == " " and txtage.get() == " " and txtjob.get() == " " and combogender.get() == " " and txtEmail.get() == " " and txtphone.get() == " " and txtadd.get(1.0, END) == " ":
        messagebox.showerror("Error", "Please Fill All The Entry")
        return
    db.insert(
        txtName.get(),
        txtage.get(),
        txtjob.get(),
        txtEmail.get(),
        combogender.get(),
        txtphone.get(),
        txtadd.get(1.0, END))
    messagebox.showinfo("success", "Employee Added successfully")
    clear()
    DisplayAll()

def update():
    if txtName.get() == " " and txtage.get() == " " and txtjob.get() == " " and combogender.get() == " " and txtEmail.get() == " " and txtphone.get() == " " and txtadd.get(1.0, END) == " ":
        messagebox.showerror("Error", "Please Fill All The Entry")
        return
    db.update(
        row[0],
        txtName.get(),
        txtage.get(),
        txtjob.get(),
        txtEmail.get(),
        combogender.get(),
        txtphone.get(),
        txtadd.get(1.0, END))
    messagebox.showinfo("success", "UpDated successfully")
    clear()
    DisplayAll()
#========= Button Frame ==========#

#btn_frame = Frame(entry_frame, bg="white", relief=SOLID, bd=1).place(x=10, y=400, width=335, height=100)
btn_Add = Button(entry_frame, text="Add Employee", width=14, height=1, font="calibri 16", fg="white", bg="#e63946", bd=0, command=add_emp)
btn_Add.place(x=4, y=400)

btn_update = Button(entry_frame, text="UpDate", width=14, height=1, font="calibri 16", fg="white", bg="#e63946", bd=0, command=update)
btn_update.place(x=180, y=400)

btn_del = Button(entry_frame, text="Delete", width=14, height=1, font="calibri 16", fg="white", bg="#e63946", bd=0, command=delete)
btn_del.place(x=4, y=450)

btn_clear = Button(entry_frame, text="Clear All", width=14, height=1, font="calibri 16", fg="white", bg="#e63946", bd=0,command=clear)
btn_clear.place(x=180, y=450)

#========= Table Frame ==========#
table_frame = Frame(root,bg="white").place(x=406, y=1, width=950, height=510)
style = ttk.Style()
style.configure("mystyle.Treeview", font="calibri 13", rowheight =50)
style.configure("mystyle.Treeview.Heading", font="calibri 13")

tv = ttk.Treeview(table_frame, columns=(1,2,3,4,5,6,7,8))


#tv.column('#0', width=0, stretch=NO)

tv.heading(1, text="ID",anchor="center")
tv.column(1, width="50",anchor="center")

tv.heading(2, text="Name",anchor="center")
tv.column(2, width="140",anchor="center")

tv.heading(3, text="Age",anchor="center")
tv.column(3, width="50",anchor="center")

tv.heading(4, text="Job",anchor="center")
tv.column(4, width="120",anchor="center")

tv.heading(5, text="Email",anchor="center")
tv.column(5, width="150",anchor="center")

tv.heading(6, text="Gender",anchor="center")
tv.column(6, width="90",anchor="center")

tv.heading(7, text="Phone",anchor="center")
tv.column(7, width="150",anchor="center")

tv.heading(8, text="Address",anchor="center")
tv.column(8, width="190",anchor="center")

tv['show'] = 'headings'

tv.bind("<ButtonRelease-1>", getData)
#tv.pack(side=RIGHT,padx=0,pady=0)
tv.place(x=395, y=1, height=510, width=950)

DisplayAll()

root.mainloop()