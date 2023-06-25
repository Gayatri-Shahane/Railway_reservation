from BackgroundPage import *
from tkinter import *
import time

class LastPage(BackgroundPage):
    def __init__(self,root):
        super().__init__(root)
        self.header.config(text="JPSG Railway")
        self.header.place(x=650, y=20)
        self.f1.place(x=580, y=25)
        last_message = "Thank You for using our services. Have a safe travel"
        self.display = Message(self.f, text=last_message, width=600,
                               font=("Monotype Corsiva", 40, "bold", "italic")
                               , bg="white", relief=SOLID, borderwidth=2)
        self.display.place(x=500, y=400)
        self.display.bind('<Button-1>',self.go_back_to_main_page)

    def go_back_to_main_page(self,event):
        self.f.destroy()
        import MainPage
        MainPage.MainPage(self.root)

if __name__ == "__main__":
    root = Tk()
    a = LastPage(root)
    root.mainloop()