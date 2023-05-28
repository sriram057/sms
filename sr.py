from tkinter import *
import time
import ttkthemes
from tkinter import ttk
import pymysql
from tkinter import messagebox
from tkinter import filedialog
import pandas

#functions

def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()
    newlist=[]
    for index in indexing:
        content=studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)


    table=pandas.DataFrame(newlist,columns=['Id','Name','Mobile','Email','Address','Gender','DOB','Added Date','Added Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is saved succesfully')






def update_student():
    def update_data():
        currentdate = time.strftime('%d/%m/%y')
        currenttime = time.strftime('%H:%M:%S')
        query = 'update student set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(query, (nameEntry.get(), phoneEntry.get(), emailEntry.get(), addressEntry.get(),
                                 genderEntry.get(), dobEntry.get(), currentdate, currenttime, idEntry.get()))
        con.commit()
        messagebox.showinfo('Success', f'Id {idEntry.get()} is modified successfully', parent=update_window)
        update_window.destroy()
        show_student()



    update_window = Toplevel()
    update_window.title('search student')
    update_window.grab_set()
    update_window.resizable(False, False)
    idLabel = Label(update_window, text='Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(update_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(update_window, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(update_window, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(update_window, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    dobLabel = Label(update_window, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=5, column=1, pady=15, padx=10)

    genderLabel = Label(update_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=6, column=1, pady=15, padx=10)


    search_student_button = ttk.Button(update_window, text='update',command=update_data)
    search_student_button.grid(row=7, columnspan=2, pady=15)

    indexing = studentTable.focus()

    content = studentTable.item(indexing)
    listdata = content['values']
    idEntry.insert(0, listdata[0])
    nameEntry.insert(0, listdata[1])
    phoneEntry.insert(0, listdata[2])
    emailEntry.insert(0, listdata[3])
    addressEntry.insert(0, listdata[4])
    genderEntry.insert(0, listdata[5])
    dobEntry.insert(0, listdata[6])


def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)

def delete_student():
    indexing=studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    content_id=content['values'][0]
    query='delete from student where id =%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'Id {content_id} is deleted sucessfully')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)






def search_student():
    def search_data():
        query='select * from student where id=%s or name =%s or email=%s or mobile=%s or address=%s or gender=%s or dob=%s'
        mycursor.execute(query,(idEntry.get(),nameEntry.get(),emailEntry.get(),phoneEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data=mycursor.fetchall()
        for data in fetched_data:
            studentTable.insert('',END,values=data)


    search_window = Toplevel()
    search_window.title('search student')
    search_window.grab_set()
    search_window.resizable(False, False)
    idLabel = Label(search_window, text='Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(search_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(search_window, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(search_window, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(search_window, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    dobLabel = Label(search_window, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=5, column=1, pady=15, padx=10)

    genderLabel = Label(search_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=6, column=1, pady=15, padx=10)


    search_student_button = ttk.Button(search_window, text='Search student', command=search_data)
    search_student_button.grid(row=7, columnspan=2, pady=15)


def add_student():
    def add_data():
        if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()==''or addressEntry.get()=='' or dobEntry.get()=='' or genderEntry.get()=='' :
            messagebox.showerror('Error','All fields are required',parent=screen)
        else:
            currentdate=time.strftime('%d/%m/%y')
            currenttime=time.strftime('%H:%M:%S')
            query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),dobEntry.get(),genderEntry.get(),currentdate,currenttime))
            con.commit()
            result=messagebox.askyesno('confirm','Data saved sucessfully.Do you want to clean the form?')
            if result:
                idEntry.delete(0,END)
                nameEntry.delete(0, END)
                phoneEntry.delete(0, END)
                emailEntry.delete(0, END)
                addressEntry.delete(0, END)
                genderEntry.delete(0, END)
                dobEntry.delete(0, END)

            query='select * from student'
            mycursor.execute(query)
            fetched_data=mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for data in fetched_data:
                datalist=list(data)
                studentTable.insert('',END,values=datalist)


    screen=Toplevel()

    screen.grab_set()
    screen.resizable(False, False)
    idLabel = Label(screen, text='Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(screen, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(screen, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(screen, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(screen, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    dobLabel = Label(screen, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=5, column=1, pady=15, padx=10)

    genderLabel = Label(screen, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=6, column=1, pady=15, padx=10)



    add_student_button = ttk.Button(screen, text='ADD STUDENT', command=add_data)
    add_student_button.grid(row=7, columnspan=2, pady=15)
















def connect_database():
    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host='localhost' , user='root' ,
                            password='Sr@057sr')
            mycursor=con.cursor()
            messagebox.showinfo('sucess','data connection is sucess',parent=connectwindow)
        except:
            messagebox.showerror('Error','Invalid details',parent=connectwindow)
            return
        try:
            query='create database sms'
            mycursor.execute(query)
            query='use sms'
            mycursor.execute(query)
            query='create table student(id int not null primary key,name varchar(30),mobile varchar(30),' \
                   'email varchar (30),address varchar(100),gender varchar(10),dob varchar(14),' \
                  'date varchar(30),time varchar(30))'
            mycursor.execute(query)
        except:
            query = 'use sms'
            mycursor.execute(query)
        messagebox.showinfo('sucess', 'data connection is sucess', parent=connectwindow)
        connectwindow.destroy()
        addstudentbutton.config(state=NORMAL)
        updatestudentbutton.config(state=NORMAL)
        searchstudentbutton.config(state=NORMAL)
        deletestudentbutton.config(state=NORMAL)
        showstudentbutton.config(state=NORMAL)
        exportstudentdata.config(state=NORMAL)








    connectwindow=Toplevel()
    connectwindow.geometry('470x250+730+230')
    connectwindow.title('Database Connection')
    connectwindow.resizable(False,False)

    hostnamelabel=Label(connectwindow,text='Host Name',font=('arial',20,'bold'))
    hostnamelabel.grid(row=0,column=0,padx=20)

    hostentry=Entry(connectwindow,font=('roman',15,'bold'),bd=2)
    hostentry.grid(row=0,column=1,padx=40,pady=20)

    usernamelabel=Label(connectwindow,text='User Name',font=('arial',20,'bold'))
    usernamelabel.grid(row=1,column=0,padx=20)

    userentry=Entry(connectwindow,font=('roman',15,'bold'),bd=2)
    userentry.grid(row=1,column=1,padx=40,pady=20)

    passwordlabel=Label(connectwindow,text='Password',font=('arial',20,'bold'))
    passwordlabel.grid(row=2,column=0,padx=20)

    passwordentry=Entry(connectwindow,font=('roman',15,'bold'),bd=2)
    passwordentry.grid(row=2,column=1,padx=40,pady=20)


    connectdatabasebutton=ttk.Button(connectwindow,text='CONNECT',command=connect)
    connectdatabasebutton.grid(row=3,columnspan=2)



