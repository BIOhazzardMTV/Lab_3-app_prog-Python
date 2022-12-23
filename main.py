import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_next_cat = QPushButton('Следующая кошка', self)
        self.button_next_dog = QPushButton('Следующая собака', self)
        self.button_task_1 = QPushButton('csv-файл', self)
        self.button_task_2 = QPushButton('Задание 2', self)
        self.button_task_3 = QPushButton('Задание 3', self)
        self.init_ui()

    def init_ui(self):
        self.setGeometry(360, 190, 1200, 700)
        self.setWindowTitle("Lab3")
        self.button_next_cat.setGeometry(225, 515, 140, 40)
        self.button_next_cat.setToolTip("Переход к следующему изображению кошки из датасета")
        self.button_next_cat.clicked.connect(self.next_cat)

        self.button_next_dog.setGeometry(835, 515, 140, 40)
        self.button_next_dog.setToolTip("Переход к следующему изображению собаки из датасета")
        self.button_next_dog.clicked.connect(self.next_dog)

        self.button_task_1.setGeometry(15, 620, 140, 40)
        self.button_task_1.setToolTip("Создание файла-аннотации для текущего датасета")
        self.button_task_1.clicked.connect(self.task1)

        self.button_task_2.setGeometry(170, 620, 140, 40)
        self.button_task_2.setToolTip("Создание датасета с организацией файлов, согласно заданию 2 варианта 3")
        self.button_task_2.clicked.connect(self.task2)

        self.button_task_3.setGeometry(325, 620, 140, 40)
        self.button_task_3.setToolTip("Создание датасета с организацией файлов, согласно заданию 3 варианта 3")
        self.button_task_3.clicked.connect(self.task3)

        self.show()

    def next_cat(self):
        pass

    def next_dog(self):
        pass

    def task1(self):
        pass

    def task2(self):
        pass

    def task3(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
