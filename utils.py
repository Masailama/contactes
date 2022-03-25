import sqlite3
from PIL import Image

# imatges
PATH_PHOTO = "images/photo.png"

# fonts
TITLE_FONT = ("Segoe UI", 18, "bold")
LABEL_FONT = ("Segoe UI", 12, "bold")
BUTTON_FONT = ("Segoe UI", 10, "bold")

# Variables
TABLE = """CREATE TABLE IF NOT EXISTS CONTACTE (ID INTEGER PRIMARY KEY, NOM TEXT, COGNOMS TEXT, TELEFON TEXT, EMAIL TEXT, CARRER TEXT, CIUTAT TEXT, FOTO TEXT)""" 

# functions
def resize_image(path_image, size=(100, 100)):
    image = Image.open(path_image)
    image = image.resize(size)
    return image

def run_sql(name, query, parameters=(), read=False):
    connect_db = sqlite3.connect(name)
    cursor_db = connect_db.cursor()
    cursor_db.execute(query, parameters)
    data = cursor_db.fetchall()
    connect_db.commit()
    connect_db.close()
    if read:
        return data
    