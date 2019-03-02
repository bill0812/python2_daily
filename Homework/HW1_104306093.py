#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 14:14:48 2017

@author: wangboren
"""

def Q1(string,width,height):
    Q1_pic = Image.open(string)
    pixel = Q1_pic.load()
    for i in range(width):
        for j in range(height):
            R,G,B = pixel[i,j]
            if i < width/3:
                pixel[i,j] = (3*R,G,B)
            if i > width/3 and i < width*2/3:
                pixel[i,j] = (R,3*G,B)
            if i < width and i > width*2/3:
                pixel[i,j] = (R,G,3*B)
    Q1_pic.save("Q1.jpg")

def Q2(string,width,height):
    Q2_pic = Image.open(string).convert("CMYK")
    pixel = Q2_pic.load()
    for i in range(width):
        for j in range(height):
            C,M,Y,K = pixel[i,j]
            if i < width/4:
                pixel[i,j] = (3*C,M,Y,K)
            if i > width/4 and i < width*2/4:
                pixel[i,j] = (C,3*M,Y,K)
            if i < width*3/4 and i > width*2/4:
                pixel[i,j] = (C,M,3*Y,K)
            if i < width and i > width*3/4:
                pixel[i,j] = (C,M,Y,3*K)

    Q2_pic.save("Q2.jpg")

def Q3(string,width,height):
    Q3_pic = Image.open(string)
    pixel = Q3_pic.load()
    for i in range(width):
        for j in range(height):
            R,G,B = pixel[i,j]
            pixel[i,j] = (255-R,255-G,255-B)

    Q3_pic.save("Q3.jpg")

def Q4(string,width,height):
    Q4_pic = Image.open(string)
    pixel = Q4_pic.load()
    for i in range(0,width,8):
        for j in range(0,height,8):
            R,G,B =  pixel[i,j]
            for dotx in range(8):
                for doty in range(8):
                    pixel[i+dotx,j+doty] = (R,G,B)

    Q4_pic.save("Q4.jpg")

def Q5_1(string,width,height):
    Q5_1_pic = Image.open(string)
    pixel = Q5_1_pic.load()
    for i in range(width):
        for j in range(height):
            R,G,B =  pixel[i,j]
            pixel[i,j] = (((R+G+B)/3),((R+G+B)/3),((R+G+B)/3))

    Q5_1_pic.save("Q5-1.jpg")

def Q5_2(string,width,height):
    Q5_2_pic = Image.open(string)
    pixel = Q5_2_pic.load()
    for i in range(width):
        for j in range(height):
            R,G,B =  pixel[i,j]
            R = int(0.299*R+0.587*G+0.114*B)
            G = int(0.299*R+0.587*G+0.114*B)
            B = int(0.299*R+0.587*G+0.114*B)
            pixel[i,j] = (R,G,B)

    Q5_2_pic.save("Q5-2.jpg")

def Q6_1(string,width,height):
    Q6_1_pic = Image.open(string)
    pixel = Q6_1_pic.load()
    for i in range(width):
        for j in range(height):
            R,G,B =  pixel[i,j]
            if (int(R+G+B)/3) < 180:
                pixel[i,j] = (0,0,0)
            elif (int(R+G+B)/3) >= 180:
                pixel[i,j] = (255,255,255)
    Q6_1_pic.save("Q6-1.jpg")

def Q6_2(string,width,height):
    Q6_2_pic = Image.open(string)
    pixel = Q6_2_pic.load()
    for i in range(width):
        for j in range(height):
            R,G,B =  pixel[i,j]
            if (int(R+G+B)/3) < 64:
                pixel[i,j] = (0,0,0)
            elif (int(R+G+B)/3) >= 64:
                pixel[i,j] = (255,255,255)
    Q6_2_pic.save("Q6-2.jpg")

def Q6_3(string,width,height):
    Q6_3_pic = Image.open(string)
    pixel = Q6_3_pic.load()
    for i in range(width):
        for j in range(height):
            R,G,B =  pixel[i,j]
            if (int(R+G+B)/3) < 20:
                pixel[i,j] = (0,0,0)
            elif (int(R+G+B)/3) >= 20:
                pixel[i,j] = (255,255,255)
    Q6_3_pic.save("Q6-3.jpg")

def Q7_1(string,width,height):
    Q7_1_pic = Image.open(string)
    pixel = Q7_1_pic.load()
    for i in range(width):
        for j in range(height):
            R,G,B =  pixel[i,j]
            pixel[i,j] = (R,B,G)
    Q7_1_pic.save("Q7-1.jpg")

def Q7_2(string,width,height):
    Q7_2_pic = Image.open(string)
    pixel = Q7_2_pic.load()
    for i in range(width):
        for j in range(height):
            R,G,B =  pixel[i,j]
            pixel[i,j] = (G,R,B)
    Q7_2_pic.save("Q7-2.jpg")

def Q7_3(string,width,height):
    Q7_3_pic = Image.open(string)
    pixel = Q7_3_pic.load()
    for i in range(width):
        for j in range(height):
            R,G,B =  pixel[i,j]
            pixel[i,j] = (G,B,R)
    Q7_3_pic.save("Q7-3.jpg")

def Q7_4(string,width,height):
    Q7_4_pic = Image.open(string)
    pixel = Q7_4_pic.load()
    for i in range(width):
        for j in range(height):
            R,G,B =  pixel[i,j]
            pixel[i,j] = (B,R,G)
    Q7_4_pic.save("Q7-4.jpg")

def Q7_5(string,width,height):
    Q7_5_pic = Image.open(string)
    pixel = Q7_5_pic.load()
    for i in range(width):
        for j in range(height):
            R,G,B =  pixel[i,j]
            pixel[i,j] = (B,G,R)
    Q7_5_pic.save("Q7-5.jpg")

def Q8(string,width,height):
    Q8_pic = Image.open(string)
    pixel = Q8_pic.load()
    simular = int()
    for i in range(width):
        for j in range(height):
            R,G,B =  pixel[i,j]
            simular = ((255-R)**2+(190-G)**2+(25-B)**2)**0.5
            if simular < 100:
                pixel[i,j] = (R,int(0.6*G),B)
            else:
                pixel[i,j] = (R,G,B)
    Q8_pic.save("Q8.jpg")

def Q9(string,width,height):
    Q9_pic = Image.open(string)
    pixel = Q9_pic.load()
    this = int()
    this_next = int()
    this_below = int()
    minus_next = int()
    minus_below = int()
    for i in range(width):
        for j in range(height):
            R,G,B =  pixel[i,j]
            if i == (width-1):
                if j != (height-1):
                    R2,G2,B2 = pixel[i,j+1]
                    this = (R+G+B)/3
                    this_below = (R2+G2+B2)/3
                    minus_below = int(abs(this- this_below))
                    if minus_below > 10 :
                        pixel[i,j] = (0,0,0)
                    else:
                        pixel[i,j] = (255,255,255)
                else:
                    pixel[i,j] = (0,0,0)
            elif j == (height-1):
                R1,G1,B1 = pixel[i+1,j]
                this = (R+G+B)/3
                this_next = (R1+G1+B1)/3
                minus_next = int(abs(this-this_next))
                if minus_next > 10:
                    pixel[i,j] = (0,0,0)
                else:
                    pixel[i,j] = (255,255,255)
            else:
                R1,G1,B1 = pixel[i+1,j]
                R2,G2,B2 = pixel[i,j+1]
                this = (R+G+B)/3
                this_next = (R1+G1+B1)/3
                this_below = (R2+G2+B2)/3
                minus_next = int(abs(this-this_next))
                minus_below = int(abs(this- this_below))
                if minus_below > 10 and minus_next > 10:
                    pixel[i,j] = (0,0,0)
                else:
                    pixel[i,j] = (255,255,255)
    Q9_pic.save("Q9.jpg")

def Q10(string,width,height):
    Q10_pic = Image.open(string)
    pixel = Q10_pic.load()

    for i in range(width):
        for j in range(height):
            block = list()
            if i == 0 or i == width-1:
                if i == 0  and j == 0:
                    R,G,B = pixel[i,j]
                    R_5,G_5,B_5 = pixel[i,j+1]
                    R_7,G_7,B_7 = pixel[i+1,j]
                    R_8,G_8,B_8 = pixel[i+1,j+1]
                    block.append((R_5+G_5+B_5)/3)
                    block.append((R_7+G_7+B_7)/3)
                    block.append((R_8+G_8+B_8)/3)
                    block.append((R+G+B)/3)
                    block.sort()
                    if (block[1]+block[2])/2 == (R_5+G_5+B_5)/3:
                        pixel[i,j]= (R_5,G_5,B_5)
                    elif (block[2]+block[1])/2 == (R_7+G_7+B_7)/3:
                        pixel[i,j]= (R_7,G_7,B_7);
                    elif (block[2]+block[1])/2 == (R_8+G_8+B_8)/3:
                        pixel[i,j]= (R_8,G_8,B_8);
                    elif (block[2]+block[1])/2 == (R+G+B)/3:
                        pixel[i,j]= (R,G,B);
                elif i == 0  and j == height-1:
                    R,G,B = pixel[i,j]
                    R_5,G_5,B_5 = pixel[i,j-1]
                    R_7,G_7,B_7 = pixel[i+1,j]
                    R_8,G_8,B_8 = pixel[i+1,j-1]
                    block.append((R_5+G_5+B_5)/3)
                    block.append((R_7+G_7+B_7)/3)
                    block.append((R_8+G_8+B_8)/3)
                    block.append((R+G+B)/3)
                    block.sort()
                    if (block[1]+block[2])/2 == (R_5+G_5+B_5)/3:
                        pixel[i,j]= (R_5,G_5,B_5);
                    elif (block[2]+block[1])/2 == (R_7+G_7+B_7)/3:
                        pixel[i,j]= (R_7,G_7,B_7);
                    elif (block[2]+block[1])/2 == (R_8+G_8+B_8)/3:
                        pixel[i,j]= (R_8,G_8,B_8);
                    elif (block[2]+block[1])/2 == (R+G+B)/3:
                        pixel[i,j]= (R,G,B);
                elif i == width-1  and j == height-1:
                    R,G,B = pixel[i,j]
                    R_5,G_5,B_5 = pixel[i-1,j-1]
                    R_7,G_7,B_7 = pixel[i-1,j]
                    R_8,G_8,B_8 = pixel[i,j-1]
                    block.append((R_5+G_5+B_5)/3)
                    block.append((R_7+G_7+B_7)/3)
                    block.append((R_8+G_8+B_8)/3)
                    block.append((R+G+B)/3)
                    block.sort()
                    if (block[1]+block[2])/2 == (R_5+G_5+B_5)/3:
                        pixel[i,j]= (R_5,G_5,B_5);
                    elif (block[2]+block[1])/2 == (R_7+G_7+B_7)/3:
                        pixel[i,j]= (R_7,G_7,B_7);
                    elif (block[2]+block[1])/2 == (R_8+G_8+B_8)/3:
                        pixel[i,j]= (R_8,G_8,B_8);
                    elif (block[2]+block[1])/2 == (R+G+B)/3:
                        pixel[i,j]= (R,G,B);
                elif i == width-1  and j == 0:
                    R,G,B = pixel[i,j]
                    R_5,G_5,B_5 = pixel[i-1,j]
                    R_7,G_7,B_7 = pixel[i-1,j+1]
                    R_8,G_8,B_8 = pixel[i,j+1]
                    block.append((R_5+G_5+B_5)/3)
                    block.append((R_7+G_7+B_7)/3)
                    block.append((R_8+G_8+B_8)/3)
                    block.append((R+G+B)/3)
                    block.sort()
                    if (block[1]+block[2])/2 == (R_5+G_5+B_5)/3:
                        pixel[i,j]= (R_5,G_5,B_5);
                    elif (block[2]+block[1])/2 == (R_7+G_7+B_7)/3:
                        pixel[i,j]= (R_7,G_7,B_7);
                    elif (block[2]+block[1])/2 == (R_8+G_8+B_8)/3:
                        pixel[i,j]= (R_8,G_8,B_8);
                    elif (block[2]+block[1])/2 == (R+G+B)/3:
                        pixel[i,j]= (R,G,B);
                elif i == 0:
                    R,G,B = pixel[i,j]
                    R_4,G_4,B_4 = pixel[i,j-1]
                    R_5,G_5,B_5 = pixel[i,j+1]
                    R_6,G_6,B_6 = pixel[i+1,j-1]
                    R_7,G_7,B_7 = pixel[i+1,j]
                    R_8,G_8,B_8 = pixel[i+1,j+1]
                    block.append((R_4+G_4+B_4)/3)
                    block.append((R_5+G_5+B_5)/3)
                    block.append((R_6+G_6+B_6)/3)
                    block.append((R_7+G_7+B_7)/3)
                    block.append((R_8+G_8+B_8)/3)
                    block.append((R+G+B)/3)
                    block.sort()
                    if (block[2]+block[3])/2 == (R_4+G_4+B_4)/3:
                        pixel[i,j]= (R_4,G_4,B_4);
                    elif (block[2]+block[3])/2 == (R_5+G_5+B_5)/3:
                        pixel[i,j]= (R_5,G_5,B_5);
                    elif (block[2]+block[3])/2 == (R_6+G_6+B_6)/3:
                        pixel[i,j]= (R_6,G_6,B_6);
                    elif (block[2]+block[3])/2 == (R_7+G_7+B_7)/3:
                        pixel[i,j]= (R_7,G_7,B_7);
                    elif (block[2]+block[3])/2 == (R_8+G_8+B_8)/3:
                        pixel[i,j]= (R_8,G_8,B_8);
                    elif (block[2]+block[3])/2 == (R+G+B)/3:
                        pixel[i,j]= (R,G,B);
                elif i == width-1:
                    R,G,B = pixel[i,j]
                    R_4,G_4,B_4 = pixel[i,j-1]
                    R_5,G_5,B_5 = pixel[i,j+1]
                    R_6,G_6,B_6 = pixel[i-1,j-1]
                    R_7,G_7,B_7 = pixel[i-1,j]
                    R_8,G_8,B_8 = pixel[i-1,j+1]
                    block.append((R_4+G_4+B_4)/3)
                    block.append((R_5+G_5+B_5)/3)
                    block.append((R_6+G_6+B_6)/3)
                    block.append((R_7+G_7+B_7)/3)
                    block.append((R_8+G_8+B_8)/3)
                    block.append((R+G+B)/3)
                    block.sort()
                    if (block[2]+block[3])/2 == (R_4+G_4+B_4)/3:
                        pixel[i,j]= (R_4,G_4,B_4);
                    elif (block[2]+block[3])/2 == (R_5+G_5+B_5)/3:
                        pixel[i,j]= (R_5,G_5,B_5);
                    elif (block[2]+block[3])/2 == (R_6+G_6+B_6)/3:
                        pixel[i,j]= (R_6,G_6,B_6);
                    elif (block[2]+block[3])/2 == (R_7+G_7+B_7)/3:
                        pixel[i,j]= (R_7,G_7,B_7);
                    elif (block[2]+block[3])/2 == (R_8+G_8+B_8)/3:
                        pixel[i,j]= (R_8,G_8,B_8);
                    elif (block[2]+block[3])/2 == (R+G+B)/3:
                        pixel[i,j]= (R,G,B);
            elif j == 0 or j == height-1:
                if i != 0 and i != width-1:
                    if j == 0:
                        R,G,B = pixel[i,j]
                        R_1,G_1,B_1 = pixel[i-1,j+1]
                        R_2,G_2,B_2 = pixel[i-1,j]
                        R_4,G_4,B_4 = pixel[i,j+1]
                        R_6,G_6,B_6 = pixel[i+1,j+1]
                        R_7,G_7,B_7 = pixel[i+1,j]
                        block.append((R_1+G_1+B_1)/3)
                        block.append((R_2+G_2+B_2)/3)
                        block.append((R_4+G_4+B_4)/3)
                        block.append((R_6+G_6+B_6)/3)
                        block.append((R_7+G_7+B_7)/3)
                        block.append((R+G+B)/3)
                        block.sort()
                        if (block[2]+block[3])/2 == (R_1+G_1+B_1)/3:
                            pixel[i,j]= (R_1,G_1,B_1);
                        elif (block[2]+block[3])/2 == (R_2+G_2+B_2)/3:
                            pixel[i,j]= (R_2,G_2,B_2);
                        elif (block[2]+block[3])/2 == (R_4+G_4+B_4)/3:
                            pixel[i,j]= (R_4,G_4,B_4);
                        elif (block[2]+block[3])/2 == (R_6+G_6+B_6)/3:
                            pixel[i,j]= (R_6,G_6,B_6);
                        elif (block[2]+block[3])/2 == (R_7+G_7+B_7)/3:
                            pixel[i,j]= (R_7,G_7,B_7);
                        elif (block[2]+block[3])/2 == (R+G+B)/3:
                            pixel[i,j]= (R,G,B);

                    elif j == height-1:

                        R,G,B = pixel[i,j]
                        R_1,G_1,B_1 = pixel[i-1,j-1]
                        R_2,G_2,B_2 = pixel[i-1,j]
                        R_4,G_4,B_4 = pixel[i,j-1]
                        R_6,G_6,B_6 = pixel[i+1,j-1]
                        R_7,G_7,B_7 = pixel[i+1,j]
                        block.append((R_1+G_1+B_1)/3)
                        block.append((R_2+G_2+B_2)/3)
                        block.append((R_4+G_4+B_4)/3)
                        block.append((R_6+G_6+B_6)/3)
                        block.append((R_7+G_7+B_7)/3)
                        block.append((R+G+B)/3)
                        block.sort()
                        if (block[2]+block[3])/2 == (R_1+G_1+B_1)/3:
                            pixel[i,j]= (R_1,G_1,B_1);
                        elif (block[2]+block[3])/2 == (R_2+G_2+B_2)/3:
                            pixel[i,j]= (R_2,G_2,B_2);
                        elif (block[2]+block[3])/2 == (R_4+G_4+B_4)/3:
                            pixel[i,j]= (R_4,G_4,B_4);
                        elif (block[2]+block[3])/2 == (R_6+G_6+B_6)/3:
                            pixel[i,j]= (R_6,G_6,B_6);
                        elif (block[2]+block[3])/2 == (R_7+G_7+B_7)/3:
                            pixel[i,j]= (R_7,G_7,B_7);
                        elif (block[2]+block[3])/2 == (R+G+B)/3:
                            pixel[i,j]= (R,G,B);
            else:
                R,G,B = pixel[i,j]
                R_1,G_1,B_1 = pixel[i-1,j-1]
                R_2,G_2,B_2 = pixel[i-1,j]
                R_3,G_3,B_3 = pixel[i-1,j+1]
                R_4,G_4,B_4 = pixel[i,j-1]
                R_5,G_5,B_5 = pixel[i,j+1]
                R_6,G_6,B_6 = pixel[i+1,j-1]
                R_7,G_7,B_7 = pixel[i+1,j]
                R_8,G_8,B_8 = pixel[i+1,j+1]
                block.append((R_1+G_1+B_1)/3)
                block.append((R_2+G_2+B_2)/3)
                block.append((R_3+G_3+B_3)/3)
                block.append((R_4+G_4+B_4)/3)
                block.append((R_5+G_5+B_5)/3)
                block.append((R_6+G_6+B_6)/3)
                block.append((R_7+G_7+B_7)/3)
                block.append((R_8+G_8+B_8)/3)
                block.append((R+G+B)/3)
                block.sort()
                if block[4] == (R_1+G_1+B_1)/3:
                    pixel[i,j]= (R_1,G_1,B_1);
                elif block[4] == (R_2+G_2+B_2)/3:
                    pixel[i,j]= (R_2,G_2,B_2);
                elif block[4] == (R_3+G_3+B_3)/3:
                    pixel[i,j]= (R_3,G_3,B_3);
                elif block[4] == (R_4+G_4+B_4)/3:
                    pixel[i,j]= (R_4,G_4,B_4);
                elif block[4] == (R_5+G_5+B_5)/3:
                    pixel[i,j]= (R_5,G_5,B_5);
                elif block[4] == (R_6+G_6+B_6)/3:
                    pixel[i,j]= (R_6,G_6,B_6);
                elif block[4] == (R_7+G_7+B_7)/3:
                    pixel[i,j]= (R_7,G_7,B_7);
                elif block[4] == (R_8+G_8+B_8)/3:
                    pixel[i,j]= (R_8,G_8,B_8);
                elif block[4] == (R+G+B)/3:
                    pixel[i,j]= (R,G,B);
    Q10_pic.save("Q10.jpg")

def Q11_1(string,width,height):
    Q11_1_pic = Image.open(string)
    transpose_img = Image.open(string)
    box = (0, 0, width, height/2)
    region = Q11_1_pic.crop(box)
    region = region.transpose(Image.ROTATE_180)
    region = region.transpose(Image.FLIP_LEFT_RIGHT)
    transpose_img.paste(region,(0, height/2, width, height))
    transpose_img.save("Q11-1.jpg")

def Q11_2(string,width,height):
    Q11_2_pic = Image.open(string)
    transpose_img = Image.open(string)
    box = (0, 0, width/2, height)
    region = Q11_2_pic.crop(box)
    region = region.transpose(Image.FLIP_LEFT_RIGHT)
    transpose_img.paste(region,(width/2, 0, width, height))
    transpose_img.save("Q11-2.jpg")

def Q11_3(string,width,height):
    Q11_3_pic = Image.open(string)
    transpose_img = Image.open(string)
    box = (width/2, 0, width, height)
    region = Q11_3_pic.crop(box)
    #region = region.transpose(Image.ROTATE_180)
    region = region.transpose(Image.FLIP_LEFT_RIGHT)
    transpose_img.paste(region,(0, 0, width/2, height))
    transpose_img.save("Q11-3.jpg")

def Q11_4(string,width,height):
    Q11_4_pic = Image.open(string)
    transpose_img = Image.open(string)
    box = (0, height/2, width, height)
    region = Q11_4_pic.crop(box)
    region = region.transpose(Image.ROTATE_180)
    region = region.transpose(Image.FLIP_LEFT_RIGHT)
    transpose_img.paste(region,(0, 0, width, height/2))
    transpose_img.save("Q11-4.jpg")

def Q12(string_1,string_2):
    Q12_1_pic = Image.open(string_1)
    Q12_2_pic = Image.open(string_2)
    width, height = Q12_1_pic.size
    pixel_1 = Q12_1_pic.load()
    pixel_2 = Q12_2_pic.load()
    for i in range(width):
        for j in range(height):
            R = 29
            G = 18
            B = 86
            R_1,G_1,B_1 = pixel_2[i,j]
            if (((R_1-R)**2+(G_1-G)**2+(B_1-B)**2)**0.5) < 10:
                pixel_2[i,j] = pixel_1[i,j]
    Q12_2_pic.save("Q12.jpg")

if __name__== "__main__" :
    from PIL import Image
    string = 'Penguins.jpg'
    string_10 = "Penguins_noise.jpg"
    string_12_1 = "Chrysanthemum.jpg"
    string_12_2 = "Elsa.jpg"
    im = Image.open(string)
    width,height = im.size
    Q1(string,width,height)
    Q2(string,width,height)
    Q3(string,width,height)
    Q4(string,width,height)
    Q5_1(string,width,height)
    Q5_2(string,width,height)
    Q6_1(string,width,height)
    Q6_2(string,width,height)
    Q6_3(string,width,height)
    Q7_1(string,width,height)
    Q7_2(string,width,height)
    Q7_3(string,width,height)
    Q7_4(string,width,height)
    Q7_5(string,width,height)
    Q8(string,width,height)
    Q9(string,width,height)
    Q10_answer = Q10(string_10,width,height)
    Q11_1(string,width,height)
    Q11_2(string,width,height)
    Q11_3(string,width,height)
    Q11_4(string,width,height)
    Q12(string_12_1,string_12_2)
