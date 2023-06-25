from tkinter import *
from BackgroundPage import *
from Components.ButtonComponent import *
from tkinter import messagebox
from Queries.User import *
from DatabaseHelper import *
from Components.table import *


class UserPage(BackgroundPage):
    def __init__(self, root, details):
        super().__init__(root)
        self.header.config(text="JPSG Railway")
        self.header.place(x=650, y=20)
        self.f1.place(x=580, y=25)
        self.details = details
        self.welcome = Message(self.f, text=f"Welcome {self.details.get('UserName')}", width=600,
                               font=("Monotype Corsiva", 30, "bold", "italic")
                               , bg="white", relief=SOLID, borderwidth=2)
        self.welcome.place(x=40, y=200)

        self.user_id = Message(self.f, text=f"Username: {self.details.get('UserName')} \nUserId: "
                                            f"{self.details.get('UserId')}", width=600,
                               font=("Monotype Corsiva", 20, "bold", "italic")
                               , bg="white", relief=SOLID, borderwidth=2)
        self.user_id.place(x=1300, y=200)
        self.train_details = {}
        self.add_widgets()

    def add_widgets(self):
        self.logout = GrayButton(self.f, text="Logout", command=self.logout_user, width=10,
                                 font=("Monotype Corsiva", 15, "bold", "italic"))
        self.logout.place(x=1300, y=100)
        self.upcoming_travels = GrayButton(self.f, text="Upcoming travels", command=self.check_upcoming, width=15,
                                           font=("Monotype Corsiva", 20, "bold", "italic"))
        self.upcoming_travels.place(x=1300, y=320)
        self.ticket = Message(self.f, text=f"Book Tickets:", width=600, font=("Monotype Corsiva", 20, "bold", "italic")
                              , bg="white", relief=SOLID, borderwidth=2)
        self.ticket.place(x=670, y=400)
        self.from_label = Message(self.f, text=f"From:", width=600, font=("Monotype Corsiva", 20, "bold", "italic")
                                  , bg="white", relief=SOLID, borderwidth=2)
        self.from_label.place(x=200, y=550)
        self.from_entry = Entry(self.f, width=30, fg='black', bg='white')
        self.from_entry.place(x=150, y=610)

        self.to_label = Message(self.f, text=f"To:", width=600, font=("Monotype Corsiva", 20, "bold", "italic")
                                , bg="white", relief=SOLID, borderwidth=2)
        self.to_label.place(x=500, y=550)
        self.to_entry = Entry(self.f, width=30, fg='black', bg='white')
        self.to_entry.place(x=450, y=610)

        self.date_label = Message(self.f, text=f"Date(YYYY-MM-DD):", width=600,
                                  font=("Monotype Corsiva", 20, "bold", "italic")
                                  , bg="white", relief=SOLID, borderwidth=2)
        self.date_label.place(x=700, y=550)
        self.date_entry = Entry(self.f, width=30, fg='black', bg='white')
        self.date_entry.place(x=750, y=610)

        val = StringVar()
        val.set('All Classes')
        classes = ('AC First Class', 'Exec. Chair car', 'AC 2 Tier', 'First Class', 'AC 3 Tier')
        self.c1 = OptionMenu(self.f, val, *classes, command=self.func)
        self.c1.config(bg='white', font=("Monotype Corsiva", 20, "bold", "italic"))
        self.c1.place(x=1100, y=550)

        self.search_button = GrayButton(self.f, text="Search Trains", command=self.search, width=15,
                                        font=("Monotype Corsiva", 20, "bold", "italic"))
        self.search_button.place(x=650, y=750)

    def logout_user(self):
        import MainPage
        self.f.destroy()
        MainPage.MainPage(self.root)

    def search(self):
        if self.from_entry.get() == "" or self.to_entry.get() == "" or self.date_entry.get() == "":
            messagebox.showerror("Incomplete Data", "Please fill all the details")
        else:
            self.train_details['From'] = self.from_entry.get()
            self.train_details['To'] = self.to_entry.get()
            self.train_details['Date'] = self.date_entry.get()
            query = Query.SEARCH_TRAINS
            parameters = (self.train_details['From'], self.train_details['To'], self.train_details['Class'],
                          self.train_details['Date'])
            print(parameters)
            result = DatabaseHelper.get_all_data(query, parameters)
            print(result)
            print(len(result))
            if len(result) == 1:
                messagebox.showwarning("Unavailable", "No trains are available for selected options")
                self.f.destroy()
                UserPage(self.root, self.details)
            else:
                self.f.destroy()
                import TicketPage
                TicketPage.TicketPage(self.root, self.details, result)

    def func(self, value):
        self.train_details['Class'] = value

    def check_upcoming(self):
        self.f.destroy()
        import UpcomingTravelPage
        UpcomingTravelPage.UpcomingTravel(self.root,self.details)


if __name__ == "__main__":
    root = Tk()
    user_details = {'UserId': 2, 'UserName': 'Prerna', 'UserPassword': 'prerna',
                    'UserEmail': '2019prerna.peswani@ves.ac.in', }
    a = UserPage(root, user_details)
    root.mainloop()
