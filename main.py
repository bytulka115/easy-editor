from PyQt6.QtWidgets import *

app = QApplication([])
window = QWidget()



dir_btn = QPushButton("папка")
HorizontalLine = QHBoxLayout()
image_lbl = QLabel("картинки")
images_list = QListWidget()

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








window.setLayout(main_line)
window.show()
app.exec()