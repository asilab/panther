#!python
#!/usr/bin/env python
# prepare train / test split
import shutil
import os
import sys
from os import listdir
from os.path import isfile, join
import scipy.io
import numpy as np

if __name__ == "__main__":

    for f in listdir("../Paintings91/Images"):
        if isfile(join("../Paintings91/Images", f)):
            if ".JPG" in f:
                result = f.replace(".JPG", ".jpg")
            if "DOUARD_MANET" in f:
                result = f.replace("ÃDOUARD_MANET","EDOUARD_MANET").replace("ÉDOUARD_MANET","EDOUARD_MANET").replace("􏹉DOUARD_MANET","EDOUARD_MANET").replace("\udcc9DOUARD_MANET","EDOUARD_MANET").replace("\udcc9","EDOUARD_MANET").replace("\x89","")
                os.rename("../Paintings91/Images/"+f, "../Paintings91/Images/"+result)
                
    ############# Author Classification##############

    data = scipy.io.loadmat('../Paintings91/Labels/image_names.mat')
    image_names_authors=data['image_names']
   
    data =  scipy.io.loadmat('../Paintings91/Labels/trainset.mat')
    trainset = data['trainset']

    data =  scipy.io.loadmat('../Paintings91/Labels/testset.mat')
    testset = data['testset']

    data = scipy.io.loadmat('../Paintings91/Labels/labels.mat')
    labels_author = data['labels']   
     
    labels_authors_train = labels_author[np.where(trainset)[0],]
    labels_authors_test = labels_author[np.where(testset)[0],]

    labels_authors_index = np.where(labels_author)[1]


    for k in range(621, 666):
        image_names_authors[k][0][0] = image_names_authors[k][0][0].replace("ÃDOUARD_MANET","EDOUARD_MANET").replace("ÉDOUARD_MANET","EDOUARD_MANET").replace("􏹉DOUARD_MANET","EDOUARD_MANET").replace("\udcc9DOUARD_MANET","EDOUARD_MANET").replace("\udcc9DOUARD_MANET","EDOUARD_MANET").replace("\x89","")

    for k in range(len(labels_authors_index)):
        authors = labels_authors_index[k]
        try:
            os.mkdir('../Labels_Author/Train/%s' %authors)
        except:
            pass
        try:
            os.mkdir('../Labels_Author/Test/%s' %authors)
        except:
            pass
        if trainset[k]:
            try:
                if ".JPG" in image_names_authors[k][0][0]:
                    image_names_authors[k][0][0] = image_names_authors[k][0][0].replace(".JPG", ".jpg")
                _ = shutil.copy('../Paintings91/Images/%s' %image_names_authors[k][0][0], '../Labels_Author/Train/%s' %authors)
            except:
                print(k, image_names_authors[k][0][0])
        else:
            try:
                if ".JPG" in image_names_authors[k][0][0]:
                    image_names_authors[k][0][0] = image_names_authors[k][0][0].replace(".JPG", ".jpg")
                _ = shutil.copy('../Paintings91/Images/%s' %image_names_authors[k][0][0], '../Labels_Author/Test/%s' %authors)
            except:
                print(k, image_names_authors[k][0][0])
    ############# Style Classification##############

    data =  scipy.io.loadmat('../Paintings91/Labels_Style/image_names_style.mat')
    image_names_style = data['image_names_style']


    data =  scipy.io.loadmat('../Paintings91/Labels_Style/trainset_style.mat')
    trainset = data['trainset_style']

    data =  scipy.io.loadmat('../Paintings91/Labels_Style/testset_style.mat')
    testset = data['testset_style']

    data =  scipy.io.loadmat('../Paintings91/Labels_Style/labels_style.mat')
    labels_style = data['labels_style']

    labels_style_train = labels_style[np.where(trainset)[0],]
    labels_style_test = labels_style[np.where(testset)[0],]


    labels_style_index = np.where(labels_style)[1]

    # correct some problems with encodings!
    for k in range(734, 779):
        image_names_style[k][0][0] = image_names_style[k][0][0].replace("ÃDOUARD_MANET","EDOUARD_MANET").replace("ÉDOUARD_MANET","EDOUARD_MANET").replace("􏹉DOUARD_MANET","EDOUARD_MANET").replace("\udcc9DOUARD_MANET","EDOUARD_MANET").replace("\udcc9DOUARD_MANET","EDOUARD_MANET").replace("\x89","")

    for k in range(len(labels_style_index)):
        style = labels_style_index[k]
        try:
            os.mkdir('../Labels_Style/Train/%s' %style)
        except:
            pass
        try:
            os.mkdir('../Labels_Style/Test/%s' %style)
        except:
            pass
        if trainset[k]:
            try:
                if ".JPG" in image_names_authors[k][0][0]:
                    image_names_authors[k][0][0] = image_names_authors[k][0][0].replace(".JPG", ".jpg")
                _ = shutil.copy('../Paintings91/Images/%s' %image_names_style[k][0][0], '../Labels_Style/Train/%s' %style)
            except:
                print(k, image_names_style[k][0][0])
        else:
            try:
                if ".JPG" in image_names_authors[k][0][0]:
                    image_names_authors[k][0][0] = image_names_authors[k][0][0].replace(".JPG", ".jpg")
                _ = shutil.copy('../Paintings91/Images/%s' %image_names_style[k][0][0], '../Labels_Style/Test/%s' %style)
            except:
                print(k, image_names_style[k][0][0])

