######################### HOME PAGE   ####################################################
from datetime import date
from datetime import datetime

from tkinter import *
import sys

running="main"
sign_in="no"
personal_text=""

def opensignin(event):
    global running
    root.destroy()
    running="sign_in"


def opensignup(event):
    global running
    root.destroy()
    running="sign_up"
    


root=Tk()
root.title("Homepage")


root.geometry("480x400")
root.title("Test button")
root.configure(bg="blue")
root.resizable(False, False)

b1 = Button(root, text="Sign in", height=8, width=25, bg="lightBlue", cursor="hand2")
b2 = Button(root, text="Sign up", height=8, width=25, bg="lightBlue", cursor="hand2")
b1.bind("<Button-1>", opensignin)
b2.bind("<Button-1>", opensignup)

b1.place(x=160, y=50)
b2.place(x=160, y=200)



root.mainloop()

#############################        SIGN UP PAGE     #####################################################################################################


def _quit():
    running="main"
    sign_in=="no"
    global root
    root.destroy()
    sys.exit()

def show():
    password_entry.configure(show="")
    checkbox.configure(command=hide, text="Show password")

def hide():
    password_entry.configure(show="*")
    checkbox.configure(command=show, text="Show password")


def create_login(event):
    user_vacancy=0
    username1=(username.get())
    password1=(password.get())
    username1=("'" + username1 + "'")
    password_length=(len(password1))
    username_length=(len(username1))

    if password_length > 4:
        if username_length > 6:
            f=open("names.txt", "r")
            for line in f:
                if username1 in line:
                    user_vacancy=(user_vacancy+1)
            f.close()

            if user_vacancy > 0:
                invalid_label=Label(root, text="\tUsername is taken\t", bg="red")
                invalid_label.place(x=35, y=130)
            else:
                invalid_label=Label(root, text="\tNew account created\t", bg="red")
                invalid_label.place(x=35, y=130)
                f=open("names.txt", "a+")
                f.write("\n" + username1)
                f.close()
                f=open("passwords.txt", "a+")
                f.write("\n" + password1)
                f.close()
                running="sign_in"
                root.destroy()
                running="sign_in"
        else:
            invalid_label=Label(root, text="\tUsername is too short\t", bg="red")
            invalid_label.place(x=35, y=130)
    else:
        invalid_label=Label(root, text="\tPassword is too short\t", bg="red")
        invalid_label.place(x=35, y=130)



while running=="sign_up":

    root=Tk()
    root.title("Sign up")
    root.geometry("600x152")
    root.configure(bg="#dbdbdb")
    username=StringVar()
    password=StringVar()
    root.resizable(False, False)
    root.title("Sign up")

    frame=Frame(root, height=50, width=250, relief="groove", borderwidth=3, cursor="hand1", bg="#fcfafa")
    frame.place(x=300, y=30)
    #check if window is closed
    root.protocol("WM_DELETE_WINDOW", _quit)

    #objects
    title_label=Label(root, text="\t\t\t\t\tEnter a new username and password\t\t\t\t\t", bg="blue", fg="white")
    name_label=Label(root, text="Username", bg="#dbdbdb")
    password_label=Label(root, text="Password", bg="#dbdbdb")
    name_entry=Entry(root, textvariable=username, width=30, bg="#d6d6d6")
    password_entry=Entry(root, textvariable=password, width=30, show="*", bg="#d6d6d6")
    checkbox=Checkbutton(root, text="Show password", command=show, bg="#dbdbdb", activebackground='#c3c4c7', cursor="hand2")
    signup_button=Button(root, text="Sign up", bg="#dbdbdb", fg="black", activebackground='#c3c4c7', cursor="hand2")
    info_label=Label(frame, text="-Your password must be at least 5 characters\n-Your username must be at least 5 characters\n-You can't use an existing username\t\t\n-You can use a combination of any characters", bg="#d6d6d6")

    #placing objects
    title_label.place(x=0, y=1)
    name_label.place(x=2, y=32)
    password_label.place(x=2, y=57)
    name_entry.place(x=61, y=32)
    password_entry.place(x=61, y=57)
    checkbox.place(x=5, y=91)
    info_label.pack()
    signup_button.place(x=193, y=89)
    signup_button.bind("<Button-1>", create_login)






    root.mainloop()
    running="sign_in"




######################################      SIGN IN PAGE        ############################################################################################################


def show():
    entry_2.configure(show="")
    c.configure(command=hide, text="Show password")

def hide():
    entry_2.configure(show="*")
    c.configure(command=show, text="Show password")



