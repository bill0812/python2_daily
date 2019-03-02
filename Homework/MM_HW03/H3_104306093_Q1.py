from PIL import Image
import numpy,math,glob,time,colorsys
from matplotlib import pyplot as plt
def check_mode(query_image,image_search):
    if image_search.mode == "L" :
        image_search = image_search.convert("RGB")
        #print "mode is being modified~"
    elif query_image.mode == "L" :
        query_image = query_image.convert("RGB")
        #print "mode is being modified~"
    else:
        pass
        #print "mode is appropreiate~"

    pixel_query = query_image.load()
    pixel_image = image_search.load()
    return pixel_query,pixel_image
def new_memory():
    query = list()
    search = list()
    query_hist = list()
    search_hist = list()
    for length in range(3):
        query.append([])
        search.append([])
        query_hist.append([])
        search_hist.append([])
    return query,search,query_hist,search_hist
def new_memory_hsv():
    query = list()
    search = list()
    query_hist = list()
    search_hist = list()
    return query,search,query_hist,search_hist
def deal_pixel(image_list,pixel_image,width,height):
    for x in range(width):
        for y in range(height):
            #print pixel_image[x,y]
            for i in range(3):
                image_list[i].append(pixel_image[x,y][i])
def deal_pixel_hsv(image_list,pixel_image,width,height):
    for x in range(width):
        for y in range(height):
            image_list.append(colorsys.rgb_to_hsv(pixel_image[x,y][0],pixel_image[x,y][1],pixel_image[x,y][2]))
    return image_list
def deal_hist(query,search,query_hist,search_hist):
    for i in range(3):
        hist_1,bins = numpy.histogram(numpy.array(query[i]),256,[0,256])
        query_hist[i] = hist_1.tolist()
        hist_2,bins = numpy.histogram(numpy.array(search[i]),256,[0,256])
        search_hist[i] = hist_2.tolist()
def calculate(query_hist,search_hist):
    for i in range(3):
        sum_query = sum(query_hist[i])
        sum_search = sum(search_hist[i])
        for length in range(len(query_hist[i])):
            query_hist[i][length] = float(query_hist[i][length])/float(sum_query)
        for length in range(len(search_hist[i])):
            search_hist[i][length] = float(search_hist[i][length])/float(sum_search)
    return query_hist,search_hist
def calculate_hsv(img,query_list,search_list):
    distance = 0
    for i in range(len(query_list)):
        distance = distance + (( query_list[i][0] - search_list[i][0] )**2 + ( query_list[i][1] - search_list[i][1] )**2 +( query_list[i][2] - search_list[i][2] )**2)**(0.5)
    return distance
def find_hist(query_image,image_search,query_width,query_height,image_width,image_height):
    pixel_query,pixel_image = check_mode(query_image,image_search)
    query,search,query_hist,search_hist = new_memory()
    deal_pixel(query,pixel_query,query_width,query_height)
    deal_pixel(search,pixel_image,image_width,image_height)
    deal_hist(query,search,query_hist,search_hist)
    query_hist,search_hist = calculate(query_hist,search_hist)
    return query_hist, search_hist
def find_hist_hsv(query_image,image_search,query_width,query_height,image_width,image_height):
    pixel_query,pixel_image = check_mode(query_image,image_search)
    query,search,query_hist,search_hist = new_memory_hsv()
    query_list = deal_pixel_hsv(query,pixel_query,query_width,query_height)
    search_list = deal_pixel_hsv(search,pixel_image,image_width,image_height)
    return query_list,search_list
def rank(query_hist,search_hist):
    distance = 0
    for color in range(3):
        for length in range(256):
            distance = distance + ((query_hist[color][length])-(search_hist[color][length]))**2

    distance = (distance)**(0.5)
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
def Question_1_rgb(fileName,dataset,data_directory):
    test = glob.glob(dataset)
    query = fileName
    query_img = Image.open(query)
    query_width,query_height = query_img.size
    query_img = query_img.convert("RGB")
    rank_list = list()
    i = 0
    for img in test:
        #print "Processing {} picture".format(img)
        image = Image.open(img)
        image_width,image_height = image.size
        query_hist,search_hist = find_hist(query_img,image,query_width,query_height,image_width,image_height)
        rank_list.append([])
        rank_list[i].append(img)
        rank_list[i].append((rank(query_hist,search_hist)*100))
        #print "Finish {} picture,and distance is {}".format(img,rank_list[i])
        i = i+1
    return show_rank(rank_list)
