import sqlite3
from PIL import Image

# imatges
PATH_PHOTO = "images/photo.png"

# fonts
TITLE_FONT = ("Segoe UI", 18, "bold")
LABEL_FONT = ("Segoe UI", 12, "bold")
BUTTON_FONT = ("Segoe UI", 10, "bold")

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
    