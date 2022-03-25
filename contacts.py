import tkinter as tk
from tkinter import ttk
from utils import BUTTON_FONT, LABEL_FONT, PATH_PHOTO, resize_image
from PIL import ImageTk


class ContactsView(tk.Frame):
    def __init__(self, window, db_name=""):
        tk.Frame.__init__(self, window, bg=window.cget("bg"))
        # variables
        self.path_image = PATH_PHOTO
        self.img_contact = ImageTk.PhotoImage(resize_image(self.path_image))
        self.db_name = f"{db_name}.db"
        # fields
        self.frame_fields = tk.Frame(self, bg=self.cget("bg"))
        self.lb_name = tk.Label(self.frame_fields, text="Nom: ", font=LABEL_FONT, bg=self.cget("bg"))
        self.txt_name = tk.Entry(self.frame_fields, width=20, bd=0, relief="flat")
        self.lb_surname = tk.Label(self.frame_fields, text="Cognoms: ", font=LABEL_FONT, bg=self.cget("bg"))
        self.txt_surname = tk.Entry(self.frame_fields, width=25, bd=0, relief="flat")
        self.lb_phone = tk.Label(self.frame_fields, text="Telèfon: ", font=LABEL_FONT, bg=self.cget("bg"))
        self.txt_phone = tk.Entry(self.frame_fields, width=15, bd=0, relief="flat")
        self.lb_email = tk.Label(self.frame_fields, text="E-mail: ", font=LABEL_FONT, bg=self.cget("bg"))
        self.txt_email = tk.Entry(self.frame_fields, width=35, bd=0, relief="flat")
        self.lb_street = tk.Label(self.frame_fields, text="Direcció: ", font=LABEL_FONT, bg=self.cget("bg"))
        self.txt_street = tk.Entry(self.frame_fields, width=50, bd=0, relief="flat")
        self.lb_city = tk.Label(self.frame_fields, text="Ciutat: ", font=LABEL_FONT, bg=self.cget("bg"))
        self.txt_city = tk.Entry(self.frame_fields, width=30, bd=0, relief="flat")
        self.txt_photo = tk.Label(self.frame_fields, image=self.img_contact)
        self.frame_buttons = tk.Frame(self, bg=self.cget("bg"))
        self.bt_add = tk.Button(self.frame_buttons, text="Afegir registre", bg="bisque", relief="flat", bd=0, 
            activebackground="navajo white", cursor="hand2", font=BUTTON_FONT)
        self.bt_update = tk.Button(self.frame_buttons, text="Actualitzar registre", bg="bisque", relief="flat", 
            bd=0, activebackground="navajo white", cursor="hand2", font=BUTTON_FONT)
        self.bt_delete = tk.Button(self.frame_buttons, text="Eliminar registre", bg="bisque", relief="flat", 
            bd=0, activebackground="navajo white", cursor="hand2", font=BUTTON_FONT)
        self.bt_erase = tk.Button(self.frame_buttons, text="Esborrar camps", bg="bisque", relief="flat", bd=0, 
            activebackground="navajo white", cursor="hand2", font=BUTTON_FONT)
        self.frame_list = tk.Frame(self, bg=self.cget("bg"))
        self.scroll_list = tk.Scrollbar(self.frame_list, orient="vertical")
        self.contact_list = ttk.Treeview(self.frame_list, columns=["name", "surname", "phone"], height=10,
            yscrollcommand=self.scroll_list.set)
        self.contact_list.heading("#0", text="ID")
        self.contact_list.heading("name", text="Nom")
        self.contact_list.heading("surname", text="Cognoms")
        self.contact_list.heading("phone", text="Telèfon")
        self.contact_list.column("#0", width=50)
        self.scroll_list.config(command=self.contact_list.yview)
        self.draw()
        self.txt_name.focus()

    def draw(self):
        self.pack(fill="both", expand=True)
        self.frame_fields.grid(row=0, column=0)
        self.lb_name.grid(row=0, column=0, padx=(10, 0), pady=(20, 0), sticky="e")
        self.txt_name.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="w")
        self.lb_surname.grid(row=1, column=0, padx=(10, 0), pady=(10, 0), sticky="e")
        self.txt_surname.grid(row=1, column=1, padx=(0, 10), pady=(10, 0), sticky="w")
        self.lb_phone.grid(row=2, column=0, padx=(10, 0), pady=(10, 0), sticky="e")
        self.txt_phone.grid(row=2, column=1, padx=(0, 10), pady=(10, 0), sticky="w")
        self.lb_email.grid(row=3, column=0, padx=(10, 0), pady=(10, 0), sticky="e")
        self.txt_email.grid(row=3, column=1, padx=(0, 10), pady=(10, 0), sticky="w")
        self.lb_street.grid(row=4, column=0, padx=(10, 0), pady=(10, 0), sticky="e")
        self.txt_street.grid(row=4, column=1, columnspan=2, padx=(0, 10), pady=(10, 0), sticky="w")
        self.lb_city.grid(row=5, column=0, padx=(10, 0), pady=(10, 20), sticky="e")
        self.txt_city.grid(row=5, column=1, padx=(0, 10), pady=(10, 20), sticky="w")
        self.txt_photo.grid(row=0, column=2, rowspan=3, padx=10, pady=(10, 0), sticky="e")
        self.frame_buttons.grid(row=0, column=1, sticky="ns")
        self.bt_add.pack(padx=(20, 10), pady=(30, 0))
        self.bt_update.pack(padx=(20, 10), pady=(20, 0))
        self.bt_delete.pack(padx=(20, 10), pady=(20, 0))
        self.bt_erase.pack(padx=(20, 10), pady=(20, 30))
        self.frame_list.grid(row=1, column=0, columnspan=2, pady=(10,20), padx=20)
        self.contact_list.pack(fill=tk.X, side="left")
        self.scroll_list.pack(side="right", fill=tk.Y)
