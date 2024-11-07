import os

from PIL import Image, ImageEnhance, ImageFilter
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import *

app = QApplication([])
window = QWidget()




app.setStyleSheet("""
        QWidget {
            background: #01a049;
        }
        
        QPushButton
        {
            background: #95c2d5;
            border-style: outset;
            font-family: Roboto;
            min_widh: 6em;
            padding: 6px;
            
        }
    
    """)










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

    def bw(self):
        self.photo = self.photo.convert("L")
        self.show_image(self.image_lbl)

    def rotate(self):
        self.photo = self.photo.transpose(Image.ROTATE_90)
        self.show_image(self.image_lbl)

    def yaskravist(self):
        self.photo = ImageEnhance.Brightness(self.photo).enhance(1.5)
        self.show_image(self.image_lbl)

    def kontrastnist(self):
        self.photo =  ImageEnhance.Contrast(self.photo).enhance(1.5)
        self.show_image(self.image_lbl)

    def blur(self):
        self.photo = self.photo.filter(ImageFilter.BLUR)
        self.show_image(self.image_lbl)

    def contur(self):
        self.photo = self.photo.filter(ImageFilter.CONTOUR)
        self.show_image(self.image_lbl)

    def emboss(self):
        self.photo = self.photo.filter(ImageFilter.EMBOSS )
        self.show_image(self.image_lbl)

    def Unsharp (self):
        self.photo = self.photo.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
        self.show_image(self.image_lbl)






















filter1 = QPushButton("ч/б")
filter2 = QPushButton("поворот ліворуч на 90 градусів")
filter3 = QPushButton("збільшення яскравості на 50%")
filter4 = QPushButton("збільшення контрастності на 50%")
filter5 = QPushButton("Розмивання")
filter6 = QPushButton("Накладення контурів")
filter7 = QPushButton("Тиснення")
filter8 = QPushButton("Ефект нерізкості")


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
v2.addWidget(filter6)
v2.addWidget(filter7)
v2.addWidget(filter8)
v3.addLayout(v2)




main_line.addLayout(v3)


photo_manager = PhotoManger()
photo_manager.image_lbl = image_lbl


def open_folder():
    photo_manager.folder = QFileDialog.getExistingDirectory()

    files = os.listdir(photo_manager.folder)

    images_list.clear()


    images_list.addItems(files)




def show_chosen_image():
    photo_manager.filename = images_list.currentItem().text()
    photo_manager.load()
    photo_manager.show_image(image_lbl)




images_list.currentRowChanged.connect(show_chosen_image)






filter1.clicked.connect(photo_manager.bw)
filter2.clicked.connect(photo_manager.rotate)
filter3.clicked.connect(photo_manager.yaskravist)
filter4.clicked.connect(photo_manager.kontrastnist)
filter5.clicked.connect(photo_manager.blur)
filter6.clicked.connect(photo_manager.contur)
filter7.clicked.connect(photo_manager.emboss)
filter8.clicked.connect(photo_manager.Unsharp)


























dir_btn.clicked.connect(open_folder)

window.setLayout(main_line)
window.show()
app.exec()