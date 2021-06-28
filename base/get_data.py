import os

def read_txt(filename):
    with open(os.getcwd()+os.sep+"data"+os.sep+filename, "r", encoding="utf-8")as f:
        arrs = []
        for i in f.readlines():
            arrs.append(tuple(i.strip().split(",")))
        return arrs

def read_line(filename, start=0, end=100):
    with open(os.getcwd()+os.sep+"data"+os.sep+filename, "r", encoding="utf-8")as f:
        arrs = []
        for i in f.readlines()[start:end]:
            arrs.append(tuple(i.strip().split(",")))
        return arrs


def read_txt_1():
    with open("../data/information.txt", "r", encoding="utf-8")as f:
        arrs = []
        for i in f.readlines()[10:]:
            arrs.append(tuple(i.strip().split(",")))
        return arrs


if __name__ == '__main__':
    print(read_txt_1())