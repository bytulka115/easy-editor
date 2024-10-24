import os

from PIL import Image
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import *

app = QApplication([])
window = QWidget()



dir_btn = QPushButton("папка")
HorizontalLine = QHBoxLayout()
image_lbl = QLabel("картинки")
images_list = QListWidget()







def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap


class PhotoManger:
    def __init__(self):
        self.photo = None
        self.folder = None
        self.filename = None


    def load(self):
        image_path = os.path.join(self.folder, self.filename)
        self.photo = Image.open(image_path)


    def show_image(self, image_lbl):
        pixels = pil2pixmap(self.photo)
        pixels = pixels.scaledToWidth(500)
        image_lbl.setPixmap(pixels)














filter1 = QPushButton("фільтер1")
filter2 = QPushButton("фільтер2")
filter3 = QPushButton("фільтер3")
filter4 = QPushButton("фільтер4")
filter5 = QPushButton("фільтер5")

main_line = QHBoxLayout()

v1 = QVBoxLayout()
v1.addWidget(dir_btn)
v1.addWidget(images_list)
main_line.addLayout(v1)
v3 = QVBoxLayout()
v3.addWidget(image_lbl)
v2 = QHBoxLayout()
v2.addWidget(filter1)
v2.addWidget(filter2)
v2.addWidget(filter3)
v2.addWidget(filter4)
v2.addWidget(filter5)
v3.addLayout(v2)




main_line.addLayout(v3)


photo_manager = PhotoManger()



def open_folder():
    photo_manager.folder = QFileDialog.getExistingDirectory()

    files = os.listdir(photo_manager.folder)

    images_list.clear()

    for i in files:

    if i,endswith("png"):
        images_list.addItems((i))
    images_list.addItems(files)




def show_chosen_image():
    photo_manager.filename = images_list.currentItem().text()
    photo_manager.load()
    photo_manager.show_image(image_lbl)




images_list.currentRowChanged.connect(show_chosen_image)
















dir_btn.clicked.connect(open_folder)

window.setLayout(main_line)
window.show()
app.exec()