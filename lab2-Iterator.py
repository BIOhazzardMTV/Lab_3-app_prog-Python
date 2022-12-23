import csv
import os.path


class Iterator:
    """"""
    def __init__(self, path):
        self.counter = 0
        self.data = []
        for i in os.listdir(f"{path}/"):
            self.data.append(os.path.abspath(f"{path}/{i}"))
        self.limit = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            i = self.counter
            self.counter += 1
            return self.data[i]
        else:
            raise StopIteration

    def get_limit(self):
        return self.limit


if __name__ == "__main__":
    os.chdir("dataset")
    iterator = Iterator(f"{os.getcwd()}/cat")
    for i in range(0, iterator.get_limit()):
        print(next(iterator))
