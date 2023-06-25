from BackgroundPage import *
from tkinter import *
from Components.ButtonComponent import *
from LoginWindow import *
from SignUpPage import *



class LoginPage(BackgroundPage):
    def __init__(self, root):
        super().__init__(root)

        self.root.state('zoomed')
        self.header.place(x=600, y=20)
        self.f1.place(x=530, y=25)
        self.raw_image = Image.open("Images/Background3.jpeg")
        self.raw_image = self.raw_image.resize((1600, 900))
        self.img = ImageTk.PhotoImage(self.raw_image)
        LoginPage.img = self.img
        self.panel = Label(self.f, image=self.img)
        self.panel.pack()
        self.panel.pack_propagate(0)
        self.login = Message(self.f, text="Login", width=600,
                             font=("Monotype Corsiva", 20, "bold", "italic")
                             , bg="white", relief=SOLID, borderwidth=2)
        self.login.place(x=1210, y=200)
        self.admin_button = GrayButton(self.f, text="Admin Login", command=lambda : Login("Admin", self),height=2)
        self.admin_button.place(x=1050,y=300)
        self.admin_button = GrayButton(self.f, text="User Login", command=lambda: Login("User", self), height=2)
        self.admin_button.place(x=1300, y=300)
        self.admin_button = GrayButton(self.f, text="New User? Register now!", command=SignUp, height=2)
        self.admin_button.place(x=1175, y=400)

    def redirect_to_page(self,result,login_type):
        self.f.destroy()
        if login_type == "Admin":
            import AdminPage
            AdminPage.AdminPage(self.root, result)
        elif login_type == "User":
             import UserPage
             UserPage.UserPage(self.root, result)


if __name__ == "__main__":
    root = Tk()
    d = LoginPage(root)
    root.mainloop()
