from skbio import DistanceMatrix as DM
from skbio.stats.distance import mantel
import statistics

def average_and_std(lst): 
    mean = statistics.mean(lst)
    std = statistics.stdev(lst)
    return mean, std



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

def reorder_256(artist_list):
    order_256=[0, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 10, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 11, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 12, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 13, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 14, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 15, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 16, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 17, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 18, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 19, 1, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 20, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 21, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 22, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 23, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 24, 250, 251, 252, 253, 254, 255, 25, 26, 27, 28, 29, 2, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 3, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 4, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 5, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 6, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 7, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 8, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 9]
    reorder_list=[None] * (len(order_256))
    for a in range(len(order_256)):
        reorder_list[order_256[a]]=artist_list[a]
    return reorder_list

def reorder_64(artist_list):
    order_64=[0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 2, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 3, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 4, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 5, 60, 61, 62, 63, 6, 7, 8, 9]
    reorder_list=[None] * (len(order_64))
    for a in range(len(order_64)):
        reorder_list[order_64[a]]=artist_list[a]
    return reorder_list

def reorder_1024(artist_list):
    order_1024=[0, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 100, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 101, 1020, 1021, 1022, 1023, 102, 103, 104, 105, 106, 107, 108, 109, 10, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 11, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 12, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 13, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 14, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 15, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 16, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 17, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 18, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 19, 1, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 20, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 21, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 22, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 23, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 24, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 25, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 26, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 27, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 28, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 29, 2, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 30, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 31, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 32, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 33, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 34, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 35, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 36, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 37, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 38, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 39, 3, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 40, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 41, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 42, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 43, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 44, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 45, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 46, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 47, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 48, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 49, 4, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 50, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 51, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 52, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 53, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 54, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 55, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 56, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 57, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 58, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 59, 5, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 60, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 61, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 62, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 63, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 64, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 65, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 66, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 67, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 68, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 69, 6, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 70, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 71, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 72, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 73, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 74, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 75, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 76, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 77, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 78, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 79, 7, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 80, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 81, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 82, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 83, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 84, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 85, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 86, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 87, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 88, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 89, 8, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 90, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 91, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 92, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 93, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 94, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 95, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 96, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 97, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 98, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 99, 9] 
    reorder_list=[None] * (len(order_1024))
    for a in range(len(order_1024)):
        reorder_list[order_1024[a]]=artist_list[a]
    return reorder_list

def create_distance_matrix(region_nc, level):
    distance_matrix = []
    artists=[]
    counter=0
    for artist1 in region_nc:
        line=[]
        artists.append(artist1[0].title().replace('_', ' '))
        for artist2 in region_nc:
            if level==64:
                region_nc_artist1=reorder_64(artist1[1:])
                region_nc_artist2=reorder_64(artist2[1:])
            elif level==256:
                region_nc_artist1=reorder_256(artist1[1:])
                region_nc_artist2=reorder_256(artist2[1:])
            elif level==1024:
                region_nc_artist1=reorder_1024(artist1[1:])
                region_nc_artist2=reorder_1024(artist2[1:])
            else:
                sys.exit("ERROR")
            diff =  sum([abs(a_i - b_i) for a_i, b_i in zip(region_nc_artist1, region_nc_artist2)])
            line.append(diff)
        distance_matrix.append(line)
        #distance_matrix.append(line)
        counter+=1
    artists[-1]="Edouard Manet"
    return artists, distance_matrix

def get_avg_std(dist_1,dist_2):
    cumulative_mod =[]
    for lines in zip(dist_1,dist_2):
        for val in zip(lines[0],lines[1]):
            if val[0]!=0 and val[1]!=0:
                cumulative_mod.append(abs(val[0]-val[1]))       
        return average_and_std(cumulative_mod)

if __name__ == "__main__":
    filename_64 ="../reports/REPORT_AVG_REGIONAL_COMPLEXITY_PER_BLOCK_64"
    filename_256 = "../reports/REPORT_AVG_REGIONAL_COMPLEXITY_PER_BLOCK_256"
    filename_1024 ="../reports/REPORT_AVG_REGIONAL_COMPLEXITY_PER_BLOCK_1024"
    normalized_file_256 = "../reports/REPORT_AVG_REGIONAL_COMPLEXITY_NORMALIZED_PER_BLOCK_256"

    regional_nc_64 = readfile(filename_64)
    regional_nc_256 = readfile(filename_256)
    regional_nc_1024 = readfile(filename_1024)
    normalized_regional_nc_256 = readfile(normalized_file_256)

    artists,distance_matrix_64 = create_distance_matrix(regional_nc_64, 64)
    artists,distance_matrix_256 = create_distance_matrix(regional_nc_256, 256)
    artists,distance_matrix_1024 = create_distance_matrix(regional_nc_1024, 1024)
    artists_normalized,distance_matrix_normalized_256 = create_distance_matrix(normalized_regional_nc_256, 256)
    
    cumulative_mod =[]
    for lines in zip(distance_matrix_256,distance_matrix_normalized_256):
        for val in zip(lines[0],lines[1]):
            if val[0]!=0 and val[1]!=0:
                cumulative_mod.append(abs(val[0]-val[1]))
    
    # Compute average difference between painter's (normalized and non-normalized images)
    avg_64, std_64 = get_avg_std(distance_matrix_64, distance_matrix_256)
    avg_256, std_256 = get_avg_std(distance_matrix_256, distance_matrix_normalized_256)
    avg_1024, std_1024 = get_avg_std(distance_matrix_256, distance_matrix_1024)

    img_dm_64 = DM(distance_matrix_64)
    img_dm_256 = DM(distance_matrix_256)
    img_dm_1024 = DM(distance_matrix_1024)
    norm_img_dm_256 = DM(distance_matrix_normalized_256)

    coeff_256, p_value_256, n = mantel(img_dm_256, norm_img_dm_256)
    coeff_64, p_value_64, n = mantel(img_dm_256, img_dm_64)
    coeff_1024, p_value_1024, n = mantel(img_dm_256, img_dm_1024)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nnormalized images (256 blocks) vs 256 blocks\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Average variation = ", avg_256,"+/-", std_256)
    print("Mantel coeficient = ", coeff_256, ", p-value = ", p_value_256)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n64 blocks vs 256 blocks\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Average variation = ", avg_64,"+/-", std_64)
    print( "Mantel coeficient = ", coeff_64, ", p-value = ", p_value_64)
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n1024 blocks vs 256 blocks\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Average variation = ", avg_1024,"+/-", std_1024)
    print( "Mantel coeficient = ", coeff_1024, ",p-value = ", p_value_1024)