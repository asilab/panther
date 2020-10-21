#!python
#!/usr/bin/env python

import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import sys
import matplotlib.pylab as plt
from string import digits
import statistics
import scipy.io

def reorder_64(artist_list):
    order_64=[0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 2, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 3, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 4, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 5, 60, 61, 62, 63, 6, 7, 8, 9]

    reorder_list=[None] * (len(order_64))
    for a in range(len(order_64)):
        reorder_list[order_64[a]]=artist_list[a]
    return reorder_list


def reorder(artist_list):
    order_256=[0, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 10, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 11, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 12, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 13, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 14, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 15, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 16, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 17, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 18, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 19, 1, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 20, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 21, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 22, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 23, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 24, 250, 251, 252, 253, 254, 255, 25, 26, 27, 28, 29, 2, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 3, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 4, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 5, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 6, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 7, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 8, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 9]

    reorder_list=[None] * (len(order_256))
    for a in range(len(order_256)):
        reorder_list[order_256[a]]=artist_list[a]
    return reorder_list

def process_nc_64_features(file1):
    lines = file1.readlines() 
    painters_images_complexity = []
    painters_name = []
    painters_n = []
    number = 0
    painter = ""
    painter_label = [] 
    for x in lines:
            string_line = x.replace("ÃDOUARD_MANET","EDOUARD_MANET").replace('\n', '').replace(' ', '\t').replace(':', '').split('\t')
            unordered_image = list(filter(None, string_line))
            author = unordered_image[0]
            remove_digits = str.maketrans('', '', digits)
            res = author.translate(remove_digits).replace('.jpg.pgm', '').replace('_', ' ').title()
            unordered_image = unordered_image[1:]
            unordered_image = [float(x) for x in unordered_image]
            if (len(unordered_image) != 64):
                print(author, len(unordered_image))
            else:
                ordered_image = reorder_64(unordered_image) 
                painters_images_complexity.append(ordered_image)
                painters_name.append(res)
                painters_n.append(author)
                # print (painter,"/t" ,res)
                if(painter == res):
                    painter_label.append(number)
                else:
                    painter = res
                    number += 1
                    painter_label.append(number)

    nc_values = np.array(painters_images_complexity).astype('float32')
    classes  = np.array(painter_label).astype('int32')
    print(nc_values.shape)
    print(classes.shape)
    return classes, nc_values


def process_nc_256_features(file1):
    lines = file1.readlines() 
    painters_images_complexity = []
    painters_name = []
    painters_n = []
    number = 0
    painter = ""
    painter_label = [] 
    for x in lines:
            string_line = x.replace("ÃDOUARD_MANET","EDOUARD_MANET").replace('\n', '').replace(' ', '\t').replace(':', '').split('\t')
            unordered_image = list(filter(None, string_line))
            author = unordered_image[0]
            remove_digits = str.maketrans('', '', digits)
            res = author.translate(remove_digits).replace('.jpg.pgm', '').replace('_', ' ').title()
            unordered_image = unordered_image[1:]
            unordered_image = [float(x) for x in unordered_image]
            if (len(unordered_image) != 256):
                print(author, len(unordered_image))
            else:
                ordered_image = reorder(unordered_image) 
                painters_images_complexity.append(ordered_image)
                painters_name.append(res)
                painters_n.append(author)
                # print (painter,"/t" ,res)
                if(painter == res):
                    painter_label.append(number)
                else:
                    painter = res
                    number += 1
                    painter_label.append(number)

    nc_values = np.array(painters_images_complexity).astype('float32')
    classes  = np.array(painter_label).astype('int32')
    print(nc_values.shape)
    print(classes.shape)
    return classes, nc_values

def restructure_data(name,painting, classes, style_class, nc_256,nc_64, hdc, alpha):
    data = {
        'painting':painting,
        'classes': classes,
        'style_classes':style_class,
        'nc_256': nc_256,
        'nc_64' : nc_64,
        'hdc': hdc,
        'alpha':alpha,
    }

    np.save("../data/"+name+'data.npy', data)

