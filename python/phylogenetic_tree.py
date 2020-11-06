#!python
#!/usr/bin/env python
import sys
import os
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceMatrix, DistanceTreeConstructor
from Bio import AlignIO
from Bio import Phylo
import math
from matplotlib import pyplot as plt
import pylab
import numpy as np
from scipy import spatial
from ete3 import Tree, TreeStyle, TextFace, NodeStyle, faces, RectFace, CircleFace, ImgFace
from os import path
from glob import glob  
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from networkx.drawing.nx_pylab import draw_networkx
import networkx as nx
from ete3 import add_face_to_node


def compute_minimum_spanning_tree(file_name, artists, distance_matrix, authors, styles,list_period_color):
    dst_list =[]
    
    max = len(distance_matrix[-1])
    for line in distance_matrix:
        remain = max - len(line)
        dst_list.append( line + [0.0] *remain)

    G = np.array(dst_list)
    Tcsr = minimum_spanning_tree(G)       
    G = nx.Graph(Tcsr)
    
    elst = bfs_edge_lst(G, 1)
    tree = tree_from_edge_lst(elst)
    newick_minimum_spanning_tree = tree_to_newick(tree) + ';'
    
    t = Tree(newick_minimum_spanning_tree)
    vl = []
    for node in t.traverse("postorder"):
        if node.is_leaf():
            name =artists[int(node.name)]
            node.name = name
        else:
            name = artists[int(node.support)]
            node.name = name
        vl.append(node.name)

    ts = TreeStyle()
    ts,t = set_default_TreeStyle(t)

    def my_layout(node):
        F = TextFace("\t"+node.name, tight_text=True,fstyle="bold", fsize=40, fgcolor="black")
        F.rotation = 90
        add_face_to_node(F, node, column=0, position="branch-bottom")

    ts.layout_fn = my_layout
    list_of_nodes ={}
   

    for author in authors:
        for node in t.traverse("postorder"):
            if (node.name == author):
                    new_dic = get_sister_common_styles(node, artists, styles)
        list_of_nodes.update(new_dic)
   
    prevalent_dict = most_prevalent(list_of_nodes)

    for author in authors:
        for node in t.traverse("postorder"):
            if (node.name == author):
                attribute_legend(node, authors,styles)
                add_painting(node, im, basename)
    
    savename_period = "../plots/" + file_name + "Kruskal_minimum_spanning_tree.pdf"
    t.render(savename_period,tree_style=ts)

def find_ext(dr, ext):
    return glob(path.join(dr,"*.{}".format(ext)))

def readlabelfile(filename):
    file1 = open(filename, 'r') 
    lines = file1.readlines() 
    values = []
    for x in lines:
        string_line = x.replace('\n', '').split('\t')
        values.append(list(string_line))

    return values

def readfile(filename):
    file1 = open(filename, 'r') 
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
    
    artists_average = []

    for painter in painters_average:
        name = painter[0]
        values = painter[1:]
        values = [float(value) for value in values]
        artists_average.append([name] + values)
    
    return artists_average


def create_distance_matrix_sq(region_nc):
    distance_matrix = []
    artists=[]
    counter=0
    for artist1 in region_nc:
        line=[]
        artists.append(artist1[0].title().replace('_', ' '))
        for artist2 in region_nc:
            region_nc_artist1=reorder_256(artist1[1:])
            region_nc_artist2=reorder_256(artist2[1:])
            diff =  math.sqrt(sum([(a_i - b_i)**2 for a_i, b_i in zip(region_nc_artist1, region_nc_artist2)]))
            line.append(diff)
        distance_matrix.append(line[0:counter+1])
        #distance_matrix.append(line)
        counter+=1
    artists[-1]="Edouard Manet"
    return artists, distance_matrix

def reorder_256(artist_list):
    # order=[0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 2, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 3, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 4, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 5, 60, 61, 62, 63, 6, 7, 8, 9]
    order_256=[0, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 10, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 11, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 12, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 13, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 14, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 15, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 16, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 17, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 18, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 19, 1, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 20, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 21, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 22, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 23, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 24, 250, 251, 252, 253, 254, 255, 25, 26, 27, 28, 29, 2, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 3, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 4, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 5, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 6, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 7, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 8, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 9]

    reorder_list=[None] * (len(order_256))
    for a in range(len(order_256)):
        reorder_list[order_256[a]]=artist_list[a]
    return reorder_list

