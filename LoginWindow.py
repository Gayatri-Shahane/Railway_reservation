from tkinter import *
from tkinter import messagebox
from DatabaseHelper import *

class Login:
    def __init__(self,login_type,login_page):
        self.login_window = Toplevel()
        self.login_type = login_type
        self.login_window.title(login_type)
        self.login_window.iconbitmap('Images/Icon.ico')
        self.login_page = login_page
        f = Frame(self.login_window, height=200, width=400)
        l1 = Label(f, width=20, text="Enter username: ")
        self.e_username = Entry(f, width=30, fg='black', bg='white')
        self.e_username.focus_set()
        self.e_password = Entry(f, width=30, fg='black', bg='white', show='*')
        l2 = Label(f, width=20, text="Enter password: ")
        l1.grid(row=1, column=1, padx=10, pady=10)
        l2.grid(row=2, column=1, padx=10, pady=10)
        self.e_username.grid(row=1, column=4, padx=10, pady=10)
        self.e_password.grid(row=2, column=4, padx=10, pady=10)
        b1 = Button(f, text="Submit", height=2, width=10, command=self.validate)
        b1.grid(row=3, column=1, padx=10, sticky='e')
        b2 = Button(f, text="Reset", height=2, width=10, command=self.reset)
        b2.grid(row=3, column=4, padx=10, sticky='w')
        f.pack()
        f.grid_propagate(0)

    def validate(self):
        username = self.e_username.get()
        pwd = self.e_password.get()
        if self.login_type == "Admin":
            query = "Select * from railway.admin where AdminName= %s and AdminPassword=%s"
        else:
            query = "Select * from railway.user where UserName= %s and UserPassword=%s"
        parameters = (username, pwd)
        result = DatabaseHelper.get_data(query, parameters)
        if result is None:
            messagebox.showerror("Login Failed", "Incorrect credentials")
            self.login_window.tkraise()
            self.reset()
            self.e_username.focus()
        else:
            messagebox.showinfo('Login Success', "Login successfuly completed")
            self.login_window.destroy()
            self.login_page.redirect_to_page(result, self.login_type)


    def reset(self):
        self.e_username.delete(0, END)
        self.e_password.delete(0, END)
