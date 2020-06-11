#!/bin/bash
# 
function COMPRESS(){

rm -f ../reports/REPORT_COMPLEXITY_NC_$1;
cd $1
for x in *.jpg.pgm.PROCESSED.bin;
    do
    echo "Running $x ... in $1...";
      original=`ls -la $x | awk '{ print $5;}'`;
      ../../paq8kx_v7.exe -8 $x
      compressed=`ls -la $x.paq8kx | awk '{ print $5;}'`;
      entropy=`echo "scale=10; ($compressed * 8.0) / $original" | bc -l | awk '{printf "%f", $0}'`;
      echo "$x : $entropy" >> ../../reports/REPORT_COMPLEXITY_NC_$1;
  done
cd ../
}


shopt -s globstar
cd ../Paintings91/
COMPRESS "Quantizing2" &
COMPRESS "Quantizing4" &
COMPRESS "Quantizing6" &
COMPRESS "Quantizing8" &
P=$!
wait $P
cd ../
#