def create_distance_matrix(region_nc):
    distance_matrix = []
    artists=[]
    counter=0
    for artist1 in region_nc:
        line=[]
        artists.append(artist1[0].title().replace('_', ' '))
        for artist2 in region_nc:
            region_nc_artist1=reorder_256(artist1[1:])
            region_nc_artist2=reorder_256(artist2[1:])
            diff =  sum([abs(a_i - b_i) for a_i, b_i in zip(region_nc_artist1, region_nc_artist2)])
            line.append(diff)
        distance_matrix.append(line[0:counter+1])
        #distance_matrix.append(line)
        counter+=1
    artists[-1]="Edouard Manet"
    return artists, distance_matrix

def create_distance_matrix_cosine(region_nc):
    distance_matrix = []
    artists=[]
    counter=0
    for artist1 in region_nc:
        line=[]
        artists.append(artist1[0].title().replace('_', ' '))
        for artist2 in region_nc:
            region_nc_artist1=reorder_256(artist1[1:])
            region_nc_artist2=reorder_256(artist2[1:])
            diff = 1 - spatial.distance.cosine(region_nc_artist1, region_nc_artist2)
            line.append(diff)
        distance_matrix.append(line[0:counter+1])
        #distance_matrix.append(line)
        counter+=1
    artists[-1]="Edouard Manet"
    return artists, distance_matrix

def create_distance_matrix_max(region_nc):
    distance_matrix = []
    artists=[]
    counter=0
    for artist1 in region_nc:
        line=[]
        artists.append(artist1[0].title().replace('_', ' '))
        for artist2 in region_nc:
            region_nc_artist1=reorder_256(artist1[1:])
            region_nc_artist2=reorder_256(artist2[1:])
            diff =  [abs(a_i - b_i) for a_i, b_i in zip(region_nc_artist1, region_nc_artist2)]
            diff = max(diff)
            line.append(diff)
        distance_matrix.append(line[0:counter+1])
        #distance_matrix.append(line)
        counter+=1
    artists[-1]="Edouard Manet"
    return artists, distance_matrix

def set_default_TreeStyle(tree):
    ts = TreeStyle()
    ts.mode = "c"
    ts.root_opening_factor = 1
    ts.show_branch_length = True
    ts.show_branch_support = True
    ts.force_topology = True
    ts.show_leaf_name = False
    ts.min_leaf_separation=10
    ts.root_opening_factor=1
    ts.complete_branch_lines_when_necessary=True
    ns=NodeStyle()
    ns["size"] = 6
    ns["fgcolor"] = "Black"
    ns["hz_line_width"] = 8
    ns["vt_line_width"] = 8

    for node in tree.traverse("postorder"):
        # if not node.is_leaf():
        node.set_style(ns)

    tree.set_style(ts)
    return ts, tree

def set_date_artist_color(name,tree_date, list_period_date,list_date_color):
    ts, tree_date = set_default_TreeStyle(tree_date)

    for row in list_period_date:
        leaf_date = tree_date.get_leaves_by_name(row[0])
        date = float(row[1].replace(',', '.'))
        color_date = get_date_color(list_date_color, date)
        leaf_date[0] = attribute_color(leaf_date[0],color_date)

    tree_date.set_style(ts)
    savename_date= "../plots/" + name + "_date.pdf"
    ts.show_leaf_name = False
    tree_date.render(savename_date,tree_style=ts, dpi=1500,w=600)

def set_period_artist_color(name,tree_period, list_period_color, styles, authors, im, basename):
    ts,tree_period = set_default_TreeStyle(tree_period)
    list_of_nodes ={}

    for author in authors:
        leaf_period = tree_period.get_leaves_by_name(author)
        new_dic = get_sister_common_styles(leaf_period[0], authors,styles)
        list_of_nodes.update(new_dic)

    for author in authors:
        leaf_period = tree_period.get_leaves_by_name(author)
        new_dic = get_common_styles(leaf_period[0], authors,styles,list_of_nodes)
        list_of_nodes.update(new_dic)

    prevalent_dict = most_prevalent(list_of_nodes)

    for author in authors:
        leaf_period = tree_period.get_leaves_by_name(author)
        leaf_period[0], p = attribute_color_2(leaf_period[0], list_of_nodes, prevalent_dict, list_period_color)
        attribute_legend(leaf_period[0], authors,styles)
        add_painting(leaf_period[0], im, basename)
    
    ts = legend(ts,list_period_color)  
    savename_period = "../plots/" + name + "_period_final.pdf"
    tree_period.render(savename_period,tree_style=ts, dpi=5000,w=60000)

