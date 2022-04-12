import sys    
import os    
import json
import random
from os import walk
import shutil
from turtle import position
from PIL import Image
from sys import exit

from tools import *
file_name =  os.path.basename(sys.argv[0])
file_name=file_name.split(".")[0]





def add_images(images_main ,images_add):
    images_main=Image.open("images_main")
    for add in images_add:
        add_on =Image.open("images_add")

        images_main=Image.alpha_composite(images_main,add_on) #intermediate

    images_main.save(images_main)



def find_number_tag(name):
    number =name.split("\\")[-1]
    number = int(number.split(".")[0])
    print(number)

    position_1000 = int(number/1000)
    position_0100 = int((number%1000)/100)
    position_0010 = int((number%100)/10)
    position_0001 = int(number%10)

    return [position_1000,position_0100,position_0010,position_0001]



def run(main_path_workspace ,result_path ,images_combile ):

    main_path_images =main_path_workspace+"images//"
    result_images = result_path+"images//"
    
    isExist_create_dir([main_path_images ,result_images ])


    images_main_path = get_namefile_in(main_path_images)

    find_number_tag(name)
    



    for name_json in (name_files_json):
        
        print("working on :",main_path_json+name_json)
        data_json = read_json(main_path_json+name_json)
        




        if(next(item for item in data_json["attributes"] if item["trait_type"] == "Hair")['value']) == "Orc Haiasdr" :
            print("name : ",name_json)
            name_images = name_json.split(".")[0]+".png"
            shutil.copyfile(main_path_images+name_images, result_images+name_images)
            add_images(result_images+name_images,images_combile)



# # - - - - - - - setting - - - - - - - - #
# # root
# project =".\\"+file_name+"\\"
# main_path_workspace = project + "clone_workspace\\"
# result_path   = project + "result\\"

# isExist_create_dir([project,main_path_workspace ,result_path])

# # images_combile =["project"+"hair.png"]

# tag ="main_path_workspace\\tax.png"

# floder_images =["num_000x\\" ,"num_00x0\\" ,"num_0x00\\" ,"num_x000\\" ]

# images_combile=[]

# for index_folder,name in enumerate(floder_images):
#     images_combile.append([])
#     for i in range(10):
#         # print(name+str(i)+".png")
#         file_images = main_path_workspace+name+str(i)+".png"

#         if file_isExist(file_images):
#             images_combile[index_folder].append(file_images)
#         else :
#             exit()

# images_combile.append(tag)

# # # -  -  -  -  -  -  -  -  -  -  - -  -  -# 

# run(main_path_workspace ,result_path ,images_combile )