def Question_1_hsv(fileName,dataset,data_directory):
    test = glob.glob(dataset)
    query = fileName
    query_img = Image.open(query)
    query_width,query_height = query_img.size
    query_img = query_img.convert("RGB")
    rank_list = list()
    i = 0
    for img in test:
        #print "Processing {} picture".format(img)
        image = Image.open(img)
        image_width,image_height = image.size
        if image_width != query_width or image_height != query_height:
            image = image.resize((query_width,query_height),Image.BILINEAR)
            image_width,image_height = image.size
        else:
            pass
        #query_hist,search_hist =
        query_list,search_list = find_hist_hsv(query_img,image,query_width,query_height,image_width,image_height)
        distance = calculate_hsv(img,query_list,search_list)
        rank_list.append([])
        rank_list[i].append(img)
        rank_list[i].append(distance)
        #print "Finish {} picture,and distance is {}".format(img,distance)
        i = i+1
    return show_rank(rank_list)
def compare(x,y,marsek_width,marsek_height,width,height,pixel_query,search_pixel):
    query,search,query_hist,search_hist = new_memory()
    for pixel_x in range(width):
        for pixel_y in range(height) :
            for i in range(3):
                query[i].append(pixel_query[x*marsek_width+pixel_x,y*marsek_height+pixel_y][i])
    deal_pixel(search,search_pixel,width,height)
    deal_hist(query,search,query_hist,search_hist)
    query_hist,search_hist = calculate(query_hist,search_hist)
    #print query_hist
    #print "=========="
    #print search_hist
    #print "=========="
    return query_hist, search_hist
def show_rank_marsek(rank_list):
    distance = list()
    final_description_dis = list()
    i = 0
    final_description = list()
    for length in range(len(rank_list)):
        distance.append(rank_list[length][1])
    distance.sort()
    del distance[1:]
    for check in range(len(rank_list)):
        if rank_list[check][1] in distance:
            final_description.append([])
            final_description[i].append(rank_list[check][0])
            final_description[i].append(rank_list[check][1])
            i = i+1
        else:
            pass
    return final_description
def replace(x,y,marsek_width,marsek_height,width,height,pixel_query,search_pixel):
    for pixel_x in range(width):
        for pixel_y in range(height):
            pixel_query[x*marsek_width+pixel_x,y*marsek_height+pixel_y] = search_pixel[pixel_x,pixel_y]
