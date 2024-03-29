import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

sets=[('train'), ('valid')]

classes = ['C'] #modify the class name

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
wd = getcwd()

def convert_annotation(image_id, image_set):
    # in_file = ('olive/olive%s/Annotations/%s.xml' % (year, image_id))
    # out_file = open('olive/olive%s/labels/%s.txt' % (year, image_id), 'w')
    in_file = ('annotations/'+ image_set +'/%s.xml' % (image_id))
    out_file = open('labels/'+ image_set +'/%s.txt' % (image_id), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')



img_path = 'images/'

for image_set in sets:
    if not os.path.exists('labels/'+ image_set):
        os.makedirs('labels/' + image_set)
    image_ids = os.listdir(img_path + image_set)

  #  list_file = open('%s.txt' % (image_set), 'w')
    for image_id in image_ids:
        image_name = os.path.splitext(image_id)[0]
        convert_annotation(image_name, image_set)


# for image_set in sets:
#     if not os.path.exists('olive/olive%s/labels/' % (year)):
#         os.makedirs('olive/olive%s/labels/'% (year) )
#     image_ids = open('olive/olive%s/ImageSets/Main/%s.txt' % (year, image_set)).read().strip().split()
#     list_file = open('%s_%s.txt' % (year, image_set), 'w')
#     for image_id in image_ids:
#         list_file.write('%s/olive/olive%s/Images/%s.png\n' % (wd, year, image_id))
#         convert_annotation(year, image_id)
#     list_file.close()

