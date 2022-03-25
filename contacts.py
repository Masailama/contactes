import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from utils import BUTTON_FONT, LABEL_FONT, PATH_PHOTO, TABLE, resize_image, run_sql
from PIL import ImageTk


class ContactsView(tk.Frame):
    def __init__(self, window, db_name="contactes"):
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
        self.txt_photo.bind("<Double Button 1>", self.select_image)
        self.frame_buttons = tk.Frame(self, bg=self.cget("bg"))
        self.bt_add = tk.Button(self.frame_buttons, text="Afegir registre", bg="bisque", relief="flat", bd=0, 
            activebackground="navajo white", cursor="hand2", font=BUTTON_FONT, command=self.add_contact)
        self.bt_update = tk.Button(self.frame_buttons, text="Actualitzar registre", bg="bisque", relief="flat", 
            bd=0, activebackground="navajo white", cursor="hand2", font=BUTTON_FONT, command=self.update_contact)
        self.bt_delete = tk.Button(self.frame_buttons, text="Eliminar registre", bg="bisque", relief="flat", 
            bd=0, activebackground="navajo white", cursor="hand2", font=BUTTON_FONT, command=self.delete_contact)
        self.bt_erase = tk.Button(self.frame_buttons, text="Esborrar camps", bg="bisque", relief="flat", bd=0, 
            activebackground="navajo white", cursor="hand2", font=BUTTON_FONT, command=self.erase_fields)
        self.frame_list = tk.Frame(self, bg=self.cget("bg"))
        self.scroll_list = tk.Scrollbar(self.frame_list, orient="vertical")
        self.contact_list = ttk.Treeview(self.frame_list, columns=["name", "surname", "phone"], height=10,
            yscrollcommand=self.scroll_list.set)
        self.contact_list.heading("#0", text="ID")
        self.contact_list.heading("name", text="Nom")
        self.contact_list.heading("surname", text="Cognoms")
        self.contact_list.heading("phone", text="Telèfon")
        self.contact_list.column("#0", width=50, anchor=tk.CENTER)
        self.contact_list.column("name", anchor=tk.CENTER)
        self.contact_list.column("surname", anchor=tk.CENTER)
        self.contact_list.column("phone", anchor=tk.CENTER)
        self.contact_list.bind("<Double Button 1>", self.select_contact)
        self.scroll_list.config(command=self.contact_list.yview)
        self.draw()
        self.create_database()
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

    def add_contact(self):
        if self.check_fields():
            sql = "INSERT INTO CONTACTE VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
            params = (self.fin_id(), self.txt_name.get().upper(), self.txt_surname.get().upper(), 
                self.txt_phone.get(), self.txt_email.get(), self.txt_street.get(), self.txt_city.get().upper(),
                self.path_image)
            run_sql(name=self.db_name, query=sql, parameters=params)
            messagebox.showinfo("Contactes", "Contacte afegit correctament.")
            self.fill_list()
            self.erase_fields()

    def update_contact(self):
        if len(self.contact_list.selection()) > 0:
            if self.check_fields():
                sql = "UPDATE CONTACTE SET NOM=?, COGNOMS=?, TELEFON=?, EMAIL=?, CARRER=?, CIUTAT=?, FOTO=? WHERE ID=?"
                params = (self.txt_name.get().upper(), self.txt_surname.get().upper(), self.txt_phone.get(), 
                    self.txt_email.get(), self.txt_street.get(), self.txt_city.get().upper(), self.path_image,
                    self.contact_list.item(self.contact_list.selection()[0])["text"])
                run_sql(name=self.db_name, query=sql, parameters=params)
                messagebox.showinfo("Contactes", "Has actualitzat un contacte.")
                self.erase_fields()
                self.fill_list()

    def delete_contact(self):
        if len(self.contact_list.selection()) > 0:
            sql = "DELETE FROM CONTACTE WHERE ID=?"
            params = (self.contact_list.item(self.contact_list.selection()[0])["text"], )
            run_sql(name=self.db_name, query=sql, parameters=params)
            messagebox.showinfo("Contactes", "Has eliminat un contacte.")
            self.erase_fields()
            self.fill_list()

    def erase_fields(self):
        self.txt_name.delete(0, tk.END)
        self.txt_surname.delete(0, tk.END)
        self.txt_phone.delete(0, tk.END)
        self.txt_email.delete(0, tk.END)
        self.txt_street.delete(0, tk.END)
        self.txt_city.delete(0, tk.END)
        self.add_image(PATH_PHOTO)
        self.txt_name.focus()

    def add_image(self, image):
        self.path_image = image
        self.img_contact = ImageTk.PhotoImage(resize_image(self.path_image))
        self.txt_photo["image"] = self.img_contact

    def select_image(self, event):
        image =filedialog.askopenfilename(title="Seleccionar imatge", 
            filetypes=(("imatges PNG", "*.png"), ("imatges JPG", "*.jpg;*.jpeg")))
        if image:
            self.add_image(image)

    def create_database(self):
        sql = TABLE
        run_sql(name=self.db_name, query=sql)
        self.fill_list()

    def check_fields(self):
        if self.txt_name.get() != "" and self.txt_phone.get() != "":
            return True
        messagebox.showerror("Contactes", "Has d'emplenar el nom i el telèfon.")
        return False

    def fin_id(self):
        num_id = 1
        sql = "SELECT ID FROM CONTACTE ORDER BY ID ASC"
        data = run_sql(name=self.db_name, query=sql, read=True)
        for item in data:
            if item[0] != num_id:
                break
            num_id += 1
        return num_id

    def fill_list(self):
        for item in self.contact_list.get_children():
            self.contact_list.delete(item)
        sql = "SELECT ID, NOM, COGNOMS, TELEFON FROM CONTACTE ORDER BY ID ASC"
        data = run_sql(name=self.db_name, query=sql, read=True)
        for item in data:
            text = item[0]
            values = (item[1], item[2], item[3])
            self.contact_list.insert("", tk.END, text=text, values=values)

    def select_contact(self, event):
        if self.contact_list.item(self.contact_list.selection()[0])["text"]:
            self.fill_fields(self.contact_list.item(self.contact_list.selection()[0])["text"])

    def fill_fields(self, id_contact):
        self.erase_fields()
        sql = "SELECT * FROM CONTACTE WHERE ID=?"
        params = (id_contact, )
        data = run_sql(name=self.db_name, query=sql, parameters=params, read=True)
        self.txt_name.insert(0, data[0][1])
        self.txt_surname.insert(0, data[0][2])
        self.txt_phone.insert(0, data[0][3])
        self.txt_email.insert(0, data[0][4])
        self.txt_street.insert(0, data[0][5])
        self.txt_city.insert(0, data[0][6])
        self.add_image(data[0][7])