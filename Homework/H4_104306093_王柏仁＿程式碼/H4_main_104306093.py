#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from pylab import *

import pickle

from Tkinter import *
from PIL import ImageTk, Image
import tkMessageBox
import tkFileDialog
from ttk import Frame, Button, Label, Style

from random import randint
from PIL import Image

import H4_104306093_Q1 as Q1
import H4_104306093_Q2 as Q2
import H4_104306093_Q3 as Q3

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()


    def initUI(self):

        self.parent.title("HW3")

        self.pack(fill=BOTH, expand=1)

        Button(self, text = "Select File", command = openFile).grid(row=0, column=0, pady=5, padx=5)
        self.fileName = StringVar()
        Label(self, textvariable=self.fileName).grid(row=0, column=1, columnspan=2, pady=5, padx=5)

        Label(self, text = "Select Mode: ").grid(row=1, column=0, pady=5, padx=5)
        Label(self, text = "Select Dataset: ").grid(row=1, column=2, pady=5, padx=5)
        Label(self, text = "Select Ways: ").grid(row=1, column=4, pady=5, padx=5)
        Label(self, text = "要不要馬賽克製圖").grid(row=2, column=0, pady=5, padx=5)
        Label(self, text = "選擇等分：（馬賽克時用）").grid(row=2, column=2, pady=5, padx=5)

        mode = StringVar(self)
        mode.set("Q1-ColorHistogram")
        om_mode = OptionMenu(self, mode, "Q1-ColorHistogram", "Q2-ColorLayout", "Q3-SIFT Visual Words", "Q4-Visual Words using stop words")
        om_mode.grid(row=1, column=1, pady=5, padx=5)

        color = StringVar(self)
        color.set("RGB")
        om_color = OptionMenu(self, color, "RGB", "HSV")
        om_color.grid(row=1, column=5, pady=5, padx=5)

        marsek = StringVar(self)
        marsek.set("不要")
        om_marsek = OptionMenu(self, marsek, "不要", "要")
        om_marsek.grid(row=2, column=1, pady=5, padx=5)

        cut = StringVar(self)
        cut.set("4")
        om_cut = OptionMenu(self, cut, "4","16","64","81","100", "400","900","1600")
        om_cut.grid(row=2, column=3, pady=5, padx=5)

        dataset = StringVar(self)
        dataset.set("Clothes")
        om_data = OptionMenu(self, dataset, "Clothes" , "Daily Life")
        om_data.grid(row=1, column=3, pady=5, padx=5)
        Button(self, text = "SEARCH", command = lambda: startSearching(self.fileName.get(),mode.get(),dataset.get(),color.get(),marsek.get(),cut.get())).grid(row=3, column=0, pady=5, padx=5)

        self.images = []
        for i in range(10):
            self.images.append(Label(self))
            self.images[i].grid(row=i/5+6, column=i%5, pady=50, padx=5)

def openFile ():
    fileName = tkFileDialog.askopenfilename()
    app.fileName.set(fileName)
    if app.fileName.get() == "" :
        print "hi"
    else :
        image = Image.open(app.fileName.get())
        app.query = ImageTk.PhotoImage(image.resize((100,100), Image.BILINEAR))
        Label(app, image=app.query).grid(row=0, column=3, pady=5, padx=5)

def startSearching (fileName, mode , dataset,color,marsek,cut):
    if marsek == "不要".decode('utf-8') :
        if dataset == "Clothes":
            finish = find_in_data(fileName,"dataset_clothes/*.jpg","dataset_clothes",mode,color)
            if finish == "已分好SIFT檔" or finish == "還沒完成" :
                app.images = []
                app.images.append(Label(app))
                app.images[0].grid(row=0/5+6, column=0%5, pady=50, padx=5)
                app.images[0].configure(text = finish)
            else :
                for i in range(len(finish)):
                    path = finish[i][0]
                    img = ImageTk.PhotoImage(Image.open(path).resize((100,100)), Image.BILINEAR)
                    app.images[i].configure(image = img)
                    app.images[i].image = img

        else :
            finish = find_in_data(fileName,"dataset_life/*.jpg","dataset_life",mode,color)
            if finish == "已分好SIFT檔" or finish == "還沒完成":
                app.images = []
                app.images.append(Label(app))
                app.images[0].grid(row=0/5+6, column=0%5, pady=50, padx=5)
                app.images[0].configure(text = finish)
            else :
                for i in range(len(finish)):
                    path = finish[i][0]
                    img = ImageTk.PhotoImage(Image.open(path).resize((100,100)), Image.BILINEAR)
                    app.images[i].configure(image = img)
                    app.images[i].image = img
    else :
        if dataset == "Clothes":
            finish = make_pics(fileName,"dataset_clothes/*.jpg","dataset_clothes",mode,color,cut)
            if finish == "not yet" :
                app.images = []
                app.images.append(Label(app))
                app.images[0].grid(row=0/5+6, column=0%5, pady=50, padx=5)
                app.images[0].configure(text = finish)
            else :
                for i in range(1):
                    path = finish
                    img = ImageTk.PhotoImage(Image.open(path).resize((500,500)), Image.BILINEAR)
                    app.images[i].configure(image = img)
                    app.images[i].image = img
        else :
            finish = make_pics(fileName,"dataset_life/*.jpg","dataset_life",mode,color,cut)
            if finish == "not yet" :
                app.images = []
                app.images.append(Label(app))
                app.images[0].grid(row=0/5+6, column=0%5, pady=50, padx=5)
                app.images[0].configure(text = finish)
            else :
                for i in range(1):
                    path = finish
                    img = ImageTk.PhotoImage(Image.open(path).resize((500,500)), Image.BILINEAR)
                    app.images[i].configure(image = img)
                    app.images[i].image = img

def make_pics(fileName,dataset_name,data_dir,mode,color,cut) :
    if mode == "Q1-ColorHistogram" :
        if color == "RGB" :
            print "start !"
            return Q1.Question_1_marsek(fileName,dataset_name,data_dir,cut)
            #return "result.jpg"
            print "done !"
        elif color == "HSV" :
            return "not yet"
            #還沒完成"
    elif mode == "Q2-ColorLayout" :
        return "not yet"
    elif mode == "Q3-SIFT Visual Words" :
        return "not yet"
    elif mode == "Q4-Visual Words using stop words" :
        return "not yet"
    else :
        return "not yet"

def find_in_data(fileName,dataset_name,data_dir,mode,color) :
    if mode == "Q1-ColorHistogram" :
        if color == "RGB" :
            return Q1.Question_1_rgb(fileName,dataset_name,data_dir)
        elif color == "HSV" :
            return Q1.Question_1_hsv(fileName,dataset_name,data_dir)
            #"還沒完成"
    elif mode == "Q2-ColorLayout" :
        return Q2.Question_2(fileName,dataset_name,data_dir)
    elif mode == "Q3-SIFT Visual Words" :
        Q3.Question_3(fileName,dataset_name,data_dir)
        return "已分好SIFT檔"
    elif mode == "Q4-Visual Words using stop words" :
        return "還沒完成"
    else :
        pass

if __name__ == '__main__':
    root = Tk()
    size = 300, 220

    app = Example(root)
    root.geometry("1024x720")
    root.mainloop()
