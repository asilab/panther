#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from matplotlib.patches import Ellipse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
#import matplotlib.axes.Axes as axes

class data_class():
    def __init__(self,list_data, color):
        self.author = extract(list_data,0)
        self.x_hdc = to_int(extract(list_data,1))
        self.y_nc = to_int(extract(list_data,3))
        self.c_authors = extract(list_data,2)
        self.c_style = color

def extract(lst, index): 
    return [item[index] for item in lst] 

def to_int(lst):
    return [ float(x) for x in lst ]

def draw_confidence_ellipse(data_class,ax):
    confidence_ellipse(np.asarray(data_class.x_hdc), np.asarray(data_class.y_nc), ax, alpha=.7,facecolor=data_class.c_style, edgecolor=data_class.c_style)

def confidence_ellipse(x, y, ax, n_std=1, facecolor='none', **kwargs):
    """
    Create a plot of the covariance confidence ellipse of `x` and `y`

    Parameters
    ----------
    x, y : array_like, shape (n, )
        Input data.

    ax : matplotlib.axes.Axes
        The axes object to draw the ellipse into.

    n_std : float
        The number of standard deviations to determine the ellipse's radiuses.

    Returns
    -------
    matplotlib.patches.Ellipse

    Other parameters
    ----------------
    kwargs : `~matplotlib.patches.Patch` properties
    """
    print(x,"\n", y)
    #print(x[0]-x[1],"\n", y)
    print("\n\n\n")
    if x.size != y.size:
        raise ValueError("x and y must be the same size")

    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    # Using a special case to obtain the eigenvalues of this
    # two-dimensionl dataset.
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0),
        width=ell_radius_x * 2,
        height=ell_radius_y * 2,
        facecolor=facecolor,
        **kwargs)

    # Calculating the stdandard deviation of x from
    # the squareroot of the variance and multiplying
    # with the given number of standard deviations.
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    # calculating the stdandard deviation of y ...
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)

    transf = transforms.Affine2D() \
        .rotate_deg(45) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)


if __name__ == "__main__":
    #
    file = 'FINAL'
    f=open(file,"r")
    lines=f.readlines()
    result=[]
    line=[]
    for x in lines:
        string_line = x.replace('\n', '').split('\t')
        result.append(list(string_line))
    sorted_results = sorted(result, key = lambda x: x[4])
    value=sorted_results[0][4]
    new_list=[]
    separated_results=[]
    for l in sorted_results:
        if l[4]==value:
            new_list.append(l)
        else:  
            separated_results.append(new_list)
            value = l[4]
            new_list=[]
            new_list.append(l)
    f.close()
    colors = ['b','g','k', 'c', 'y', 'm', 'r','teal','pink', 'forestgreen', 'dimgrey','lime','crimson']
    postImpressionism = data_class(separated_results[0],colors[0])
    baroque = data_class(separated_results[1],colors[1])
    realism = data_class(separated_results[2],colors[2])
    renaissance = data_class(separated_results[3],colors[3])
    surrealism = data_class(separated_results[4],colors[4])
    cubism = data_class(separated_results[5],colors[5])
    romanticism = data_class(separated_results[6],colors[6])
    abstractExpressionism = data_class(separated_results[7],colors[7])
    symbolism = data_class(separated_results[8],colors[8])
    constructivism = data_class(separated_results[9],colors[9])
    neoExpressionism = data_class(separated_results[10],colors[10])
    impressionism = data_class(separated_results[11],colors[11])
    neoClassical = data_class(separated_results[12],colors[12])

    ax = plt.gca()
    PI = plt.scatter(postImpressionism.x_hdc, postImpressionism.y_nc, s=50, c=postImpressionism.c_style, alpha=0.5)    
    BA = plt.scatter(baroque.x_hdc, baroque.y_nc, s=50, c=baroque.c_style, alpha=0.8)
    REAL = plt.scatter(realism.x_hdc, realism.y_nc, s=50, c=realism.c_style, alpha=0.8)
    REN = plt.scatter(renaissance.x_hdc, renaissance.y_nc, s=50, c=renaissance.c_style, alpha=0.8)
    SUR = plt.scatter(surrealism.x_hdc, surrealism.y_nc, s=50, c=surrealism.c_style, alpha=0.8)
    CUB = plt.scatter(cubism.x_hdc, cubism.y_nc, s=50, c=cubism.c_style, alpha=0.8)
    ROM = plt.scatter(romanticism.x_hdc, romanticism.y_nc, s=50, c=romanticism.c_style, alpha=0.8)
    AbEx = plt.scatter(abstractExpressionism.x_hdc, abstractExpressionism.y_nc, s=50, c=abstractExpressionism.c_style, alpha=0.8)
    Sym = plt.scatter(symbolism.x_hdc, symbolism.y_nc, s=50, c=symbolism.c_style, alpha=0.8)
    Cons = plt.scatter(constructivism.x_hdc, constructivism.y_nc, s=50, c=constructivism.c_style, alpha=0.8)
    NE = plt.scatter(neoExpressionism.x_hdc, neoExpressionism.y_nc, s=50, c=neoExpressionism.c_style, alpha=0.8)
    IMP = plt.scatter(impressionism.x_hdc, impressionism.y_nc, s=50, c=impressionism.c_style, alpha=0.8)
    NC = plt.scatter(neoClassical.x_hdc, neoClassical.y_nc, s=50, c=neoClassical.c_style, alpha=0.8)
    
    draw_confidence_ellipse(postImpressionism,ax)
    draw_confidence_ellipse(baroque,ax)
    draw_confidence_ellipse(realism,ax)
    draw_confidence_ellipse(renaissance,ax)
    draw_confidence_ellipse(surrealism,ax)
    draw_confidence_ellipse(cubism,ax)
    draw_confidence_ellipse(romanticism,ax)
    draw_confidence_ellipse(abstractExpressionism,ax)
    #draw_confidence_ellipse(symbolism,ax)
    draw_confidence_ellipse(constructivism,ax)
    #draw_confidence_ellipse(neoExpressionism,ax)
    draw_confidence_ellipse(impressionism,ax)
    draw_confidence_ellipse(neoClassical,ax)

    plt.legend([PI,BA,REAL,REN,SUR,CUB,ROM,AbEx,Sym,Cons,NE,IMP,NC],
     ['Post Impressionism','Baroque','Realism','Renaissance',
     'Surrealism','Cubism','Romanticism','Abstract Expressionism','Symbolism',
     'Constructivism','Neo Expressionism','Impressionism','Neo Classical'])
    plt.show()