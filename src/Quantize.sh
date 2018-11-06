#!/bin/bash
cp ../bins/LMQ LMQuant
shopt -s globstar
for x in Paintings91/Images/*.jpg;
  do
  echo "Converting and quantizing $x ...";
  convert $x $x.pgm
  ./LMQuant -n 64 $x.pgm
  gunzip lloydMaxQuantizedImg.pgm.gz
  mv lloydMaxQuantizedImg.pgm $x.pgm
done