def restructure_normalized_data(name,painting, classes, style_class, nc_256, hdc, alpha):
    data = {
        'painting':painting,
        'classes': classes,
        'style_classes':style_class,
        'nc_256': nc_256,
        'hdc': hdc,
        'alpha':alpha,
    }

    np.save("../data/"+name+'data.npy', data)


def process_hdc_features(file_to_read):
    lines = file_to_read.readlines() 
    values_image = []
    number = 0
    painter = ""
    classes = []
    for x in lines:
        hdc = []
        string_line = x.replace("ÃDOUARD_MANET","EDOUARD_MANET").replace('\n', '').replace(' ', '\t').replace(':', '').split('\t')
        image = list(filter(None, string_line))
        author = image[0]

        remove_digits = str.maketrans('', '', digits)
        res = author.translate(remove_digits).replace('.jpg.pgm', '').replace('_', ' ').title()
        image = image[1:]
        for radious_hdc in image:
            hdc.append(float(radious_hdc.replace("(","").replace(")","").split(",")[1]))
       
        if(painter != res):
            painter = res
            number += 1
        classes.append(number)
        values_image.append(hdc)

    minimum = min(map(len, values_image))

    maximum = max(map(len, values_image))
    padding_hdc = []
    for hdc in values_image:
        n_zeros = maximum - len(hdc)
        hdc_padded = hdc + [0]*n_zeros
        padding_hdc.append(hdc_padded)

    hdc_val=np.array(padding_hdc).astype('float32')
    classes=np.array(classes).astype('int32')
    print(hdc_val.shape)
    print(classes.shape)
    return classes, hdc_val

def style_label(file_to_read, labels_to_paintings):
    lines = file_to_read.readlines() 
    values_image = []

    painter = ""
    authors = []
    
    for x in lines:
        hdc = []
        string_line = x.replace("ÃDOUARD_MANET","EDOUARD_MANET").replace('\n', '').replace(' ', '\t').replace(':', '').split('\t')
        image = list(filter(None, string_line))
        author = image[0]
        authors.append(author)
        # remove_digits = str.maketrans('', '', digits)
        # res = author.translate(remove_digits).replace('.jpg.pgm', '').replace('_', ' ').title()
        # print(author)
    count=0
    style = []
    painting =[]
    for author in authors:
        l = -1 
        for name, label in labels_to_paintings:
            if name in author:
               l=label
        painting.append(author)
        style.append(l)
    pnt =[]
    for p in painting:
        if "DOUARD_MANET" in p:
            p = p.replace("ÉDOUARD_MANET", "EDOUARD_MANET")
        pnt.append(p)
    painting = np.array(pnt)


    st = np.array(style).astype('int32')
    # for a in painting:
    #     print(a)
    return st, painting



def process_hdc_features_2(file_to_read):
    lines = file_to_read.readlines() 
    values_image = []
    number = 0
    painter = ""
    classes = []
    for x in lines:
        hdc = []
        string_line = x.replace("ÃDOUARD_MANET","EDOUARD_MANET").replace('\n', '').replace(' ', '\t').replace(':', '').split('\t')
        image = list(filter(None, string_line))
        author = image[0]

        remove_digits = str.maketrans('', '', digits)
        res = author.translate(remove_digits).replace('.jpg.pgm', '').replace('_', ' ').title()
        image = image[1:]       
        if(painter != res):
            painter = res
            number += 1
        classes.append(number)
        values_image.append(image)

    alpha_value=np.array(values_image).astype('float32')
    classes=np.array(classes).astype('int32')
    return classes, alpha_value

def match_label(report_hdc, report_nc, labels):
    label_matcher=[]
    for painting_nc in report_nc:
        for label in labels:
            if label[0] in painting_nc[0]:
                label_matcher.append( [label[0], label[1], painting_nc[1]])

    label_complete=[]
    for label in label_matcher:
        for painting_hdc in report_hdc:
            if label[0] in painting_hdc[0]:
                value = label + [painting_hdc[1]]
                label_complete.append(value)
    label_complete.sort(key=lambda x: x[1])

    return label_complete