def login_check(event):
    global username_verify
    global password_verify
    password_verify=False
    username_verify=False
    username1=(username.get())
    password1=(password.get())
    username1=("'"+username1+"'")
    user_line = (int(0))
    line_num=0
    f=open("names.txt", mode="r")
    for line in f:
        line_num+=1
        if username1 in line:
            user_line = (line_num)
            user_line = (user_line-1)
            username_verify=True
            
    f.close()

    f=open("passwords.txt", mode="r")
    readtxt = f.readlines()
    password_line = (readtxt[user_line])
    password_line=(password_line.strip())
    
    
    if password1 == (password_line):
        password_verify=True
        
    else:
        password_verify=False

    if password_verify==True and username_verify==True:
        global sign_in
        sign_in="yes"
        root.destroy()

    else:
        wrongLabel = Label(frame, text="  Incorrect username or password  ", bg="#dbdbdb", fg="red")
        wrongLabel.place(x=0, y=0)




while running=="sign_in":


    
    root = Tk()
    root.geometry("290x162")
    root.configure(bg="#dbdbdb")
    frame=Frame(root, height=25, width=290, relief="sunken", borderwidth=3, bg="#dbdbdb")
    frame.place(x=0, y=140)
    root.title("Sign in")
    root.resizable(False, False)


    username = StringVar()  
    password = StringVar()


    titleLabel = Label(root, text="\tEnter your username and password\t  ", fg="white", bg="blue")
    label_1 = Label(root, text="Username", bg="#dbdbdb", fg="black")
    label_2 = Label(root, text="Password", bg="#dbdbdb", fg="black")
    entry_1 = Entry(root, textvariable=username, width=30, bg="#d6d6d6", fg="black")
    entry_2 = Entry(root, textvariable=password, show="*", width=30, bg="#d6d6d6", fg="black")

    #check if window is closed
    root.protocol("WM_DELETE_WINDOW", _quit)



    c = Checkbutton(root, text="Show password", command=show, bg="#dbdbdb", activebackground='#c3c4c7', cursor="hand2")
    c.place(x=5, y=91)

    titleLabel.place(x=15, y=1)
    label_1.place(x=15, y=32)
    label_2.place(x=15, y=57)

    entry_1.place(x=76, y=32)
    entry_2.place(x=76, y=57)



    printButton = Button(root,  text="Sign in", bg="#dbdbdb", fg="black", activebackground='#c3c4c7', cursor="hand2")
    printButton.bind("<Button-1>", login_check)
    printButton.place(x=193, y=89)




    root.mainloop()

    #checking username and password for second root (personal text)
    password_verify=False
    username_verify=False
    username1=(username.get())
    password1=(password.get())
    username1=("'"+username1+"'")
    user_line = (int(0))
    line_num=0
    f=open("names.txt", mode="r")
    for line in f:
        line_num+=1
        if username1 in line:
            user_line = (line_num)
            user_line = (user_line-1)
            username_verify=True
                
    f.close()

    f=open("passwords.txt", mode="r")
    readtxt = f.readlines()
    password_line = (readtxt[user_line])
    password_line=(password_line.strip())


    #second root############################################################################################
    while sign_in=="yes":
        def set_personal():
            global date
            f=open("personal.txt", "r")
            readfile=f.readlines()
            personal_text=(readfile[user_line])
            personal_text = personal_text.strip()
            status = Frame(root, height=1, bd=1, relief=SUNKEN)
            status.pack(side=BOTTOM, fill=X)
            personal_label = Label(status, text=personal_text)
            personal_label.pack(side=LEFT)
            statustext = Label(status, text="Logged in at : ")

            #date and time            
            today = date.today()
            date = today.strftime("%d/%m/%Y")
            now = datetime.now()
            currentTime = now.strftime("%H:%M:%S")
            
            timelabel = Label(status, text=currentTime)
            datelabel = Label(status, text=date)
            timelabel.pack(side=RIGHT)
            datelabel.pack(side=RIGHT)
            statustext.pack(side=RIGHT)

    
        #window
        root=Tk()
        root.geometry("700x300")
        root.configure(bg="#b7bdc4")
        set_personal()


        #bar menu
        barMenu = Menu(root)
        root.config(menu=barMenu)
        fileMenu = Menu(barMenu) 
        barMenu.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="New file")
        fileMenu.add_separator()
        fileMenu.add_command(label="open...")
        editMenu=Menu(barMenu)
        barMenu.add_cascade(label="Edit", menu=editMenu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")




        #check if window is closed
        root.protocol("WM_DELETE_WINDOW", _quit)




        
        root.mainloop()


