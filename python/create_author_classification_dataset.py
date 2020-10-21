import scipy.io
import numpy as np
import shutil
import os

if __name__ == "__main__":
    data = scipy.io.loadmat('../Paintings91/Labels/labels.mat')
    labels_author = data['labels']    
   
    data = scipy.io.loadmat('../Paintings91/Labels/image_names.mat')
    image_names_authors=data['image_names']

    data =  scipy.io.loadmat('../Paintings91/Labels/trainset.mat')
    trainset = data['trainset']

    data =  scipy.io.loadmat('../Paintings91/Labels/testset.mat')
    testset = data['testset']

    labels_author_train = labels_author[np.where(trainset)[0],]
    labels_author_test = labels_author[np.where(testset)[0],]

    labels_authors_index = np.where(labels_author)[1]


# correct some problems with encodings!
for k in range(734, 779):
    image_names_authors[k][0][0] = image_names_authors[k][0][0].replace('Ã', 'É')


for k in range(len(labels_authors_index)):
    authors = labels_authors_index[k]
    try:
        os.mkdir('Labels_Author/Train/%s' %authors)
    except:
        pass
    try:
        os.mkdir('Labels_Author/Test/%s' %authors)
    except:
        pass
    if trainset[k]:
        try:
            _ = shutil.copy('Images/%s' %image_names_authors[k][0][0], '../Paintings91/Labels_Author/Train/%s' %authors)
        except:
            print(k, image_names_authors[k][0][0])
    else:
        try:
            _ = shutil.copy('Images/%s' %image_names_authors[k][0][0], '../Paintings91/Labels_Author/Test/%s' %authors)
        except:
            print(k, image_names_authors[k][0][0])
