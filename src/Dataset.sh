#!/bin/bash
cd ..
rm -f Paintings91.zip
wget http://cat.cvc.uab.es/~joost/data/Paintings91.zip
unzip Paintings91.zip
cd Paintings91/Images/
mv LUCIO_FONTANA_36.JPG LUCIO_FONTANA_36.jpg
mv LUCIO_FONTANA_37.JPG LUCIO_FONTANA_37.jpg
cd ../../
cd src