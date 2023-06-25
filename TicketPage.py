from tkinter import *
from BackgroundPage import *
from Components.ButtonComponent import *
from Components.table import *
from Queries.User import *
from DatabaseHelper import *
from tkinter import messagebox

class TicketPage(BackgroundPage):
    def __init__(self,root,details,result):
        super().__init__(root)
        self.header.config(text="JPSG Railway")
        self.header.place(x=650, y=20)
        self.f1.place(x=580, y=25)
        self.details = details
        self.train_details = result
        self.dct_IntVar = {}
        self.welcome = Message(self.f, text=f"Welcome {self.details.get('UserName')}", width=600,
                               font=("Monotype Corsiva", 30, "bold", "italic")
                               , bg="white", relief=SOLID, borderwidth=2)
        self.welcome.place(x=40, y=200)

        self.user_id = Message(self.f, text=f"Username: {self.details.get('UserName')} \nUserId: "
                                            f"{self.details.get('UserId')}", width=600,
                               font=("Monotype Corsiva", 20, "bold", "italic")
                               , bg="white", relief=SOLID, borderwidth=2)
        self.user_id.place(x=1300, y=200)

        self.book_tickets = GrayButton(self.f, text="Book Tickets", command=self.book, width=15,
                                     font=("Monotype Corsiva", 20, "bold", "italic"))
        self.book_tickets.place(x=650, y=750)

        self.logout = GrayButton(self.f, text="Logout", command=self.logout_user, width=10,
                                 font=("Monotype Corsiva", 15, "bold", "italic"))
        self.logout.place(x=1300, y=100)
        self.back = GrayButton(self.f, text="Back", command=self.go_back, width=10,
                                 font=("Monotype Corsiva", 18, "bold", "italic"))
        self.back.place(x=100, y=100)
        self.display_trains(result)


    def display_trains(self,result):
        self.tickets_table = SimpleTable(self.f,rows=len(result),columns= len(result[0]), width=570, height=500)
        self.tickets_table.place(x=500, y=200)
        self.tickets_table.grid_propagate(0)
        for i in range(len(result)):
            for j in range(len(result[0])):
                self.tickets_table.set(row=i, column=j, value=result[i][j], width=16)

        for i in range(1, len(result)):
            self.dct_IntVar[result[i][0]] = IntVar()

        for i in range(len(result)):
            for j in range(len(result[0])):
                if (j == 0 and i != 0):
                     c = Checkbutton(self.tickets_table, text=result[i][j],
                                    variable=self.dct_IntVar.get(result[i][j]))
                     self.tickets_table.set(row=i, column=j, value=result[i][j], widget=c)
                else:
                     self.tickets_table.set(row=i, column=j, value=result[i][j])

    def book(self):
        selected_items = []
        for key, value in self.dct_IntVar.items():
            if value.get() == 1:
                selected_items.append(key)
                self.dct_IntVar[key].set(0)
        print(selected_items)
        if len(selected_items) == 0:
            messagebox.showwarning("No Trains selected", "Please select a train to proceed")
        elif len(selected_items) > 1:
            messagebox.showwarning("Multiple Trains selected", "Please select only one train to proceed")

        else:
            self.f.destroy()
            import PassengerDetailsPage
            PassengerDetailsPage.PassengerDetails(self.root,self.details,self.train_details)


    def logout_user(self):
        import MainPage
        self.f.destroy()
        MainPage.MainPage(self.root)

    def go_back(self):
        self.f.destroy()
        import UserPage
        UserPage.UserPage(self.root,self.details)

if __name__ == "__main__":
    root = Tk()
    user_details = {'UserId': 2, 'UserName': 'Prerna', 'UserPassword': 'prerna',
                    'UserEmail': '2019prerna.peswani@ves.ac.in', }

    a = TicketPage(root, user_details)
    root.mainloop()