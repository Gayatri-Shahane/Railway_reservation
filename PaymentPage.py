from tkinter import *
from BackgroundPage import *
from Components.ButtonComponent import *
from Components.table import *
from tkinter import messagebox
from DatabaseHelper import *
from Queries.User import *

class Payment(BackgroundPage):
    def __init__(self, root, details, train_details,no_of_passengers):
        super().__init__(root)
        self.header.config(text="JPSG Railway")
        self.header.place(x=650, y=20)
        self.f1.place(x=580, y=25)
        self.details = details
        self.train_details = train_details
        self.no_of_passengers = no_of_passengers + 1
        self.add_ticket_details()
        self.add_widgets()

    def add_ticket_details(self):
        self.left_frame = Frame(self.f, width=570, height=500)
        self.left_frame.place(x=40, y=190)

        self.train_name = Message(self.left_frame, text=f"Train name: {self.train_details[1][1]}", width=600,
                                  font=("Monotype Corsiva", 20, "bold", "italic")
                                  , bg="white", relief=SOLID, borderwidth=2)
        self.train_name.place(x=10, y=10)

        self.passenger_count = Message(self.left_frame,
                                       text=f"Number of Passengers: {self.no_of_passengers}"
                                       , width=600, font=("Monotype Corsiva", 20, "bold", "italic"), bg="white",
                                       relief=SOLID, borderwidth=2)
        self.passenger_count.place(x=10, y=85)

        self.date = Message(self.left_frame,
                            text=f"Date:{self.train_details[1][2]}",
                            width=600,
                            font=("Monotype Corsiva", 20, "bold", "italic")
                            , bg="white", relief=SOLID, borderwidth=2)
        self.date.place(x=10, y=160)

        self.time = Message(self.left_frame, text=f"Time:{self.train_details[1][3]}", width=600,
                            font=("Monotype Corsiva", 20, "bold", "italic")
                            , bg="white", relief=SOLID, borderwidth=2)
        self.time.place(x=10, y=235)

        self.price = Message(self.left_frame, text=f"Price:{self.train_details[1][4]}", width=600,
                             font=("Monotype Corsiva", 20, "bold", "italic")
                             , bg="white", relief=SOLID, borderwidth=2)
        self.price.place(x=10, y=310)

        self.logout = GrayButton(self.f, text="Logout", command=self.logout_user, width=10,
                                 font=("Monotype Corsiva", 15, "bold", "italic"))
        self.logout.place(x=1300, y=100)
        self.back = GrayButton(self.f, text="Back", command=self.go_back, width=10,
                               font=("Monotype Corsiva", 18, "bold", "italic"))
        self.back.place(x=100, y=100)

    def add_widgets(self):
        self.right_frame = Frame(self.f, width=570, height=500)
        self.right_frame.place(x=850, y=190)
        self.card_num = Message(self.right_frame, text="Credit Card Number:", width=600, font=("Monotype Corsiva", 18, "bold", "italic")
                                  , bg="white", relief=SOLID, borderwidth=2)
        self.card_num.place(x=10, y=10)
        self.card_entry = Entry(self.right_frame, width=30, fg='black', bg='white')
        self.card_entry.place(x=260, y=25)

        self.card_holder_name = Message(self.right_frame, text="Card Holder Name:", width=600, font=("Monotype Corsiva", 20, "bold", "italic")
                                , bg="white", relief=SOLID, borderwidth=2)
        self.card_holder_name.place(x=10, y=85)
        self.card_holder_name_entry = Entry(self.right_frame, width=30, fg='black', bg='white')
        self.card_holder_name_entry.place(x=260, y=100)

        self.expiry_date = Message(self.right_frame, text="Expiry Date:", width=600,
                                        font=("Monotype Corsiva", 20, "bold", "italic")
                                        , bg="white", relief=SOLID, borderwidth=2)
        self.expiry_date.place(x=10, y=160)

        self.expiry_date_entry = Entry(self.right_frame, width=30, fg='black', bg='white')
        self.expiry_date_entry.place(x=260, y=175)

        self.cvv = Message(self.right_frame, text="CVV:", width=600,
                                   font=("Monotype Corsiva", 20, "bold", "italic")
                                   , bg="white", relief=SOLID, borderwidth=2)
        self.cvv.place(x=10, y=235)

        self.cvv_entry = Entry(self.right_frame, width=30, fg='black', bg='white')
        self.cvv_entry.place(x=260, y=250)

        self.pay_button = GrayButton(self.right_frame, text="Pay:", command=self.send_details_to_admin, width=10,
                                 font=("Monotype Corsiva", 15, "bold", "italic"))
        self.pay_button.place(x=220, y=330)


    def logout_user(self):
        self.f.destroy()
        import MainPage
        MainPage.MainPage(self.root)

    def go_back(self):
        self.f.destroy()
        import PassengerDetailsPage
        PassengerDetailsPage.PassengerDetails(self.root, self.details,self.train_details)

    def send_details_to_admin(self):
        if self.card_entry.get().isdigit() == False or self.cvv_entry.get().isdigit() == False:
            messagebox.showerror("Payment Unsuccessful", "Please enter correct details")
            self.reset()
        else:
            query = Query.INSERT_TICKET
            parameters = (self.details['UserName'], self.train_details[1][0], self.train_details[1][1],
                          self.train_details[1][3], self.train_details[1][2], self.train_details[1][4])
            DatabaseHelper.execute_query(query, parameters)
            query = Query.INSERT_IN_PASSENGER
            parameters = (self.train_details[1][0],self.no_of_passengers)
            DatabaseHelper.execute_query(query, parameters)
            message = "Payment received. You should hear about the confirmation of tickets soon."
            messagebox.showinfo('Payment Successful', message)
            self.f.destroy()
            import LastPage
            LastPage.LastPage(self.root)

    def reset(self):
        self.card_entry.delete(0, END)
        self.card_holder_name_entry.delete(0, END)
        self.expiry_date_entry.delete(0, END)
        self.cvv_entry.delete(0, END)
        self.card_entry.focus()


if __name__ == "__main__":
    root = Tk()
    user_details = {'UserId': 2, 'UserName': 'Prerna', 'UserPassword': 'prerna',
                    'UserEmail': '2019prerna.peswani@ves.ac.in', }
    train_details = {'TrainName': "Duronto Express", 'Date of departure': '06-05-2001', 'Time': '13:00'
        , 'No of Passengers': 3, 'Price': 'Rs 1000'}
    a = Payment(root, user_details, train_details)
    root.mainloop()
