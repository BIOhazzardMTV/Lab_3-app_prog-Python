import _csv
import csv
import os


"""
Написать скрипт для формирования текстового файла-аннотации собранного датасета. Файл-аннотация должен представлять
собой csv-файл, в котором в первой колонке будет указан абсолютный путь к файлу, во второй колонке относительный путь
относительно вашего Python-проекта, третья колонка будет содержать текстовое название класса (метку класса), к которому
относится данный экземпляр.
"""


def get_csv(file: '_csv.writer', label: str) -> None:
    """Принимает открытый для дозаписи csv-файл и метку класса, записывает в csv-файл данные"""
    for i in os.listdir(label):
        if i.find(".jpg") != -1:
            file.writerow({
             "Absolute path": f"{label}/{i}",
             "Relative path": f"{os.path.relpath(f'{label}/{i}', start='../..')}",
             "Class label": f"{os.path.basename(label)}"
            })


def create_csv(name: str) -> '_csv.writer':
    """Создает csv-файл и устанавливает значения столбцов"""
    file = open(f"{name}.csv", "a+")
    columns = ["Absolute path", "Relative path", "Class label"]
    created_csv = csv.DictWriter(file, lineterminator="\r", fieldnames=columns)
    created_csv.writeheader()
    return created_csv


def task1(filename: str, path: str) -> None:
    """Функция для 3-й лабораторной работы"""
    if os.path.isfile(f"{filename}.csv"):
        os.remove(f"{filename}.csv")
    file = create_csv(filename)
    get_csv(file, f"{path}/cat")
    get_csv(file, f"{path}/dog")


if __name__ == "__main__":
    csv_file = create_csv('annotation')
    get_csv(csv_file, f"{os.getcwd()}/dataset/cat")
    get_csv(csv_file, f"{os.getcwd()}/dataset/dog")
