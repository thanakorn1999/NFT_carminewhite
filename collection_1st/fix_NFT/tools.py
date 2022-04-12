import os
import json
from os import walk
from PIL import Image
from pathlib import Path

# from tools import *
# displayText()


def isExist_create_dir(paths):
    for path in paths:
        if os.path.isdir(path) :
            pass
        else :
            os.mkdir(path)
            print("create :",path)

def file_isExist(path_file):
    if Path('filename.txt').is_file():
        # print ("File exist")
        return True
    else:
        print (path_file," File not exist!!")
        return False


def get_namefile_in(main_path):
    f = []
    for (dirpath, dirnames, filenames) in walk(main_path):
        f.extend(filenames)
        break
    return f


def read_json(file_name):
        f = open(file_name)
        data = json.load(f)
        f.close()
        return data


def write_json(file_name ,message):
    with open(file_name ,'w') as outfile:
        json.dump(message ,outfile)