count=0
text=''
def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    sliderlabel.config(text=text)
    count+=1
    sliderlabel.after(300,slider)

def clock():
    date=time.strftime('%d/%m/%y')
    currenttime=time.strftime('%H:%M:%S')
    datetimelabel.config(text=f'  {date} \n {currenttime}')
    datetimelabel.after(1000,clock)


#UI

root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')


root.geometry('1174x680+20+20')
#root.resizable(False,False)
root.title('UI')

datetimelabel=Label(root,font=('times new roman',18,'bold'))
datetimelabel.place(x=5,y=5)
clock()

s='STUDENT MANAGEMENT SYSTEM'
sliderlabel=Label(root,text=s,font=('arial',28,'bold'),fg='cornflower blue')
sliderlabel.place(x=300,y=10)
slider()

# CONNECTING TO DATABASE

connectbutton=ttk.Button(root,text='Connect database',command=connect_database)
connectbutton.place(x=980,y=2)


#creating left frame

leftframe=Frame(root,bg='ivory2')
leftframe.place(x=50,y=80,width=300,height=500)

logo_image=PhotoImage(file='haha.png')
logolabel=Label(leftframe,image=logo_image)
logolabel.grid(padx=80,pady=10)

addstudentbutton=ttk.Button(leftframe,text='Add Student',width=20,state=DISABLED,command=add_student)
addstudentbutton.grid(row=1,column=0,pady=10)

searchstudentbutton=ttk.Button(leftframe,text='Search Student',width=20,state=DISABLED,command=search_student)
searchstudentbutton.grid(row=2,column=0,pady=10)

updatestudentbutton=ttk.Button(leftframe,text='Update Student',width=20,state=DISABLED,command=update_student)
updatestudentbutton.grid(row=3,column=0,pady=10)

deletestudentbutton=ttk.Button(leftframe,text='Delete Student',width=20,state=DISABLED,command=delete_student)
deletestudentbutton.grid(row=4,column=0,pady=10)

showstudentbutton=ttk.Button(leftframe,text='Show Student',width=20,state=DISABLED,command=show_student)
showstudentbutton.grid(row=5,column=0,pady=10)

exportstudentdata=ttk.Button(leftframe,text='export Student data',width=20,state=DISABLED,command=export_data)
exportstudentdata.grid(row=6,column=0,pady=10)

Exitbutton=ttk.Button(leftframe,text='Exit',width=20,command=iexit)
Exitbutton.grid(row=7,column=0,pady=10)


#creating right frame
rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=800,height=500)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile','Email','Address',
                                 'D.O.B','Gender','Added Date','Added Time'),
                          xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

studentTable.pack(expand=1,fill=BOTH)

studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Mobile',text='Mobile No')
studentTable.heading('Email',text='Email Address')
studentTable.heading('Address',text='Address')

studentTable.heading('D.O.B',text='D.O.B')
studentTable.heading('Gender',text='Gender')

studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')

studentTable.column('Id',width=50,anchor=CENTER)
studentTable.column('Name',width=200,anchor=CENTER)
studentTable.column('Email',width=300,anchor=CENTER)
studentTable.column('Mobile',width=200,anchor=CENTER)
studentTable.column('Address',width=300,anchor=CENTER)

studentTable.column('D.O.B',width=200,anchor=CENTER)
studentTable.column('Gender',width=100,anchor=CENTER)
studentTable.column('Added Date',width=200,anchor=CENTER)
studentTable.column('Added Time',width=200,anchor=CENTER)

style=ttk.Style()

style.configure('Treeview', rowheight=40,font=('times new roman', 12, 'bold'), fieldbackground='white', background='white',)
style.configure('Treeview.Heading',font=('times new roman', 14, 'bold'),foreground='black')

studentTable.config(show='headings')


root.mainloop()
