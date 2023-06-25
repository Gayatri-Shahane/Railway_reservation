from BackgroundPage import *
from tkinter import *
from Components.ButtonComponent import GrayButton


class MainPage(BackgroundPage):
    def __init__(self, root):
        super().__init__(root)
        self.root.geometry('1200x800')
        self.root.state('normal')
        self.facts = Message(self.f, text="Amazing Facts here!", width=600,
                             font=("Monotype Corsiva", 30, "bold", "italic")
                             , bg="white", relief=SOLID, borderwidth=2)
        self.facts.place(x=100, y=250)
        self.facts.bind('<Button-1>', self.display_facts)

        self.contact_us = Message(self.f, text="Contact Us!", width=600,
                             font=("Monotype Corsiva", 30, "bold", "italic")
                             , bg="white", relief=SOLID, borderwidth=2)
        self.contact_us.place(x=800, y=250)
        self.contact_us.bind('<Button-1>', self.contact_details)

        self.details = "Phone Number: 9247604525 \n Email: jpsgrailways@gmail.com"
        self.show_details = Message(self.f, text=self.details, width=400,
                                   font=("Monotype Corsiva", 25, "bold", "italic"), bg="black", fg="white",
                                   relief=SOLID, borderwidth=2)

        self.fact_1 = "1. Indian Railways track is spread across massive of 11500 km"
        self.fact_2 = "2. The famous Fairy Queen is the world’s oldest working locomotive that is still in use."

        self.show_fact_1 = Message(self.f, text=self.fact_1, width=400,
                                   font=("Monotype Corsiva", 25, "bold", "italic"), bg="black", fg="white",
                                   relief=SOLID, borderwidth=2)

        self.show_fact_2 = Message(self.f, text=self.fact_2, width=400,
                                   font=("Monotype Corsiva", 25, "bold", "italic"), bg="black", fg="white",
                                   relief=SOLID, borderwidth=2)

        self.get_button = GrayButton(self.f, text="Get Started", command=self.get_started, width=15,
                                     font=("Monotype Corsiva", 20, "bold", "italic"))
        self.get_button.place(x=500, y=700)

    def display_facts(self, event):
        self.show_fact_1.place(x=100, y=350)
        self.show_fact_2.place(x=100, y=500)

    def contact_details(self,event):
        self.show_details.place(x=750,y=350)

    def get_started(self):
        self.f.destroy()
        self.f1.destroy()
        import LoginPage
        LoginPage.LoginPage(self.root)


if __name__ == "__main__":
    root = Tk()
    d = MainPage(root)
    root.mainloop()
