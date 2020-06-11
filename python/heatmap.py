#!python
#!/usr/bin/env python

import numpy as np
import numpy.random
import seaborn as sb
import matplotlib.pyplot as plt
import sys
import matplotlib.pylab as plt

def mass_plotting(artists):
    for artist in artists:
        heatmap(artist)

def heatmap(artist):
    artist_name=artist[0]
    print(artist_name)
    unorder_values=artist[1:]
    values = reorder(unorder_values)
    array_n = array_n=[float(word) for word in values]
    array = np.asarray(array_n)
    #array2d = np.reshape(array,(8,8))
    array2d = np.reshape(array,(16,16))

    ticklabels = [idx for idx in range(1,17)]
    ax = sb.set(font_scale=1.2)
    cmap = sb.diverging_palette(220, 10, sep=80, as_cmap=True)
    ax = sb.heatmap(array2d, cmap="Reds",  linewidth=0.5, xticklabels=ticklabels, yticklabels=ticklabels, annot=False, cbar_kws={'label': 'Average Normalized Compression','orientation': 'vertical'})
    ax.set_title(artist_name.replace('_', ' ').title())
    save_name="../local_region_complexity_256/" + artist_name + ".pdf"
    fig = ax.get_figure()
    fig.savefig(save_name) 
    fig.clf()

def reorder(artist_list):
    # order=[0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 2, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 3, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 4, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 5, 60, 61, 62, 63, 6, 7, 8, 9]
    order_256=[0, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 10, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 11, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 12, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 13, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 14, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 15, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 16, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 17, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 18, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 19, 1, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 20, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 21, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 22, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 23, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 24, 250, 251, 252, 253, 254, 255, 25, 26, 27, 28, 29, 2, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 3, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 4, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 5, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 6, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 7, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 8, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 9]

    reorder_list=[None] * (len(order_256))
    for a in range(len(order_256)):
        reorder_list[order_256[a]]=artist_list[a]
    return reorder_list

if __name__ == "__main__":

    file = sys.argv[1]
    file1 = open(file, 'r') 
    lines = file1.readlines() 
    painters_average_s = []

    for x in lines:
            string_line = x.replace('\n', '').split('\t')
            painters_average_s.append(list(string_line))
            
    painters_average = []
    for painter in painters_average_s:
        p =[]
        for value in painter:
            if (value!=''):
                p.append(value)
        painters_average.append(p)
    mass_plotting(painters_average)
    sys.exit()


