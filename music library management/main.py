from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from tkinter.ttk import *
from add import *
from delete import *
from view import *
from search import *

def main():
    mypass = "dharun1504"
    mydatabase="project"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    
    headingFrame1 = Frame(root,bg="#dfdee2",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="\n .....MUSIX MANAGEMENT.....", bg="black", fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    
    btn1 = Button(root,text="Add Some Tracks",font='Helvetica 10 bold',bg='black', fg='white', command=addsong)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

    btn2 = Button(root,text="U sure want to Delete  Tracks :(",font='Helvetica 10 bold',bg='black', fg='white', command=delete)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)



    btn3 = Button(root,text="Want to View Tracks...?",font='Helvetica 10 bold',bg='black', fg='white', command=view)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

    btn4 =Button(root,text="Search Some Tracks",font='Helvetica 10 bold',bg='black', fg='white', command=search)
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

    quitBtn = Button(root,text="Logout",font='Helvetica 11 bold',bg="#010103", fg='white', command=root.destroy)
    quitBtn.place(relx=0.41,rely=0.85, relwidth=0.18,relheight=0.08)



    root.mainloop()

root = Tk()
root.title("MUSIX MANAGEMENT SYSTEM")
root.minsize(width=400,height=400)
root.state('zoomed')
root.config(bg="purple")
main()

