#!/bin/bash
# 
# RUN COMPRESSION ===============================================================================
#
shopt -s globstar
rm -f REPORT_COMPLEXITY;
cd Paintings91/Images/
cp ../../paq8kx_v7.exe .
for x in *.jpg.pgm;
  do
  echo "Running $x ...";
  original=`ls -la $x | awk '{ print $5;}'`;
  echo "a";
  ./paq8kx_v7.exe -8 $x
  echo "b";
  compressed=`ls -la $x.paq8kx | awk '{ print $5;}'`;
  echo "c";
  entropy=`echo "scale=8; ($compressed * 8.0) / ($original * 6.0)" | bc -l | awk '{printf "%f", $0}'`;
  echo "d";
  echo "$x : $entropy" >> ../../REPORT_COMPLEXITY;
  echo "f";
  done
cd ../../
#
# ===============================================================================================
