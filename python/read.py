from string import digits
def process_nc_1024_features(file1):
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
            if (len(unordered_image) != 1024):
                print(author, len(unordered_image))
            else:
                ordered_image = unordered_image
                #ordered_image = reorder(unordered_image) 
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

if __name__ == "__main__":
    file_1 = open("../reports/R_R_C_1024", 'r', encoding='iso-8859-1')
    process_nc_1024_features(file_1)