def legend(style, color_list):
    for row in color_list:
        style.legend.add_face(CircleFace(100, row[1]), column=0)
        style.legend.add_face(TextFace("  " + row[0], fgcolor="Black", fsize=35,bold=True), column=1)
    return style

def most_prevalent(dict_styles):
    l = dict_styles.values()
    flat_list = [item for sublist in l for item in sublist]
    occurrence = [[x,flat_list.count(x)] for x in set(flat_list)]
    occurrence.sort(key=lambda x: x[1], reverse=True)
    return occurrence

def attribute_legend(node, authors,styles):
    indx1 = authors.index(node.name)
    author_styles = styles[indx1]
    text = "  "
    counter = 0
    for style in author_styles:
        if counter%2==0:
            text+="  \n  "
        counter += 1
        text += style + ", "

    text=text[:-2]
    text = "  " + text
    #F = TextFace(node.name, tight_text=True, fsize=15, fgcolor="white")
    #add_face_to_node(F, node, column=0, position="branch-right")
    N = TextFace(text, fgcolor="Black", fsize=21,fstyle="bold",bold=False, tight_text=False)
    if not node.is_leaf():
        N.rotation = 90
    
    Nspace =  TextFace("  ", fgcolor="Black", fsize=21,bold=True)
    node.add_face(face=Nspace, column=1)
    node.add_face(face=N, column=2)


def add_painting(node, im, basename):
    filename =""
    for pathname, auth_name in zip(im, basename):
        if node.name == auth_name:
            filename = pathname
    I = ImgFace(filename, width=150, height=150, is_url=False)
    if not node.is_leaf:
        I.rotation = 90
    node.add_face(face=I, column=0)


def get_sister_common_styles(node, authors,styles):
    list_of_nodes = {}
    sister = node.get_sisters()
    if not sister:
        ancestor = node.get_ancestors()
        child = node.get_children()
        if not ancestor:
            close_node = child[0]
        elif not child:
            close_node = ancestor[0]
        else:
            dist_father=node.get_distance(child[0])
            dist_child=node.get_distance(ancestor[0])
            if dist_father<=dist_child:
                close_node = ancestor[0]
            else:
                close_node=child[0]
        indx1 = authors.index(node.name)
        indx2 = authors.index(close_node.name)
        list_of_nodes={}
        ext = get_common_element(styles[indx1],styles[indx2])
        if not ext:
            list_of_nodes[node.name]=styles[indx1]
            list_of_nodes[close_node.name]=styles[indx2]
        elif ext :
            list_of_nodes[node.name]=ext
            list_of_nodes[close_node.name]=ext
        else: 
            print("ERROR!!")

    elif not "Inner" in sister[0].name:
        sister_node = sister[0]
        indx1 = authors.index(node.name)
        indx2 = authors.index(sister_node.name)
        list_of_nodes={}
        ext = get_common_element(styles[indx1],styles[indx2])
        if not ext:
            list_of_nodes[node.name]=styles[indx1]
            list_of_nodes[sister_node.name]=styles[indx2]
        elif ext :
            list_of_nodes[node.name]=ext
            list_of_nodes[sister_node.name]=ext
        else: 
            print("ERROR!!")
            sys.exit()
    return list_of_nodes

