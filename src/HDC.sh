#!/bin/bash
# 
# ===============================================================================================
# RUN HDC ===============================================================================
# ===============================================================================================

function HDC(){
  rm -f ../reports/REPORT_COMPLEXITY_HDC_$1;

  cd $1
  for x in *.jpg.pgm;
      do
        echo "Running $x ... in $1...";
        HDC=$(../../bins/hdc $x | awk '{printf "%f", $0}');
        echo "$x : $HDC" >> ../../reports/REPORT_HDC_$1;
    done
  cd ../
}

shopt -s globstar
cd ../Paintings91/
HDC "Quantizing2" &
HDC "Quantizing4" &
HDC "Quantizing6" &
HDC "Quantizing8" &
P=$!
wait $P
cd ../
#