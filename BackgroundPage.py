from tkinter import *
from PIL import Image, ImageTk


class BackgroundPage:
    def __init__(self, root):
        self.root = root
        self.root.iconbitmap('Images/Icon.ico')
        self.root.title('JPSG Railway')

        self.f = Frame(self.root, width=1600, height=900)
        self.f.pack()

        self.raw_image = Image.open("Images/Background4.jpeg")
        self.raw_image = self.raw_image.resize((1600, 900))
        self.img = ImageTk.PhotoImage(self.raw_image)
        BackgroundPage.img=self.img
        self.panel = Label(self.f, image=self.img)
        self.panel.pack()
        self.panel.pack_propagate(0)

        self.f1 = Frame(root, width=60, height=60)
        self.f1.place(x=330, y=25)

        self.logo = Image.open("Images/Icon.ico")
        self.logo = self.logo.resize((60, 60))
        self.logo_img = ImageTk.PhotoImage(self.logo)
        BackgroundPage.img1=self.logo_img

        self.label = Label(self.f1, image=self.logo_img)
        self.label.pack()
        self.label.pack_propagate(0)
        self.header = Message(self.f, text="Welcome to JPSG Railways", width=600,
                              font=("Monotype Corsiva", 30, "bold", "italic")
                              , bg="white", relief=SOLID, borderwidth=2)
        self.header.place(x=400, y=20)


if __name__ == "__main__":
    root = Tk()
    d = BackgroundPage(root)
    root.mainloop()
