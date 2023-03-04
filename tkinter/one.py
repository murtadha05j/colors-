from tkinter import Tk, Entry,Button,Label,messagebox, StringVar
root=Tk()
root.geometry("300x180")
root.title("login")
var1=StringVar()
var2=StringVar()

def log():
    import database_file
    num=database_file.database().check_user(var1.get(),var2.get())
    if num==1:
        messagebox.showinfo('login','hello' + var1.get())
        root.destroy()
        import new

    elif num==2:
        messagebox.showwarning("login", " password wrong ")
    else:
        messagebox.showinfo("log"," user is not exist ")
def sign_up():
    import signup
    signup.signup_frame().show_frame()
user=Label(root,text="user name")
user.place(x=20,y=30)
password=Label(root,text="password")
password.place(x=20,y=60)
user_name=Entry(root,textvariable=var1)
user_name.place(x=100,y=30)
Password=Entry(root,textvariable=var2,show=password)
Password.place(x=100,y=60)
login=Button(root,text="log in",command=log)
login.place(x=50,y=100)
signup=Button(root,text="sign up ",command=sign_up)
signup.place(x=120,y=100)

root.mainloop()