import os
import sys
from lab2_Iterator import Iterator
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('icon.jpeg'))
        self.folder_path = QFileDialog.getExistingDirectory(self, 'Select dataset folder')
        while not os.path.isdir(f"{self.folder_path}/cat") or not os.path.isdir(f"{self.folder_path}/dog"):
            self.folder_path = QFileDialog.getExistingDirectory(self, 'Select dataset folder')
        self.cat_iterator = Iterator(f"{self.folder_path}/cat")
        self.dog_iterator = Iterator(f"{self.folder_path}/dog")
        self.button_next_cat = QPushButton('Следующая кошка', self)
        self.button_next_dog = QPushButton('Следующая собака', self)
        self.button_task_1 = QPushButton('csv-файл', self)
        self.button_task_2 = QPushButton('Задание 2', self)
        self.button_task_3 = QPushButton('Задание 3', self)
        self.open_file = QAction('Open', self)
        self.map_cat = QLabel(self)
        self.map_dog = QLabel(self)
        self.grid = QGridLayout(self)
        self.menubar = self.menuBar()
        self.file_menu = self.menubar.addMenu('&File')

        self.init_ui()

    def init_ui(self):
        self.setGeometry(360, 190, 1200, 700)
        self.setWindowTitle("Lab3")

        self.map_cat.setPixmap(QPixmap(next(self.cat_iterator)))
        self.map_cat.setScaledContents(True)
        self.map_cat.setGeometry(5, 5, 590, 490)
        self.grid.addWidget(self.map_cat)

        self.map_dog.setPixmap(QPixmap(next(self.dog_iterator)))
        self.map_dog.setScaledContents(True)
        self.map_dog.setGeometry(605, 5, 590, 490)
        self.grid.addWidget(self.map_dog)

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

        self.open_file.setShortcut('Ctrl+O')
        self.open_file.setStatusTip('Open new File')
        self.open_file.triggered.connect(self.show_dialog)

        self.file_menu.addAction(self.open_file)

        self.show()

    def next_cat(self):
        self.map_cat.setPixmap(QPixmap(next(self.cat_iterator)))

    def next_dog(self):
        self.map_dog.setPixmap(QPixmap(next(self.dog_iterator)))

    def task1(self):
        filename = QFileDialog.getSaveFileName(self, "Напишите название файла", filter=".csv")
        task1(filename[0], self.folder_path)

    def task2(self):
        directory = QFileDialog.getExistingDirectory(self, "Выберите новую директорию")
        task2(self.folder_path, directory)

    def task3(self):
        directory = QFileDialog.getExistingDirectory(self, "Выберите новую директорию")
        task3(self.folder_path, directory)

    def show_dialog(self):
        self.folder_path = QFileDialog.getExistingDirectory(self, 'Open file')
        while not os.path.isdir(f"{self.folder_path}/cat") or not os.path.isdir(f"{self.folder_path}/dog"):
            self.folder_path = QFileDialog.getExistingDirectory(self, 'Select dataset folder')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
