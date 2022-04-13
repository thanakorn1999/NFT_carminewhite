import os
import json
import random
from os import walk
import shutil
from PIL import Image


def isExist_create_dir(paths):
    for path in paths:
        if os.path.isdir(path) :
            pass
        else :
            os.mkdir(path)
            print("create :",path)


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

def add_images(images_main ,images_add):
    images_main=Image.open("images_main")
    for add in images_add:
        add_on =Image.open("images_add")

        images_main=Image.alpha_composite(images_main,add_on) #intermediate

    images_main.save(images_main)

def run(main_path,result,images_combile):

    main_path_images =main_path+"images//"
    main_path_json = main_path+"json//"
    result_images = result+"images//"
    
    isExist_create_dir([main_path_images ,main_path_json ,result_images ])

    name_files_json = get_namefile_in(main_path_json)

    for name_json in (name_files_json):
        
        print("working on :",main_path_json+name_json)
        
        data_json = read_json(main_path_json+name_json)
        
        if(next(item for item in data_json["attributes"] if item["trait_type"] == "Hair")['value']) == "Orc Haiasdr" :
            print("name : ",name_json)
            name_images = name_json.split(".")[0]+".png"
            shutil.copyfile(main_path_images+name_images, result_images+name_images)

            add_images(result_images+name_images,images_combile)



    # for i in range(5000):

# - - - - - - - setting - - - - - - - - #
# root
project =".\\aunt_add_hair\\"

main_path = project + "clone_workspace\\"
result   = project + "result\\"

isExist_create_dir([project,main_path ,result])


images_combile =["project"+"hair.png"]
# -  -  -  -  -  -  -  -  -  -  - -  -  -# 



run(main_path,result,images_combile)