#!/bin/bash

shopt -s globstar

cd ../Paintings91/
for i in 2 4 6 8
do
  echo "Converting and Quantitizing to $i bits..."
  QValue=$i;
  Value=$(echo $((2 ** $QValue)));
  rm -rf Quantizing$QValue
  mkdir Quantizing$QValue;  
  for x in ./Images/*.jpg;
    do 
    file=$(basename "${x}");
    cp $x ./Quantizing$QValue/$(basename "${x}");
    echo "Converting and quantizing $Value ...";
    cd ./Quantizing$QValue/
    convert $file $file.pgm;
    ../../bins/LMQ -n $Value $file.pgm
    gunzip lloydMaxQuantizedImg.pgm.gz
    mv lloydMaxQuantizedImg.pgm $file.pgm
    rm $file
    cd ..;
  done
done
