from tkinter import *
from BackgroundPage import *
from Components.MessageComponent import *
from Components.ButtonComponent import *
from Components.table import *
from Queries.Admin import *
from DatabaseHelper import *
from tkinter import messagebox
from PIL import Image, ImageTk


class AdminPage(BackgroundPage):
    def __init__(self, root, details):
        super().__init__(root)
        self.header.config(text="JPSG Railway")
        self.header.place(x=650, y=20)
        self.f1.place(x=580, y=25)
        self.dct_IntVar = {}

        self.details = details
        self.welcome = Message(self.f, text=f"Welcome {self.details.get('AdminName')}", width=600,
                              font=("Monotype Corsiva", 30, "bold", "italic")
                              , bg="white", relief=SOLID, borderwidth=2)
        self.welcome.place(x=40, y=100)
        self.admin_email = WhiteMessage(self.f, text="Email: " + self.details.get("AdminEmail"),
                                        font=("Monotype Corsiva", 15, "bold", "italic"))
        self.admin_email.place(x=40, y=520)
        self.add_image()
        self.add_buttons()

    def add_image(self):
        self.admin_raw_image = Image.open('Images/' + self.details.get("AdminPhoto"))
        self.admin_raw_image.resize((180, 300))
        self.profile_pic = ImageTk.PhotoImage(self.admin_raw_image)
        AdminPage.profile_pic = self.profile_pic
        self.c = Canvas(self.f, width=180, height=300)
        self.canvas_pic = self.c.create_image(0, 0, image=self.profile_pic, anchor=NW)
        self.c.place(x=40, y=200)

    def add_buttons(self):
        self.logout = GrayButton(self.f, text="Logout", command=self.logout_admin, width=15,
                                     font=("Monotype Corsiva", 15, "bold", "italic"))
        self.logout.place(x=1300,y=100)

        self.view_all = GrayButton(self.f, text="View all tickets", command=self.view_all_tickets, width=15,
                                 font=("Monotype Corsiva", 15, "bold", "italic"))
        self.view_all.place(x=1300, y=200)

        self.non_confirmed = GrayButton(self.f, text="View Non-confirmed tickets", command=self.non_confirmed_tickets
                                        , width=25,font=("Monotype Corsiva", 15, "bold", "italic"))
        self.non_confirmed.place(x=1300, y=300)

        self.confirm = GrayButton(self.f, text="Confirm tickets", command=self.confirm_tickets, width=15,
                                 font=("Monotype Corsiva", 15, "bold", "italic"))
        self.confirm.place(x=1300, y=400)

        self.analytics = GrayButton(self.f, text="Analytics", command=self.analytics_call, width=15,
                                  font=("Monotype Corsiva", 15, "bold", "italic"))
        self.analytics.place(x=1300, y=500)


    def logout_admin(self):
        import MainPage
        self.f.destroy()
        MainPage.MainPage(self.root)

    def view_all_tickets(self):
        query = Query.CONFIRMED_TICKETS
        result = DatabaseHelper.get_all_data(query)

        self.tickets_table = SimpleTable(self.f,rows=len(result),columns= len(result[0]), width=878, height=500)
        self.tickets_table.place(x=380, y=200)
        self.tickets_table.grid_propagate(0)
        for i in range(len(result)):
            for j in range(len(result[0])):
                self.tickets_table.set(row=i, column=j, value=result[i][j], width=18)


    def non_confirmed_tickets(self):
        query = Query.PENDING_TICKETS
        result = DatabaseHelper.get_all_data(query)

        self.tickets_table = SimpleTable(self.f, rows=len(result), columns=len(result[0]), width=878, height=500)
        self.tickets_table.place(x=380, y=200)
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


    def confirm_tickets(self):
        selected_items = []
        for key, value in self.dct_IntVar.items():
            if (value.get() == 1):
                selected_items.append(key)
                self.dct_IntVar[key].set(0)
        print(selected_items)
        if (len(selected_items) == 0):
            messagebox.showwarning("Row not selected", "Please select atleast one ticket to confirm")
        else:
            query = Query.CONFIRM_TICKETS
            DatabaseHelper.execute_all_data_multiple_input(query, selected_items)
            messagebox.showinfo("Success", f"Tickets with ID's {selected_items} are confirmed")
            self.non_confirmed_tickets()

    def analytics_call(self):
        import Analyticspage
        Analyticspage.Analytics()

if __name__ == "__main__":
    root = Tk()
    admin_details = {'AdminId': 2, 'UserName': 'Jai', 'AdminPassword': 'prerna',
                     'AdminEmail': '2019prerna.peswani@ves.ac.in',
                     'AdminPhoto': 'Prerna.jpeg'}
    a = AdminPage(root, admin_details)
    root.mainloop()
