import sift
from PIL import Image
import math,glob,time
from numpy import array
import numpy
from matplotlib import pyplot as plt
def Question_3(fileName,dataset,data_directory):
    test = glob.glob(dataset)
    query = fileName
    final_list = list()
    i = 0
    j = 0
    for img in test:
        image = array(Image.open(img).convert('L'))
        sift.process_image(img,"sift_file/"+data_directory+"/"+img[-16:] + '.sift')
        #sift_spot = sift.read_features_from_file('sift_file/'+data_directory+"/"+img[-16:] + '.sift')
        #if sift_spot == "none":
        #    pass
        #else:
        #    sift_final = sift_spot.tolist()
        #if sift_spot == "none":
        #    final_list.append([])
        #else:
        #    if isinstance(sift_final[0],list):
        #        for x in range(len(sift_final)):
        #            final_list.append(sift_final[x])
        #    else:
        #        final_list.append(sift_final)
    #return final_list