def get_common_styles(node, authors, styles, list_of_nodes):
    list_nodes ={}
    sister = node.get_sisters()
    indx1 = authors.index(node.name)
    list_style_node = styles[indx1]
    # close_node =node
    if not sister:
        ancestor = node.get_ancestors()
        child = node.get_children()
        if not ancestor:
            close_node = child[0]
        elif not child:
            close_node = ancestor[0]
        else:
            dist_father=node.get_distance(child[0])
            dist_child=node.get_distance(ancestor[0])
            if dist_father<=dist_child:
                close_node = ancestor[0]
            else:
                close_node=child[0]
        
        if  close_node.name in list_of_nodes:
                list_style_node_close = list_of_nodes.get(close_node.name)
        else:
            indx2 = authors.index(close_node.name)
            list_style_node_close = styles[indx2]
    
        ext = get_common_element(list_style_node,list_style_node_close)
        if not ext:
            list_nodes[node.name]=list_style_node
            list_nodes[close_node.name]=list_style_node_close
        elif ext :
            list_nodes[node.name]=ext
            list_nodes[close_node.name]=ext
        else: 
            print("ERROR!!")
            sys.exit()
    else:
        if "Inner" in sister[0].name:
            close_node = sister[0].get_closest_leaf()
            if  close_node[0].name in list_of_nodes:
                list_style_node_close = list_of_nodes.get(close_node[0].name)
            else:
                indx2 = authors.index(close_node[0].name)
                list_style_node_close = styles[indx2]
        
            ext = get_common_element(list_style_node,list_style_node_close)
            if not ext:
                list_nodes[node.name]=list_style_node
                list_nodes[close_node[0].name]=list_style_node_close
            elif ext :
                list_nodes[node.name]=ext
                list_nodes[close_node[0].name]=ext
            else: 
                print("ERROR!!")
                sys.exit()
        return list_nodes

def get_common_element(list1,list2):
    list1_as_set = set(list1)
    intersection = list1_as_set.intersection(list2)
    intersection_as_list = list(intersection)
    if not intersection_as_list:
        return []
    else:
        return intersection_as_list

def attribute_color(node,color):
    node_style=NodeStyle()
    node_style["fgcolor"] = color
    textcolor = "Black"
    node_style["bgcolor"] = color
    if color=="Black":
        textcolor ="White"
    N =  TextFace(node.name, fgcolor=textcolor, fsize=50,bold=True)
    node.add_face(face=N, column=0)
    node.allow_face_overlap=True
    node.set_style(node_style)
    return node

def attribute_color_2(node, dictionary, common_dict, list_color):
    
    node_style=NodeStyle()
    list_of_styles = dictionary.get(node.name)
    color,p = get_color_2(list_of_styles, common_dict, list_color)
    p = p + " -> " + color
    node_style["fgcolor"] = color
    textcolor = "Black"
    node_style["bgcolor"] = color
    if color=="Black":
        textcolor ="White"
    
    text_extra = "  " 
    text = text_extra + node.name + text_extra
    N =  TextFace(text, fgcolor=textcolor, fsize=30,bold=True)
    Nspace =  TextFace("  ", fgcolor=textcolor, fsize=30,bold=True)
    node.add_face(face=Nspace, column=1)
    node.add_face(face=N, column=2)
    node.allow_face_overlap=True
    node.set_style(node_style)
    return node,p
    
def get_color_2(list_of_styles, dict_most_common, list_color):
    period =""
    occurrance = 0
    for style in list_of_styles:
        if get_occurrence(dict_most_common, style) > occurrance:
            occurrance = get_occurrence(dict_most_common, style)
            period = style
    
    for row in list_color:
            if row[0].lower()==period.lower():
                return row[1],period

def get_date_color(list_date_color, date):
    for row in list_date_color:
        year = float(row[0])
        if year>=date:
            return row[1]

def get_occurrence(list_of_lists, period):
    for row in list_of_lists:
            if row[0].lower()==period.lower():
                return row[1]

def get_color(list_color, period):
    for row in list_color:
        if row[0].lower()==period.lower():
            return row[1]
            
def get_styles_filtered(all_styles,unique_styles):
    authors = [row[0]for row in all_styles]
    st = [list(filter(None, row[1:])) for row in all_styles]
    sts=[]
    for styles in st:
        sd =[]
        for s in styles:
            if "Renaissance" in s:
                s= "Renaissance"
            sd.append(s)
        sts.append(list(set(sd)))
    st= sts
    sts =[]
    for styles in st:
        result = [x for x in styles if x in unique_styles]
        sts.append(result)
    return sts

#########################################
def recursive_search(dict, key):
    if key in dict:
        return dict[key]
    for k, v in dict.items():
        item = recursive_search(v, key)
        if item is not None:
            return item

def bfs_edge_lst(graph, n):
    return list(nx.bfs_edges(graph, n))

def tree_from_edge_lst(elst):
    tree = {1: {}}
    for src, dst in elst:
        subt = recursive_search(tree, src)
        subt[dst] = {}
    return tree

def tree_to_newick(tree):
    items = []
    for k in tree.keys():
        s = ''
        if len(tree[k].keys()) > 0:
            #print(k) #debugging
            subt = tree_to_newick(tree[k])
            if subt != '':
                s += '(' + str(subt) + ')'
        s += str(k)
        items.append(s)
    return ','.join(items)


