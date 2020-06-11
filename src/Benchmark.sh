#!/bin/bash
#
GET_AC=1;
RUN_RM=1;
RUN_COMPRESS=1;
RUN_JOIN=1;
RUN_PLOT=1;
#
# ==============================================================================
# 
shopt -s globstar
#
# ==============================================================================
#
if [[ "$GET_AC" -eq "1" ]]; then
  git clone https://github.com/pratas/ac.git
  cd ac/src/
  cmake .
  make
  cp AC ../../
  cd ../../
fi
#
# ==============================================================================
#
if [[ "$RUN_RM" -eq "1" ]]; then
  rm -f REPORT_COMPRESSION_PAQ;
  rm -f REPORT_COMPRESSION_LZMA;
  rm -f REPORT_COMPRESSION_GZIP;
  rm -f REPORT_COMPRESSION_BZIP2;
  rm -f REPORT_COMPRESSION_PPMD;
  rm -f REPORT_COMPRESSION_XZ;
  rm -f REPORT_COMPRESSION_AC;
fi
#
# ==============================================================================
#
if [[ "$RUN_COMPRESS" -eq "1" ]]; then
  cd Paintings91/Images/
  cp ../../paq8kx_v7.exe .
  cp ../../AC .
  for x in *.jpg;
    do
    echo "Running $x ...";
    ./paq8kx_v7.exe -8 $x
    compressed=`ls -la $x.paq8kx | awk '{ print $5;}'`;
    echo "$x : $compressed" >> ../../REPORT_COMPRESSION_PAQ;
    #
    lzma -9 $x
    compressed=`ls -la $x.lzma | awk '{ print $5;}'`;
    echo "$x : $compressed" >> ../../REPORT_COMPRESSION_LZMA;
    lzma -d $x.lzma
    #
    gzip -9 $x
    compressed=`ls -la $x.gz | awk '{ print $5;}'`;
    echo "$x : $compressed" >> ../../REPORT_COMPRESSION_GZIP;
    gunzip $x.gz
    #
    bzip2 -9 $x
    compressed=`ls -la $x.bz2 | awk '{ print $5;}'`;
    echo "$x : $compressed" >> ../../REPORT_COMPRESSION_BZIP2;
    bunzip2 $x.bz2
    #
    rm -f tmpX;
    ppmd e -ftmpX  -m256 $x
    compressed=`ls -la tmpX | awk '{ print $5;}'`;
    echo "$x : $compressed" >> ../../REPORT_COMPRESSION_PPMD;
    #
    xz -z -9 -e $x 
    compressed=`ls -la $x.xz | awk '{ print $5;}'`;
    echo "$x : $compressed" >> ../../REPORT_COMPRESSION_XZ;
    xz -d $x.xz
    #
    rm -f $x.co;
    ./AC -t 1 -l 3 $x
    compressed=`ls -la $x.co | awk '{ print $5;}'`;
    echo "$x : $compressed" >> ../../REPORT_COMPRESSION_AC;
    #
  done
  cd ../../
fi
#
# ==============================================================================
#
if [[ "$RUN_JOIN" -eq "1" ]]; then
  cat REPORT_COMPRESSION_GZIP  | awk 'BEGIN {t=0}; {t+=$3} END {print "GZIP\t"t}'  >  DATA ; 
  cat REPORT_COMPRESSION_BZIP2 | awk 'BEGIN {t=0}; {t+=$3} END {print "BZIP2\t"t}' >> DATA ;
  cat REPORT_COMPRESSION_XZ    | awk 'BEGIN {t=0}; {t+=$3} END {print "XZ\t"t}'    >> DATA ;
  cat REPORT_COMPRESSION_LZMA  | awk 'BEGIN {t=0}; {t+=$3} END {print "LZMA\t"t}'  >> DATA ;
  cat REPORT_COMPRESSION_AC    | awk 'BEGIN {t=0}; {t+=$3} END {print "AC\t"t}'    >> DATA ;
  cat REPORT_COMPRESSION_PPMD  | awk 'BEGIN {t=0}; {t+=$3} END {print "PPMD\t"t}'  >> DATA ;
  cat REPORT_COMPRESSION_PAQ   | awk 'BEGIN {t=0}; {t+=$3} END {print "PAQ8\t"t}'  >> DATA ;
fi
#
# ==============================================================================
#
if [[ "$RUN_PLOT" -eq "1" ]]; then
  echo "set terminal pdfcairo enhanced color
  set output 'bench.pdf'
  set auto
  set boxwidth 0.4
  set xtics nomirror
  set style fill solid 1.00
  set ylabel 'Bytes'
  set xlabel 'Methods'
  set grid ytics lc rgb '#C0C0C0'
  unset key
  set yrange[0:150000000]
  set grid
  set format y '%.0s %c'
  set style line 2 lc rgb '#406090'
  plot 'DATA' using 2:xtic(1) with boxes ls 2" | gnuplot -p
fi
#
# ==============================================================================