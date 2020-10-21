#!python
#!/usr/bin/env python
import numpy as np
import statistics
from string import digits

def process_alpha(file_to_read):
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
        values_image.append(float(image[0]))

    #alpha_value=np.array(values_image).astype('float32')
    #classes=np.array(classes).astype('int32')
    return classes, values_image

def process_nc(file_to_read):
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
        res = author.translate(remove_digits).replace('.jpg.pgm.PROCESSED.bin :', '').replace('_', ' ').title()
        image = image[1:]       
        if(painter != res):
            painter = res
            number += 1
        classes.append(number)
        values_image.append(float(image[0]))

    #alpha_value=np.array(values_image).astype('float32')
    #classes=np.array(classes).astype('int32')
    return classes, values_image


def avg_author (classes, alpha_value):
    val=classes[0]
    last_value=alpha_value[-1]
    last_class=classes[-1]
    avg = []
    group=[]
    for pair in zip(classes, alpha_value):
        if val ==pair[0]:

            group.append(pair[1])
        elif val !=pair[0] or (pair[0] == last_class and pair[1] == last_value):
            # std.append(statistics.stdev(group))
            avg.append(statistics.mean(group))
            author =[]
            val = pair[0]
    return avg

def avg_std(normalized, other):
    diff=[abs(a-b) for a,b in zip(other, normalized)]
    PERCENT_DIFF = [(abs(a-b)/((a+b)/2))*100 for a,b in zip(other, normalized)]
    avg = statistics.mean(diff)
    std = statistics.stdev(diff)
    avg_percent = statistics.mean(PERCENT_DIFF)
    std_percent = statistics.stdev(PERCENT_DIFF)
    return avg, std , avg_percent, std_percent
    
if __name__ == "__main__":
    file_1 = open("../reports/REPORT_HDC_Quantizing8", 'r', encoding='iso-8859-1')
    classes, alpha_value = process_alpha(file_1)
    alpha_avg_per_author = avg_author(classes, alpha_value)
    file_2 = open("../reports/REPORT_HDC_normalize_Quantizing8", 'r', encoding='iso-8859-1')
    classes, alpha_value = process_alpha(file_2)
    alpha_normalized_avg_per_author = avg_author(classes, alpha_value)
    avg, std, p_avg, p_std = avg_std(alpha_normalized_avg_per_author,alpha_avg_per_author)
    print("Apha Author Difference = ", avg, "+/-", std)
    print("Apha Author Mean Percentage Difference = ", p_avg, "% +/-", std, "%")

    file_1 = open("../reports/REPORT_COMPLEXITY_NC_Quantizing8", 'r', encoding='iso-8859-1')
    classes, nc_value = process_nc(file_1)
    nc_avg_per_author = avg_author(classes, nc_value)

    file_2 = open("../reports/REPORT_COMPLEXITY_NC_NORMAL_normalize_Quantizing8", 'r', encoding='iso-8859-1')
    classes, normalized_nc_value = process_nc(file_2)
    nc_normalized_avg_per_author = avg_author(classes, normalized_nc_value)

    avg, std, p_avg, p_std = avg_std(nc_normalized_avg_per_author,nc_avg_per_author)
    print("NC Author Difference = ", avg, "+/-", std)
    print("NC Author Mean Percentage Difference = ", p_avg, "% +/-", std, "%")

    ######## NBDM1 ########

    file_1 = open("../reports/REPORT_COMPLEXITY_NBDM1_Quantizing8", 'r', encoding='iso-8859-1')
    classes, nbdm1_value = process_nc(file_1)
    nbdm1_avg_per_author = avg_author(classes, nbdm1_value)

    file_2 = open("../reports/REPORT_COMPLEXITY_NBDM1_NORMAL_normalize_Quantizing8", 'r', encoding='iso-8859-1')
    classes, normalized_nbdm1_value = process_nc(file_2)
    nbdm1_normalized_avg_per_author = avg_author(classes, normalized_nbdm1_value)

    avg, std, p_avg, p_std = avg_std(nbdm1_normalized_avg_per_author,nbdm1_avg_per_author)
    print("NBDM1 Author Difference = ", avg, "+/-", std)
    print("NBDM1 Author Mean Percentage Difference = ", p_avg, "% +/-", std, "%")

    ######## NBDM2 ########

    file_1 = open("../reports/REPORT_COMPLEXITY_NBDM2_Quantizing8", 'r', encoding='iso-8859-1')
    classes, nbdm2_value = process_nc(file_1)
    nbdm2_avg_per_author = avg_author(classes, nbdm2_value)

    file_2 = open("../reports/REPORT_COMPLEXITY_NBDM2_NORMAL_normalize_Quantizing8", 'r', encoding='iso-8859-1')
    classes, normalized_nbdm2_value = process_nc(file_2)
    nbdm2_normalized_avg_per_author = avg_author(classes, normalized_nbdm2_value)

    avg, std, p_avg, p_std = avg_std(nbdm2_normalized_avg_per_author,nbdm2_avg_per_author)
    print("NBDM2 Author Difference = ", avg, "+/-", std)
    print("NBDM2 Author Mean Percentage Difference = ", p_avg, "% +/-", std, "%")