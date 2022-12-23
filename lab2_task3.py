import os
import shutil
from random import randint
import csv
import _csv


"""
Написать скрипт, создающий копию датасета таким образом, чтобы каждый файл из сходного датасета получил случайный
номер от 0 до 10000, и датасет представлял собой следующую структуру dataset/номер.jpg. Для того чтобы осталась
возможность определить принадлежность экземпляра к классу создать файл-аннотацию (как в пункте 1).
"""


def dataset_random(class_label: str, source: str, destination: str, file: '_csv.writer') -> None:
    """Принимает метку класса, путь к новой директории, открытый для дозаписи csv-файл, копирует файлы в новую
    директорию, записывает данные в csv-файл"""
    source = f"{source}/{class_label}"
    for i in os.listdir(source):
        if i.find('.jpg') != -1:
            name = randint(0, 10001)
            while os.path.isfile(f"{destination}/{name}.jpg"):
                name = randint(0, 10001)
            shutil.copy(f"{source}/{i}", f"{destination}/{name}.jpg")
            file.writerow({
                "Absolute path": f"{os.path.abspath(f'{destination}/{name}.jpg')}",
                "Relative path": f"{os.path.relpath(f'{destination}/{name}.jpg', start='..')}",
                "Class label": class_label
            })


def create_csv(name: str) -> '_csv.writer':
    """Создает csv-файл и устанавливает значения столбцов"""
    file = open(f"{name}.csv", "a+")
    columns = ["Absolute path", "Relative path", "Class label"]
    created_csv = csv.DictWriter(file, lineterminator="\r", fieldnames=columns)
    created_csv.writeheader()
    return created_csv


def task3(source: str, destination: str) -> None:
    if os.path.isdir(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    current = os.getcwd()
    os.chdir(destination)
    if os.path.isfile('annotation.csv'):
        os.remove('annotation.csv')
    file = create_csv('annotation')
    os.chdir(current)
    dataset_random("cat", source, destination, file)
    dataset_random("dog", source, destination, file)


if __name__ == "__main__":
    dirname = "dataset-task3"
    if os.path.isdir(dirname):
        shutil.rmtree(dirname)
    os.mkdir(dirname)
    dest = os.path.abspath(dirname)
    if os.path.isfile(f"{dirname}/annotation.csv"):
        os.remove(f"{dirname}/annotation.csv")
    os.chdir(dest)
    csv_file = create_csv('annotation')
    os.chdir("..")
    dataset_random("cat", f"{os.getcwd()}/dataset", dest, csv_file)
    dataset_random("dog", f"{os.getcwd()}/dataset", dest, csv_file)
