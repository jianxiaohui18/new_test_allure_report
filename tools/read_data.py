import os

import yaml

from config import filepath


def readdata(datafile):
    arr = []
    with open(filepath+ os.sep + "data" + os.sep +datafile,"r",encoding="utf-8")as f:
        for data in yaml.safe_load(f).values():
            arr.append(tuple(data.values()))
        return arr



if __name__ == '__main__':
    readdata("login.yaml")