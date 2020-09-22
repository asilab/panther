#!/bin/bash
# 
# ===============================================================================================
# RUN HDC ===============================================================================
# ===============================================================================================

function HDC(){
  rm -f ../reports/REPORT_COMPLEXITY_HDC_FEATURES_$1;

  cd $1
  for x in *.jpg.pgm;
      do
        echo "Running $x ... in $1...";
        HDC=$(../../bins/hdc $x p);
        echo "$x : $HDC" >> ../../reports/REPORT_COMPLEXITY_HDC_FEATURES_$1;
    done
  cd ../
}

shopt -s globstar
cd ../Paintings91/
HDC "Quantizing8" &
P=$!
wait $P
cd ../
#