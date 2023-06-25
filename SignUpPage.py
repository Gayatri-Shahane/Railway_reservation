from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from DatabaseHelper import *


class SignUp:
    def __init__(self):
        self.registration_window = Toplevel()
        self.frame = Frame(self.registration_window, height=400, width=700, bg="gray")
        self.frame.pack(fill=BOTH, expand="yes")
        self.setup_signup_page()

    def add_header_section(self):

        self.header_frame = Frame(self.frame, height=100, width=600)
        self.header_frame.pack(fill=X, side=TOP)
        self.header_frame.grid_propagate(0)

        self.welcome_label = Label(self.header_frame, text="Sign up",
                                   font=("Monotype Corsiva", 30, "bold", "italic"))
        self.welcome_label.place(x=250,y=20)

    def setup_signup_page(self):

        self.add_header_section()

        self.body_frame = Frame(self.frame, bg="white", height=300, width=600)
        self.body_frame.pack(side=TOP, fill=X)
        self.lab = Label(self.body_frame, width=50, text="Enter below details to create a new user account")
        self.lab.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.e_username = Entry(self.body_frame, width=30, fg='black', bg='white')
        self.e_pwd = Entry(self.body_frame, width=30, fg='black', bg='white', show='*')
        self.e_re_pwd = Entry(self.body_frame, width=30, fg='black', bg='white', show='*')
        self.e_email = Entry(self.body_frame, width=30, fg='black', bg='white')
        self.e_contact = Entry(self.body_frame, width=30, fg='black', bg='white')

        self.show_pwd = IntVar()
        self.show_pwd_check = Checkbutton(self.body_frame, text="Show", bg="white", command=self.show_hide_pwd,
                                          variable=self.show_pwd)

        Label(self.body_frame, width=20, text="Enter username: ").grid(row=2, column=1, padx=10, pady=10)
        Label(self.body_frame, width=20, text="Enter password: ").grid(row=3, column=1, padx=10, pady=10)
        Label(self.body_frame, width=20, text="Re-enter password: ").grid(row=4, column=1, padx=10, pady=10)
        Label(self.body_frame, width=20, text="Contact").grid(row=5, column=1, padx=10, pady=10)
        Label(self.body_frame, width=20, text="Email").grid(row=6, column=1, padx=10, pady=10)

        self.e_username.grid(row=2, column=2, padx=10, pady=10)
        self.e_pwd.grid(row=3, column=2, padx=10, pady=10)
        self.show_pwd_check.grid(row=3, column=3, padx=2, pady=10)
        self.e_re_pwd.grid(row=4, column=2, padx=10, pady=10)
        self.e_contact.grid(row=5, column=2, padx=10, pady=10)
        self.e_email.grid(row=6, column=2, padx=10, pady=10)

        self.e_username.focus_set()
        self.b_register = Button(self.body_frame, text="Create user", height=2, width=10,
                                 command=lambda: self.register_user())
        self.b_register.grid(row=7, column=1, columnspan=2, padx=10)
        self.b_reset = Button(self.body_frame, text="Reset", height=2, width=10, command=lambda: self.register_reset())
        self.b_reset.grid(row=7, column=2, columnspan=2, padx=10)

        self.body_frame.grid_propagate(0)


    def show_hide_pwd(self):
        if self.show_pwd.get() == 1:
            self.e_pwd.config(show="")
        else:
            self.e_pwd.config(show="*")

    def register_reset(self):
        self.e_username.delete(0, END)
        self.e_pwd.delete(0, END)
        self.e_email.delete(0, END)
        self.e_contact.delete(0, END)
        self.e_re_pwd.delete(0, END)

    def register_user(self):
        name = self.e_username.get()
        contact = self.e_contact.get()
        email = self.e_email.get()
        pwd = self.e_pwd.get()
        pwd2 = self.e_re_pwd.get()
        if (name == "" or contact == "" or email == "" or pwd == ""):
            messagebox.showwarning("Mandatory fields", "Please fill all the fields")
            self.registration_window.tkraise()
        elif (pwd != pwd2):
            messagebox.showerror("Password Error", "Passwords don't match.Please re-enter")
            self.registration_window.tkraise()
        else:
            query = "Insert into User(UserName,UserPassword, UserContact,UserEmailId) Values(%s,%s,%s,%s)"
            args = (name, pwd, contact, email)
            DatabaseHelper.execute_query(query, args)
            messagebox.showinfo("Success", "User registered successfully. Please login")
            self.registration_window.destroy()



if __name__ == "__main__":
    root = Tk()
    d = SignUp()
    root.mainloop()