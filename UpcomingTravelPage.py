from BackgroundPage import *
from tkinter import *
from Components.ButtonComponent import *
from Queries.User import *
from DatabaseHelper import *
from Components.table import *
from tkinter import messagebox


class UpcomingTravel(BackgroundPage):
    def __init__(self, root, details):
        super().__init__(root)
        self.header.config(text="JPSG Railway")
        self.header.place(x=650, y=20)
        self.f1.place(x=580, y=25)
        self.details = details
        self.user_id = Message(self.f, text=f"Username: {self.details.get('UserName')} \nUserId: "
                                            f"{self.details.get('UserId')}", width=600,
                               font=("Monotype Corsiva", 20, "bold", "italic")
                               , bg="white", relief=SOLID, borderwidth=2)
        self.user_id.place(x=1300, y=200)
        self.logout = GrayButton(self.f, text="Logout", command=self.logout_user, width=10,
                                 font=("Monotype Corsiva", 15, "bold", "italic"))
        self.logout.place(x=1300, y=100)
        self.cancel = GrayButton(self.f, text="Cancel Booking", command=self.cancel_button, width=20,
                                 font=("Monotype Corsiva", 20, "bold", "italic"))
        self.cancel.place(x=600, y=700)
        self.back = GrayButton(self.f, text="Back", command=self.go_back, width=10,
                               font=("Monotype Corsiva", 18, "bold", "italic"))
        self.back.place(x=1300, y=300)
        self.dct_IntVar = {}
        self.upcoming_travel()

    def go_back(self):
        self.f.destroy()
        import UserPage
        UserPage.UserPage(self.root, self.details)


    def upcoming_travel(self):
        query = Query.UPCOMING_TRAVEL
        parameter = (self.details.get('UserName'))
        result = DatabaseHelper.get_all_data(query,parameter)
        self.tickets_table = SimpleTable(self.f, rows=len(result), columns=len(result[0]), width=1040, height=500)
        self.tickets_table.place(x=10, y=100)
        self.tickets_table.grid_propagate(0)
        for i in range(1, len(result)):
            self.dct_IntVar[result[i][0]] = IntVar()
        for i in range(len(result)):
            for j in range(len(result[0])):
                self.tickets_table.set(row=i, column=j, value=result[i][j], width=18)

        for i in range(len(result)):
            for j in range(len(result[0])):
                if (j == 0 and i != 0):
                    c = Checkbutton(self.tickets_table, text=result[i][j],
                                    variable=self.dct_IntVar.get(result[i][j]))
                    self.tickets_table.set(row=i, column=j, value=result[i][j], widget=c)
                else:
                    self.tickets_table.set(row=i, column=j, value=result[i][j])



    def logout_user(self):
        import MainPage
        self.f.destroy()
        MainPage.MainPage(self.root)

    def cancel_button(self):
        selected_items = []
        for key, value in self.dct_IntVar.items():
            if (value.get() == 1):
                selected_items.append(key)
                self.dct_IntVar[key].set(0)
        print(selected_items)
        if (len(selected_items) == 0):
            messagebox.showwarning("Row not selected", "Please select atleast one ticket to cancel")
        else:
            query = Query.CANCEL_BOOKING
            DatabaseHelper.execute_all_data_multiple_input(query, selected_items)
            messagebox.showinfo("Success", f"Tickets with ID's {selected_items} are cancelled")
            self.upcoming_travel()



if __name__ == "__main__":
    root = Tk()
    user_details = {'UserId': 2, 'UserName': 'Jai', 'UserPassword': 'prerna',
                    'UserEmail': '2019prerna.peswani@ves.ac.in', }
    a = UpcomingTravel(root, user_details)
    root.mainloop()