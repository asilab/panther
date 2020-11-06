import cv2
import os
from PIL import Image
import numpy as np
import sys

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        if ".jpg.pgm" in filename and ".PROCESSED.bin" not in filename:
            pic = Image.open(os.path.join(folder,filename))
            img = np.array(pic)
            if img is not None:
                A = [img.shape[0], img.shape[1]]
                images.append(A)
    return images

def process_maxmin(file_to_read):
    file_1 = open(file_to_read, 'r', encoding='iso-8859-1')
    lines = file_1.readlines() 
    values_image = []
    number = 0
    painter = ""
    range = []
    for x in lines:
        hdc = []
        string_line = x.replace('\n', '').replace(':', '').replace(' ', '\t').split('\t')
        values = list(filter(None, string_line))
        range.append(int(values[-1]))
    return range



if __name__ == "__main__":
    d =process_maxmin("../reports/MIN_MAX")
    import matplotlib.pyplot as plt

    # An "interface" to matplotlib.axes.Axes.hist() method
    n, bins, patches = plt.hist(x=d, bins=20, color='#0504aa',
                                alpha=0.7, rwidth=0.85)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Max Pixel Value Image')
    plt.ylabel('Frequency')
    plt.title('max pixel value frequency')
    plt.xticks(np.arange(min(d), max(d)+1, 10.0))
    maxfreq = n.max()
    # Set a clean upper y-axis limit.
    plt.ylim(ymax=3000)
    plt.show()
  
    # blocks = [n for n in range(min(a),max(a)+10,10)] 
    # dict_values = {}

    # for block in blocks:
    #     val_len  = len([val for val in a if val>=block and val < block+10 ])
    #     dict_values[block]= val_len
    
    # sys.exit()
    # im = load_images_from_folder("../Paintings91/Quantizing8")
    # val_1 = 0
    # val_2 = 0
    # cnt =0
    # comp_list=[]
    # larg_list=[]
    # for x in im:
    #     a = x[0]
    #     b =x[1]
    #     if a>b:
    #         comprimento = x[0]
    #         largura = x[1]
    #     else:
    #         comprimento = x[1]
    #         largura = x[0]

    #     comp_list.append(comprimento)
    #     larg_list.append(largura)
    #     val_1=val_1 + comprimento
    #     val_2=val_2 + largura
    #     cnt+=1
    # print(val_1/cnt,val_2/cnt)
    # print(min(comp_list))



 