import os
import cv2
import numpy as np


mapid = [255 , 255 , 255 , 255 , 255 , 255 , 255 ,
          0 ,   1 , 255 , 255 ,   2 ,   3 ,   4 ,
          255 , 255 , 255 ,   5 , 255 ,   6 ,   7 ,
          8 ,   9 ,  10 ,  11 ,  12 ,  13 ,  14 ,  15 ,
          255 , 255 ,  16 ,  17 ,  18 ,  255];
index = np.argsort(mapid)

trainid_folder = '/mnt/yyz_data_0/users/hszhao/dev/psl/exp/cityscapes/psp50_b12_100/result/epoch_100/val/ss/gray/'
labelid_folder = '/mnt/yyz_data_0/users/hszhao/dev/psl/exp/cityscapes/psp50_b12_100/result/epoch_100/val/ss/labelid/'
if not os.path.exists(labelid_folder):
    os.mkdir(labelid_folder)

files=os.listdir(trainid_folder)
files = sorted(files)
for i, file in enumerate(files):
    print("Processing {}/{}th image, name: {}".format(i+1, len(files), file))
    trainid_name = trainid_folder + file
    labelid_name = labelid_folder + file
    trainid = cv2.imread(trainid_name, cv2.IMREAD_GRAYSCALE)
    labelid = index[trainid]
    cv2.imwrite(labelid_name, labelid)
