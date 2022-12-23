import shutil
import os
import csv


"""
Написать скрипт для копирования датасета в другую директорию таким образом, чтобы имена файлов содержали имя класса
и его порядковый номер. То есть из dataset/class/0000.jpg должно получиться dataset/class_0000.jpg. Для того чтобы
осталась возможность определить принадлежность экземпляра к классу создать файл-аннотацию (как в пункте 1).
"""


def dataset_copy(class_label: str, source: str, destination: str) -> None:
    """Принимает метку класса, путь к новой директории, копирует файлы в новую директорию"""
    source = f"{source}/{class_label}"
    for i in os.listdir(source):
        shutil.copy(f"{source}\\{i}", f"{destination}\\{class_label}_{i}")


def get_csv(destination: str) -> None:
    """Принимает путь к новой директории, записывает информацию по фото из этой директории в csv-файл """
    os.chdir(destination)
    if os.path.isfile("annotation.csv"):
        os.remove("annotation.csv")
    csv_file = create_csv('annotation')
    for i in os.listdir(destination):
        if i.find(".jpg") != -1:
            class_label = (i.split("_"))[0]
            csv_file.writerow({
                "Absolute path": f"{os.path.abspath(i)}",
                "Relative path": f"{os.path.relpath(i, start='..')}",
                "Class label": class_label
            })


def task2(src: str, destination: str) -> None:
    """Функция для 3-й лабораторной работы"""
    if os.path.isdir(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    dataset_copy("cat", src, destination)
    dataset_copy("dog", src, destination)
    get_csv(destination)


def create_csv(name: str) -> '_csv.writer':
    """Создает csv-файл и устанавливает значения столбцов"""
    file = open(f"{name}.csv", "a+")
    columns = ["Absolute path", "Relative path", "Class label"]
    created_csv = csv.DictWriter(file, lineterminator="\r", fieldnames=columns)
    created_csv.writeheader()
    return created_csv


if __name__ == "__main__":
    dirname = "dataset-task2"
    if not os.path.isdir(dirname):
        os.mkdir(dirname)
    else:
        shutil.rmtree(dirname)
        os.mkdir(dirname)
    dest = os.path.abspath(dirname)
    dataset_copy("cat", f"{os.getcwd()}/dataset", dest)
    dataset_copy("dog", f"{os.getcwd()}/dataset", dest)
    get_csv(dest)
