import os
import json
import random
from os import walk


# - - - - - - - setting - - - - - - - - #
main_path = ".\\clone_workspace\\"
need_to_combile = ["aunt\\","ape\\","max\\"]

result_images   = ".\\result\\images\\"
result_metadata = ".\\result\\metadata\\"
file_metadata   = ".\\test_metadata.json"
# -  -  -  -  -  -  -  -  -  -  - -  -  -#


def read_json(file_name):
        f = open(file_name)
        data = json.load(f)
        f.close()
        return data


def write_json(file_name ,message):
    with open(file_name ,'w') as outfile:
        json.dump(message ,outfile)


def run(need_to_combile ,main_path ,result_images ,result_metadata ,file_metadata):

    metadata_array=[]

    for i in range(5000):
        select = random.randint(0, 2)
        os.rename(main_path+need_to_combile[select] + "images\\"+ str(i)+".png", result_images + str(i) + ".png")
        # os.rename(main_path+need_to_combile[select] + "json\\" + str(i)+".json", result_metadata + str(i) + ".json")
        data = read_json(main_path +need_to_combile[select] +"json\\" +str(i) +".json")
        metadata_array.append(data)

    write_json(file_metadata, metadata_array)


run()