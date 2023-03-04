class signup_frame():
    def show_frame(self):
        from tkinter import Tk, Entry, Button, Label, messagebox, StringVar
        root = Tk()
        root.geometry("300x180")
        root.title("sign up")
        var1 = StringVar()
        var2 = StringVar()
        def send_data():
            import database_file
            database_file.database().insert_data(var1.get(),var2.get())
            messagebox.showinfo("ok","insert data")
            root.destroy()
            import one

        user = Label(root, text="user name")
        user.place(x=20, y=30)
        password = Label(root, text="password")
        password.place(x=20, y=60)
        user_name = Entry(root, textvariable=var1)
        user_name.place(x=100, y=30)
        Password = Entry(root, textvariable=var2)
        Password.place(x=100, y=60)
        login = Button(root, text="send data", command=send_data)
        login.place(x=80, y=100)
        root.mainloop()
