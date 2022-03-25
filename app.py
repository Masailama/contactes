import tkinter as tk
from contacts import ContactsView


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contactes")
        self.resizable(0, 0)
        self.config(bg="slate gray")
 

if __name__ == "__main__":
    app = App()
    contacts = ContactsView(app)
    app.mainloop()
        