def Question_1_marsek(fileName,dataset,data_directory,cut):
    test = glob.glob(dataset)
    query = fileName
    query_img = Image.open(query)
    #if query_img.mode == "L" :
    query_img = query_img.convert("RGB")
    pixel_query = query_img.load()
    query_width,query_height = query_img.size
    marsek_width = int(query_width/int(cut)**0.5)
    marsek_width_left = int(query_width%int(cut)**0.5)
    marsek_height = int(query_height/int(cut)**0.5)
    marsek_height_left = int(query_height%int(cut)**0.5)
    #print marsek_width_left
    #print marsek_height_left
    #time.sleep(3)
    part_rank = list()
    i = 0
    for x in range((int(int(cut)**0.5))) :
        for y in range((int(int(cut)**0.5))) :
            part_rank = []
            if x == (int(int(cut)**0.5)) - 1 and marsek_width_left != 0:
                #print str(x) + " / " + str(y)
                #print "first"
                #time.sleep(3)
                i = 0
                for img in test:
                    print "Processing {} picture".format(img)
                    image = Image.open(img)
                    image = image.resize((marsek_width+marsek_width_left,marsek_height),Image.BILINEAR)
                    #if image.mode == "L" :
                    image = image.convert("RGB")
                    search_pixel = image.load()
                    query_hist,search_hist = compare(x,y,marsek_width,marsek_height,marsek_width+marsek_width_left,marsek_height,pixel_query,search_pixel)
                    part_rank.append([])
                    part_rank[i].append(img)
                    part_rank[i].append((rank(query_hist,search_hist)*100))
                    i = i + 1
                    print "Finish {} picture,and distance is {}".format(img,(rank(query_hist,search_hist)*100))

                #print show_rank_marsek(part_rank)
                #time.sleep(3)
                #print show_rank_marsek(part_rank)[0][0]
                #time.sleep(3)
                image_final = Image.open(show_rank_marsek(part_rank)[0][0])
                image_final = image.resize((marsek_width+marsek_width_left,marsek_height),Image.BILINEAR)
                #if image_final.mode == "L" :
                image_final = image_final.convert("RGB")
                final_pixel = image_final.load()
                replace(x,y,marsek_width,marsek_height,marsek_width+marsek_width_left,marsek_height,pixel_query,final_pixel)
            elif y == (int(int(cut)**0.5)) - 1 and marsek_height_left != 0:
                #print str(x) + " / " + str(y)
                #print "second"
                #time.sleep(3)
                i = 0
                for img in test:
                    print "Processing {} picture".format(img)
                    image = Image.open(img)
                    image = image.resize((marsek_width,marsek_height+marsek_height_left),Image.BILINEAR)
                    #if image.mode == "L" :
                    image = image.convert("RGB")
                    search_pixel = image.load()
                    query_hist,search_hist = compare(x,y,marsek_width,marsek_height,marsek_width,marsek_height+marsek_height_left,pixel_query,search_pixel)
                    part_rank.append([])
                    part_rank[i].append(img)
                    part_rank[i].append((rank(query_hist,search_hist)*100))
                    i = i + 1
                    print "Finish {} picture,and distance is {}".format(img,(rank(query_hist,search_hist)*100))

                #print show_rank_marsek(part_rank)
                #time.sleep(3)
                #print show_rank_marsek(part_rank)[0][0]
                #time.sleep(3)
                image_final = Image.open(show_rank_marsek(part_rank)[0][0])
                image_final = image_final.resize((marsek_width,marsek_height+marsek_height_left),Image.BILINEAR)
                #if image_final.mode == "L" :
                image_final = image_final.convert("RGB")
                final_pixel = image_final.load()
                replace(x,y,marsek_width,marsek_height,marsek_width,marsek_height+marsek_height_left,pixel_query,final_pixel)
            else :
                #print str(x) + " / " + str(y)
                #print "third"
                #time.sleep(3)
                i = 0
                for img in test:
                    print "Processing {} picture".format(img)
                    image = Image.open(img)
                    image = image.resize((marsek_width,marsek_height),Image.BILINEAR)
                    #if image.mode == "L" :
                    image = image.convert("RGB")
                    search_pixel = image.load()
                    query_hist,search_hist = compare(x,y,marsek_width,marsek_height,marsek_width,marsek_height,pixel_query,search_pixel)
                    part_rank.append([])
                    part_rank[i].append(img)
                    part_rank[i].append((rank(query_hist,search_hist)*100))
                    i = i + 1
                    print "Finish {} picture,and distance is {}".format(img,(rank(query_hist,search_hist)*100))

                #print show_rank_marsek(part_rank)
                #time.sleep(3)
                #print show_rank_marsek(part_rank)[0][0]
                #time.sleep(3)
                image_final = Image.open(show_rank_marsek(part_rank)[0][0])
                image_final = image_final.resize((marsek_width,marsek_height),Image.BILINEAR)
                #if image_final.mode == "L" :
                image_final = image_final.convert("RGB")
                final_pixel = image_final.load()
                replace(x,y,marsek_width,marsek_height,marsek_width,marsek_height,pixel_query,final_pixel)
    query_img.save("result.jpg")
    return "result.jpg"
