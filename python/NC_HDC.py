#!python
#!/usr/bin/env python
import numpy as np
import scipy.io
import sys
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random
import statistics
from plot_style import confidence_ellipse

class style():
    def __init__(self,list_data, index):
        style = filter_style_by_index(list_data,index)
        colors = ['#4682b4','#deb887','#FFFF00','#adff2f','k','#ff6347','k','#3cb371','k','k','#FFA500','k','#4B0082']
        self.author = extract(style,0)
        self.x_hdc = extract(style,3)
        self.y_nc = extract(style,2)
        self.c_authors = extract(style,2)
        self.c_style = colors[index]

class author():
    def __init__(self,style_authors_list, index_author, color_vector):
        author = filter_author_by_index(style_authors_list,index_author)
        self.author_name = extract(author,0)[0]
        self.style=extract(author,1)
        self.y_nc = extract(author,2)
        self.x_hdc = extract(author,3)
        self.c_authors = color_vector[index_author]
        # print(color_vector[index_author])
        self.c_style = color_vector[index_author]


def draw_confidence_ellipse(style,ax):
    confidence_ellipse(np.asarray(style.x_hdc), np.asarray(style.y_nc), ax,n_std=1, alpha=.7,facecolor=style.c_style, edgecolor=style.c_style)

def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    
    return unique_list

def get_index(array_index,filename):
    index=[]
    counter=0
    for label_list in array_index:
        index.append([filename[counter], label_list.tolist().index(1)])
        counter+=1
    return index
    
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

def filter_style_by_index(list_artist,index):
    return [artist for artist in list_artist if artist[1]==index]

def filter_author_by_index(list_artist,index):
    return [artist for artist in list_artist if artist[-1]==index]

def extract(lst, index): 
    return [item[index] for item in lst] 

def plot_scatter(style):
    return plt.scatter(style.x_hdc, style.y_nc, s=10, c=style.c_style, alpha=1)    

def make_plot(list_artists):
    plt.clf()
    style_list = unique([row[1] for row in list_artists ])
    S=[]    
    ax = plt.gca()
    ax.set_xlabel('HDC \u03B1')
    ax.set_ylabel('NC')

    values = [4,6,8,9,11]
    for style_id in style_list:

        if style_id not in values:
            style_group = style(list_artists,style_id)
            S.append(plot_scatter(style_group))
            draw_confidence_ellipse(style_group,ax)
    plt.legend(S,
    ['Abstract Expressionism','The Baroque','Constructivism',
    'Cubism','Neo Classical','Post Impressionism'
    ,'Romanticism','Symbolism'], bbox_to_anchor=(1.04,1), loc="upper left")
    # ['Abstract Expressionism','The Baroque','Constructivism',
    # 'Cubism','#Impressionism','Neo Classical','#Pop art','Post Impressionism',
    # '#Realism','#Renaissance','Romanticism','','Symbolism'])
    plt.xlim(0, 0.5)
    plt.ylim(0.4, 1)
    plt.gca().set_aspect('auto', adjustable='box')
    plt.savefig('../plots/hdc_nc.pdf', bbox_inches='tight') 

def filter_by_author(list_artist, list_reports):
    author_paintings=[]
    labeled_authors=[]
    author_average = []
    label = 0
    for author in list_artist:
        for report in list_reports:
            if author in report[0]:
                author_paintings.append(report)
                labeled_authors.append(report+[label])
        author_average.append(average_author(author, author_paintings))# this is average artists paintings for style
        author_paintings = []
        label+=1
    # [print(row) for row in author_average]
    return (author_average,labeled_authors)

def color(author_labeled_list):
    nb_authors = unique([row[-1] for row in author_labeled_list])
    return cm.rainbow(np.linspace(0, 1, len(nb_authors)))

def make_author_plot(authors_labeled_paintings,color_vector):
    style_list = unique([row[1] for row in authors_labeled_paintings ])
    for style in style_list:
        authors_paintings = [ painting for painting in authors_labeled_paintings if painting[1]==style]
        plot_author_list(authors_class_by_style(authors_paintings,color_vector))
    #filter by style
    #in each style
    
def authors_class_by_style(authors_labeled_paintings,color_vector):
    id_authors = unique([row[-1] for row in authors_labeled_paintings ])
    authors=[]
    for id_author in id_authors:
        authors.append(author(authors_labeled_paintings,id_author,color_vector))
    return authors
 
