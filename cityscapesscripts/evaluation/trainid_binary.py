import os
import cv2


def trainids_to_binary(trainids_label):
    binary_label = trainids_label.copy()
    binary_label[(trainids_label>=0) * (trainids_label<=10)] = 0
    binary_label[(trainids_label>=11) * (trainids_label<=18)] = 1
    return binary_label


data_root = '../'
data_list = '../list/fine_val.txt'
list_read = open(data_list).readlines()
for index, line in enumerate(list_read):
    print("Processing {}/{}th image...".format(index+1, len(list_read)))
    line = line.strip().split(' ')
    trainids_path = os.path.join(data_root, line[1])
    trainids_label = cv2.imread(trainids_path, cv2.IMREAD_GRAYSCALE)
    binary_label = trainids_to_binary(trainids_label)
    binary_path = trainids_path.replace('TrainIds', 'TrainIdsBinary')
    cv2.imwrite(binary_path, binary_label)

