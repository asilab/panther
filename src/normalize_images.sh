#!/bin/bash
# 
# ===============================================================================================
# Normalize 8bit Images ===============================================================================
# ===============================================================================================

function NORM(){
  # rm -f ../reports/REPORT_REGIONAL_COMPLEXITY_$1;

  cd $1
  for x in *.jpg.pgm;
      do
        pgmnorm $x > ../normalize_Quantizing8/$x
    done
  cd ../
}

shopt -s globstar
cd ../Paintings91/
rm normalize_Quantizing8
mkdir normalize_Quantizing8

NORM "Quantizing8" &
P=$!
wait $P
cd ../
#
