import os
os.environ['CITYSCAPES_DATASET'] = '/mnt/yyz_data_0/users/hszhao/dataset/cityscapes/'
os.environ['CITYSCAPES_RESULTS'] = '/mnt/yyz_data_0/users/hszhao/dev/psl/exp/cityscapes/psp50_b12_100/result/epoch_100/val/ss/labelid/'

#import evalPixelLevelSemanticLabeling
os.system('python2 evalPixelLevelSemanticLabeling.py')
