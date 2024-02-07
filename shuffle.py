import os
import random
import shutil

road_root = "D:/DL_datasets/Road Detection/images"
img_images_path = "D:/DL_datasets/Road Detection/images"
img_annot_path = "D:/DL_datasets/Road Detection/annotations"

xml_ = '.xml'
img_ = '.png'

file_list = [file for file in os.listdir(road_root) if file.endswith(".xml")]

for i in file_list:
    print(i)

random.shuffle(file_list)

test_ratio = 0.2

test_list = file_list[:int(len(file_list)* test_ratio)]
train_list = file_list[int(len(file_list)* test_ratio):]

print(len(test_list), len(train_list))

for i in test_list:
    f_name = os.path.splitext(i)[0]
    shutil.copyfile(os.path.join(road_root, (f_name + img_)), os.path.join(img_images_path, 'valid/', (f_name+img_)))
    shutil.copyfile(os.path.join(road_root, (f_name + xml_)), os.path.join(img_annot_path, 'valid/', (f_name + xml_)))

for i in train_list:
    f_name = os.path.splitext(i)[0]
    shutil.copyfile(os.path.join(road_root, (f_name + img_)), os.path.join(img_images_path, 'train/', (f_name+img_)))
    shutil.copyfile(os.path.join(road_root, (f_name + xml_)), os.path.join(img_annot_path, 'train/', (f_name + xml_)))