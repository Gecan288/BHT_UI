import os


def read_txt(filename):
    with open(os.getcwd()+os.sep+"data"+os.sep+filename, "r", encoding="utf-8")as f:
        array = list()
        for i in f.readlines():
            array.append(tuple(i.strip().split(",")))
        return array


def read_line(filename, start=0, end=100):
    with open(os.getcwd()+os.sep+"data"+os.sep+filename, "r", encoding="utf-8")as f:
        array = list()
        for i in f.readlines()[start:end]:
            array.append(tuple(i.strip().split(",")))
        return array


def test_txt():
    with open("../data/information.txt", "r", encoding="utf-8")as f:
        array = list()
        for i in f.readlines()[8:]:
            array.append(tuple(i.strip().split(",")))
        return array


if __name__ == '__main__':
    print(test_txt())
