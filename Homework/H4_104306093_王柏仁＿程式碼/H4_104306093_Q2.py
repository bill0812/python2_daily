from PIL import Image
import numpy,math,glob,time
from scipy.fftpack import fft, dct
from matplotlib import pyplot as plt
def declar():
    query_ycbcr = list()
    image_ycbcr = list()
    for i in range(8):
        query_ycbcr.append([])
        image_ycbcr.append([])
        for j in range(8):
            query_ycbcr[i].append([])
            image_ycbcr[i].append([])
    return query_ycbcr,image_ycbcr
def represent_col(ycbcr,image,width,height):
    pixel = image.load()
    for i in range(8):
        for j in range(8):
            average_color = list()
            average_color.append(0)
            average_color.append(0)
            average_color.append(0)
            if i == 7 :
                for x in range(8+width%8):
                    for y in range(8):
                        a,b,c =  pixel[i*width+x,j*height+y]
                        average_color[0] = average_color[0] + a
                        average_color[1] = average_color[1] + b
                        average_color[2] = average_color[2] + c
                average_color[0] = average_color[0]/64
                average_color[1] = average_color[1]/64
                average_color[2] = average_color[2]/64
                ycbcr[i][j] = average_color
            elif j == 7 :
                for x in range(8):
                    for y in range(8+height%8):
                        a,b,c =  pixel[i*width+x,j*height+y]
                        average_color[0] = average_color[0] + a
                        average_color[1] = average_color[1] + b
                        average_color[2] = average_color[2] + c
                average_color[0] = average_color[0]/64
                average_color[1] = average_color[1]/64
                average_color[2] = average_color[2]/64
                ycbcr[i][j] = average_color
            else:
                count = 0
                for x in range(8):
                    for y in range(8):
                        a,b,c =  pixel[i*width+x,j*height+y]
                        count = count +1
                        average_color[0] = average_color[0] + a
                        average_color[1] = average_color[1] + b
                        average_color[2] = average_color[2] + c
                average_color[0] = average_color[0]/64
                average_color[1] = average_color[1]/64
                average_color[2] = average_color[2]/64
                ycbcr[i][j] = average_color
    return ycbcr
def printZMatrix(matrix):
        i = 0
        j = 0
        m = len(matrix)
        n = len(matrix[0])
        ret = []
        up = True
        for _ in xrange(m*n):
            ret.append(matrix[i][j])
            if up:
                if i-1<0 or j+1>=n:
                    up = False
                    if j+1>=n:  # go down
                        i += 1
                    else:  # go right
                        j += 1
                else:
                    i -= 1
                    j += 1
            else:
                if i+1>=m or j-1<0:
                    up = True
                    if i+1>=m:
                        j += 1  # go right
                    else:
                        i += 1  # go up
                else:
                    i += 1
                    j -= 1
        return ret
def zigzag(final_query,final_image):
    #print final_query[1][5][0]
    #print "======================================="
    #print final_image[1][5 ][0]
    #print "===== change ======="
    final_query_list = list()
    final_image_list = list()
    for x in range(8):
        final_query_list.append([])
        final_image_list.append([])
        for y in range(8):
            #final_query_list[x].append([])
            #final_image_list[x].append([])
            tuple_query = (final_query[x][y][0],final_query[x][y][1],final_query[x][y][2])
            tuple_image = (final_image[x][y][0],final_image[x][y][1],final_image[x][y][2])
            #print tuple_query
            #print "\n"
            #print tuple_image
            final_query_list[x].append(tuple_query)
            final_image_list[x].append(tuple_image)
    #print final_query_list[1]
    #print "\n"
    #print final_image_list[1]
    #print "======================================="
    final_query_answer = printZMatrix(final_query_list)
    final_image_answer = printZMatrix(final_image_list)
    #print final_query_answer
    #print "\n"
    #print final_image_answer
    return final_query_answer,final_image_answer
def calculate(final_query_answer,final_image_answer):
    distance1 = 0;
    distance2 = 0;
    distance3 = 0;
    #print final_query_answer
    #print final_image_answer
    for x in range(64):
        #print final_query_answer[x][0]
        #print final_image_answer[x]
        #print "=====================-"
        #print final_query_answer[x]
        a,b,c = final_query_answer[x]
        a1,b1,c1 = final_image_answer[x]
        distance1 = distance1 + (a - a1)**2
        distance2 = distance2 + (b - b1)**2
        distance3 = distance3 + (c - c1)**2
        #print distance3
    distance = distance1**0.5 + distance2**0.5 + distance3**0.5
    return distance
def partition_dct_zigzag(query_img,image,query_width,query_height,image_width,image_height):
    query_ycbcr,image_ycbcr = declar()
    x = 0
    every_query_width = query_width/8
    every_query_height = query_height/8
    every_image_width = image_width/8
    every_image_height = image_height/8
    query_ycbcr = represent_col(query_ycbcr,query_img,every_query_width,every_query_height)
    image_ycbcr = represent_col(image_ycbcr,image,every_image_width,every_image_height)
    final_query = dct(query_ycbcr, type=2, n=None, axis=-1, norm=None, overwrite_x=False)
    final_image = dct(image_ycbcr, type=2, n=None, axis=-1, norm=None, overwrite_x=False)
    final_query_answer,final_image_answer = zigzag(final_query,final_image)
    #print final_query_answer
    #print "\n"
    #print final_image_answer
    distance = calculate(final_query_answer,final_image_answer)
    return distance
def show_rank(rank_list):
    distance = list()
    final_description_dis = list()
    i = 0
    final_description = list()
    for length in range(len(rank_list)):
        distance.append(rank_list[length][1])
    distance.sort()
    del distance[10:]
    for check in range(len(rank_list)):
        if rank_list[check][1] in distance:
            final_description.append([])
            final_description[i].append(rank_list[check][0])
            final_description[i].append(rank_list[check][1])
            i = i+1
        else:
            pass
    return sorted(final_description,key=lambda x:x[1])
def Question_2(fileName,dataset,data_directory):
    test = glob.glob(dataset)
    test_image = "dataset/ukbench00001.jpg"
    query = fileName
    query_img = Image.open(query)
    query_img = query_img.convert("YCbCr")
    query_width,query_height = query_img.size
    rank_list = list()
    i = 0
    for img in test:
        #print "Processing {} picture".format(img)
        image = Image.open(img)
        image_width,image_height = image.size
        image = image.convert("YCbCr")
        distance = partition_dct_zigzag(query_img,image,query_width,query_height,image_width,image_height)
        rank_list.append([])
        rank_list[i].append(img)
        rank_list[i].append(distance)
        #print "Finish {} picture,and distance is {}".format(img,distance)
        i = i + 1
    return show_rank(rank_list)
