#!/bin/bash
# 
# ===============================================================================================
# RUN NBDM ===============================================================================
# ===============================================================================================

function NBDM(){
  rm -f ../REPORT_COMPLEXITY_NBDM1_$1;
  rm -f ../reports/REPORT_COMPLEXITY_NBDM2_$1;

  cd $1
  for x in *.jpg.pgm.PROCESSED.bin;
      do
        echo "Running $x ... in $1...";
        NBDM1=$(python3 ../../python/nbdm2d1.py $x | awk '{printf "%f", $0}');
        echo "$x : $NBDM1" >> ../../reports/REPORT_COMPLEXITY_NBDM1_$1;
        NBDM2=$(python3 ../../python/nbdm2d2.py $x | awk '{printf "%f", $0}');
        echo "$x : $NBDM2" >> ../../reports/REPORT_COMPLEXITY_NBDM2_$1;

    done
  cd ../
}

shopt -s globstar
cd ../Paintings91/
NBDM "Quantizing2" &
NBDM "Quantizing4" &
NBDM "Quantizing6" &
NBDM "Quantizing8" &
P=$!
wait $P
cd ../
#