def plot_author_list(authors_list):
    ax = plt.gca()
    for author in authors_list:
        SC0=plot_scatter(author)
        draw_confidence_ellipse(author,ax)
    plt.show()


def average_author(author, author_paintings):
    nc_list = [row[2] for row in author_paintings]
    hdc_list = [row[3] for row in author_paintings]
    sum_nc_author =float(sum(nc_list))/len(nc_list)
    sum_hdc_author = float(sum(hdc_list))/len(hdc_list)
    avg = [author, author_paintings[1][1],sum_nc_author, sum_hdc_author]
    return avg

def Average(lst): 
    return sum(lst) / len(lst) 

def average_by_style(all_elem):
    label=0
    NC_values = []
    HDC_values = []
    avg_NC_style=[]
    avg_HDC_style=[]
    for value_list in all_elem:
        if label in value_list:
            NC_values.append(value_list[2])
            HDC_values.append(value_list[3])
        else:
            std_NC=statistics.stdev(NC_values)
            std_HDC=statistics.stdev(HDC_values)
            avg_NC = Average(NC_values)
            avg_HDC = Average(HDC_values)
            NC_values = []
            HDC_values = []
            avg_NC_style.append([label, avg_NC, std_NC])
            avg_HDC_style.append([label, avg_HDC, std_HDC ])
            label+=1    
    return avg_NC_style, avg_HDC_style
    
def plot_error_bar(avg_style,limit, lgnd):
    [print(a) for a in avg_style ]
    values = [4, 6, 8, 9, 11]
    colors = ['#4682b4','#deb887','#FFFF00','#adff2f','#ff6347','#3cb371','#FFA500','#4B0082']
    x = np.array([row[0] for row in avg_style if row[0] not in values])
    y = np.array([row[1] for row in avg_style if row[0] not in values])
    yerr = np.array([row[2] for row in avg_style if row[0] not in values])
    plt.clf()
    plt.ylim(limit[0],limit[1])
    plt.ylabel(lgnd)
    # plt.tick_params(
    # axis='x',          # changes apply to the x-axis
    # which='both',      # both major and minor ticks are affected
    # bottom=False,      # ticks along the bottom edge are off
    # top=False,         # ticks along the top edge are off
    # labelbottom=False) # labels along the bottom edge are off
    S=[]
    for x1 in range(x.size):
        S.append(plt.errorbar(x1,y[x1],yerr[x1], linestyle='None', marker='s',markerfacecolor=colors[x1],mec=colors[x1], ecolor='k', capsize=2, elinewidth=1.25,markeredgewidth=2.5))
    # plt.legend(S,
    # ['Abstract Expressionism','The Baroque','Constructivism',
    # 'Cubism','Neo Classical','Post Impressionism'
    # ,'Romanticism','Symbolism'], bbox_to_anchor=(1.04,1), loc="upper left")
    plt.xticks(list(range(x.size)), ['Abstract Expressionism','The Baroque','Constructivism',
    'Cubism','Neo Classical','Post Impressionism'
    ,'Romanticism','Symbolism'],rotation=30)
    plt.savefig("../plots/" + lgnd +'.pdf', bbox_inches='tight') 


if __name__ == "__main__":
    nc_report_path="../reports/REPORT_COMPLEXITY_NC_Quantizing8"
    hdc_report_path="../reports/REPORT_HDC_Quantizing8"
    nc_report = read_report(nc_report_path)
    hdc_report = read_report(hdc_report_path)

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
    all_elem = match_label(hdc_report, nc_report,label)
    # [print(a) for a in all_elem]
    avg_NC_style, HDC_values=average_by_style(all_elem)
    
    plot_error_bar(avg_NC_style,[0.4,1], 'NC')
    plot_error_bar(HDC_values,[0,0.6], 'HDC ⟨\u03B1⟩')
    author_name=unique(names)
    unchanged_author_name=unique(unchanged_names)
    
    author_average, labeled_authors = filter_by_author(unchanged_author_name, all_elem)
    print(author_average)
    
    # colorc = color(labeled_authors)
    # random.shuffle(colorc)
    # random.shuffle(colorc)
    make_plot(author_average)
    # make_author_plot(labeled_authors,colorc)
    