def read_report(filename):
    f=open(filename, "r", errors='ignore')
    content = f.readlines()
    result = []
    for x in content:
        string_line = x.replace('\n', '').replace('.pgm', '').replace(".PROCESSED.bin","").replace(' ', '').split(':')
        line = list(string_line)
        avg_value = float(line[1])
        result.append([line[0], avg_value])
    return result

def get_index(array_index,filename):
    index=[]
    counter=0
    for label_list in array_index:
        index.append([filename[counter], label_list.tolist().index(1)])
        counter+=1
    return index

def get_style_labels():
    mat = scipy.io.loadmat('../Paintings91/Labels_Style/labels_style.mat')
    label_style = mat['labels_style']    
    mat = scipy.io.loadmat('../Paintings91/Labels_Style/image_names_style.mat')
    mapping_artist=mat['image_names_style']
    
    file_name = []
    names=[]
    unchanged_names=[]
    for a in mapping_artist:
        filename=a[0][0]
        if "DOUARD_MANET" in filename:
            filename = filename.replace("ÃDOUARD_MANET","DOUARD_MANET")
            filename=filename[1:]
        result = ''.join([i for i in a[0][0] if not i.isdigit()])
        res=result.replace("_.jpg","").replace("_"," ").title()
        file_name.append(filename)
        names.append(res)
        if "DOUARD_MANET" in result:
            result = result.replace("ÃDOUARD_MANET","DOUARD_MANET")
            result=result[1:]
        unchanged_names.append(result.replace("_.jpg",""))
    
    label = get_index(label_style, file_name)
    return label
    
if __name__ == "__main__":
    labels_paintings = get_style_labels()

    file_1 = open("../reports/REPORT_REGIONAL_COMPLEXITY_256_Quantizing8", 'r', encoding='iso-8859-1')
    classes_1, nc_256 = process_nc_256_features(file_1)
    file_2 = open("../reports/REPORT_REGIONAL_COMPLEXITY_64_Quantizing8", 'r', encoding='iso-8859-1')
    classes, nc_64 = process_nc_64_features(file_2)
    file_3 = open("../reports/REPORT_COMPLEXITY_HDC_FEATURES_Quantizing8", 'r', encoding='iso-8859-1')
    classes_2, hdc = process_hdc_features(file_3)
    file_4 = open("../reports/REPORT_HDC_Quantizing8", 'r', encoding='iso-8859-1')
    classes_3, alpha_value = process_hdc_features_2(file_4)
    file_4 = open("../reports/REPORT_HDC_Quantizing8", 'r', encoding='iso-8859-1')
    style_class, painting = style_label(file_4, labels_paintings)


    for pair in zip(classes, classes_1):
        if(pair[0]!=pair[1]):
            print("error")
            sys.exit()

    restructure_data("",painting,classes, style_class, nc_256, nc_64, hdc, alpha_value)

    #### Normalized
    print("Normalized")
    file_1 = open("../reports/REPORT_REGIONAL_COMPLEXITY_256_normalize_Quantizing8", 'r', encoding='iso-8859-1')
    classes_1, nc_256_normalized = process_nc_256_features(file_1)
    file_3 = open("../reports/NORMALIZED_HDC_FEATURES", 'r', encoding='iso-8859-1')
    classes_2, hdc_normalized = process_hdc_features(file_3)
    file_4 = open("../reports/REPORT_HDC_normalize_Quantizing8", 'r', encoding='iso-8859-1')
    classes_3, alpha_value_normalized = process_hdc_features_2(file_4)

    for pair in zip(classes, classes_1):
        if(pair[0]!=pair[1]):
            print("error")
            sys.exit()
    restructure_normalized_data("normalized_",painting, classes, style_class, nc_256_normalized, hdc_normalized, alpha_value_normalized)
    #######################
        
    

    
