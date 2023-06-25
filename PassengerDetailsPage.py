from tkinter import *
from BackgroundPage import *
from Components.ButtonComponent import *
from Components.table import *
from tkinter import messagebox


class PassengerDetails(BackgroundPage):
    def __init__(self,root,details,train_details):
        super().__init__(root)
        self.header.config(text="JPSG Railway")
        self.header.place(x=650, y=20)
        self.f1.place(x=580, y=25)
        self.details = details
        self.train_details = train_details
        self.display_message = Message(self.f, text="Add Passengers Details", width=600,
                               font=("Monotype Corsiva", 20, "bold", "italic")
                               , bg="white", relief=SOLID, borderwidth=2)
        self.display_message.place(x=40, y=170)

        self.user_id = Message(self.f, text=f"Username: {self.details.get('UserName')} \nUserId: "
                                            f"{self.details.get('UserId')}", width=600,
                               font=("Monotype Corsiva", 20, "bold", "italic")
                               , bg="white", relief=SOLID, borderwidth=2)
        self.user_id.place(x=1300, y=200)
        self.payment = GrayButton(self.f, text="Proceed to payment", command=self.payment_details, width=15,
                                       font=("Monotype Corsiva", 20, "bold", "italic"))
        self.payment.place(x=650, y=750)
        self.logout = GrayButton(self.f, text="Logout", command=self.logout_user, width=10,
                                 font=("Monotype Corsiva", 15, "bold", "italic"))
        self.logout.place(x=1300, y=100)
        self.back = GrayButton(self.f, text="Back", command=self.go_back, width=10,
                               font=("Monotype Corsiva", 18, "bold", "italic"))
        self.back.place(x=100, y=100)
        self.add_passenger_button = GrayButton(self.f, text="Add Passenger", command=self.add_passenger, width=15,
                                               font=("Monotype Corsiva", 18, "bold", "italic"))
        self.add_passenger_button.place(x=1200, y=320)
        self.count = 0
        self.add_widgets(0)


    def logout_user(self):
        import MainPage
        self.f.destroy()
        MainPage.MainPage(self.root)

    def go_back(self):
        self.f.destroy()
        import TicketPage
        TicketPage.TicketPage(self.root,self.details,self.train_details)

    def payment_details(self):
        if self.name_entry.get() == "" or self.age_entry=="" or self.contact_no_entry == "" or self.aadhar_no_entry.get()=="":
            messagebox.showerror("Incomplete details", "Please enter all details")
            self.reset()
        else:
            self.f.destroy()
            import PaymentPage
            PaymentPage.Payment(self.root,self.details,self.train_details,self.count)

    def reset(self):
        self.name_entry.delete(0, END)
        self.age_entry.delete(0, END)
        self.contact_no_entry.delete(0, END)
        self.aadhar_no_entry.delete(0, END)
        self.name_entry.focus()


    def add_widgets(self,jump):
        self.name_label = Message(self.f, text="Full Name:", width=600, font=("Monotype Corsiva", 20, "bold", "italic")
                                  , bg="white", relief=SOLID, borderwidth=2)
        self.name_label.place(x=100, y=250+jump)
        self.name_entry = Entry(self.f, width=30, fg='black', bg='white')
        self.name_entry.place(x=80, y=310+jump)

        self.age_label = Message(self.f, text="Age", width=600, font=("Monotype Corsiva", 20, "bold", "italic")
                                , bg="white", relief=SOLID, borderwidth=2)
        self.age_label.place(x=325, y=250+jump)
        self.age_entry = Entry(self.f, width=20, fg='black', bg='white')
        self.age_entry.place(x=300, y=310+jump)

        val = StringVar()
        val.set('Gender')
        classes = ('Male', 'Female', 'Other')
        self.c1 = OptionMenu(self.f, val, *classes)
        self.c1.config(bg='white', font=("Monotype Corsiva", 20, "bold", "italic"))
        self.c1.place(x=460, y=250+jump)

        self.contact_no = Message(self.f, text="Contact no:", width=600, font=("Monotype Corsiva", 20, "bold", "italic")
                                 , bg="white", relief=SOLID, borderwidth=2)
        self.contact_no.place(x=635, y=250+jump)
        self.contact_no_entry = Entry(self.f, width=30, fg='black', bg='white')
        self.contact_no_entry.place(x=620, y=310+jump)

        self.aadhar_no = Message(self.f, text="Aadhar no:", width=600, font=("Monotype Corsiva", 20, "bold", "italic")
                                  , bg="white", relief=SOLID, borderwidth=2)
        self.aadhar_no.place(x=850, y=250+jump)
        self.aadhar_no_entry = Entry(self.f, width=30, fg='black', bg='white')
        self.aadhar_no_entry.place(x=830, y=310+jump)

        val1 = StringVar()
        val1.set('Meal')
        classes1 = ('Veg', 'Non-veg', 'Jain')
        self.c2 = OptionMenu(self.f, val1, *classes1)
        self.c2.config(bg='white', font=("Monotype Corsiva", 20, "bold", "italic"))
        self.c2.place(x=1050, y=250+jump)




    def add_passenger(self):
        if self.count == 2:
            pass
        else:
            self.count+=1
            self.add_widgets(150*self.count)



if __name__ == "__main__":
    root = Tk()
    user_details = {'UserId': 2, 'UserName': 'Prerna', 'UserPassword': 'prerna',
                    'UserEmail': '2019prerna.peswani@ves.ac.in', }
    a = PassengerDetails(root, user_details)
    root.mainloop()