################################


if __name__ == "__main__":
    im  = find_ext("../aux/Img","jpg")
    im =list(filter(lambda k: '_20.jpg' in k, im))
    basename = [os.path.basename(path).replace("_20.jpg","").replace("\udcc9DOUARD_MANET","EDOUARD_MANET").replace("\x89","").replace("_"," ").title() for path in im]
    date_color = readlabelfile("../aux/date_color")
    period_color = readlabelfile("../aux/period_color")
    artist_period = readlabelfile("../aux/artist_period")
    styles = readlabelfile("../aux/AS")
    all_styles = readlabelfile("../aux/author_styles")
    
    st = [list(filter(None, row[1:])) for row in styles]
    styles_considered_list = [item for sublist in st for item in sublist]
    st = get_styles_filtered(all_styles,styles_considered_list)
    authors = [row[0]for row in styles]
    filename = "../reports/REPORT_AVG_REGIONAL_COMPLEXITY_PER_BLOCK_256"
    region_nc = readfile(filename)
    artists,distance_matrix = create_distance_matrix(region_nc)
    
    compute_minimum_spanning_tree("",artists, distance_matrix, authors, st,period_color )
    calculator = DistanceCalculator('identity')
    dm = DistanceMatrix(names=artists, matrix=distance_matrix)
    constructor = DistanceTreeConstructor()
    tree_nj = constructor.nj(dm)
    tree_upgma = constructor.upgma(dm)

    Phylo.write(tree_nj, '../aux/tree_nj.nhx', 'newick')
    Phylo.write(tree_upgma, '../aux/tree_upgma.nhx', 'newick')
    
    tree_period_nj = Tree("../aux/tree_nj.nhx", quoted_node_names=True, format=1)
    tree_date_nj = Tree('../aux/tree_nj.nhx', quoted_node_names=True, format=1)

    set_period_artist_color("t_nj",tree_period_nj, period_color,st,authors,im, basename)
    set_date_artist_color("t_nj",tree_date_nj, artist_period, date_color)
  
    tree_period_upgma = Tree('../aux/tree_upgma.nhx', quoted_node_names=True, format=1)
    tree_date_upgma = Tree('../aux/tree_upgma.nhx', quoted_node_names=True, format=1)
    set_period_artist_color("t_upgma",tree_period_upgma, period_color,st,authors,im, basename)
    set_date_artist_color("t_upgma",tree_date_upgma, artist_period, date_color)
 
    ############################ Normalized Values ########################################    
    filename = "../reports/REPORT_AVG_REGIONAL_COMPLEXITY_NORMALIZED_PER_BLOCK_256"
    region_nc = readfile(filename)

    artists,distance_matrix_normalized = create_distance_matrix(region_nc)

    compute_minimum_spanning_tree("normalized_",artists, distance_matrix_normalized, authors, st, period_color)
    calculator = DistanceCalculator('identity')
    dm = DistanceMatrix(names=artists, matrix=distance_matrix_normalized)
    constructor = DistanceTreeConstructor()
    tree_nj = constructor.nj(dm)
    tree_upgma = constructor.upgma(dm)

    Phylo.write(tree_nj, '../aux/tree_nj_normalized.nhx', 'newick')
    Phylo.write(tree_upgma, '../aux/tree_upgma_normalized.nhx', 'newick')
    
    tree_period_nj = Tree("../aux/tree_nj_normalized.nhx", quoted_node_names=True, format=1)
    tree_date_nj = Tree('../aux/tree_nj_normalized.nhx', quoted_node_names=True, format=1)

    set_period_artist_color("t_nj_normalized",tree_period_nj, period_color,st,authors,im, basename)
    set_date_artist_color("t_nj_normalized",tree_date_nj, artist_period, date_color)

    tree_period_upgma = Tree('../aux/tree_upgma_normalized.nhx', quoted_node_names=True, format=1)
    tree_date_upgma = Tree('../aux/tree_upgma_normalized.nhx', quoted_node_names=True, format=1)
    
    set_period_artist_color("../aux/t_upgma_normalized",tree_period_upgma, period_color,st,authors,im, basename)
    set_date_artist_color("../aux/t_upgma_normalized",tree_date_upgma, artist_period, date_color)