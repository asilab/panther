#!/bin/bash
# 
# RUN EDITIONS ==================================================================================
#
shopt -s globstar
rm -f REPORT_NOISE_NC;
rm -f REPORT_NOISE_NCD;
cd Paintings91/Images/
cp ../../paq8kx_v7.exe .
cp ../../../bin/AddUniformNoise2Img2 .
chmod +x AddUniformNoise2Img2
#
# ===============================================================================================
PNAME1="THEODORE_GERICAULT_40";
PNAME2="MARC_CHAGALL_23";
PNAME3="RENE_MAGRITTE_30";
#
function NCD(){
  nxvalue="1";
  #
  (./paq8kx_v7.exe -8 N_NCD-X $1 ) &> TMP-NREP-PAQ;
  (./paq8kx_v7.exe -8 N_NCD-Y $2 ) &> TMP-NREP-PAQ;
  (./paq8kx_v7.exe -8 N_NCD-XY $1 $2 ) &> TMP-NREP-PAQ;
  #
  NCX=`ls -la N_NCD-X.paq8kx | awk '{ print $5;}'`;
  NCY=`ls -la N_NCD-Y.paq8kx | awk '{ print $5;}'`;
  NCXY=`ls -la N_NCD-XY.paq8kx | awk '{ print $5;}'`;
  #
  if(( $NCX < $NCY ));
    then
    nxvalue=`echo "scale=8; (((8.0*$NCXY)-(8.0*$NCX))/(8*$NCY))" | bc -l | awk '{printf "%f", $0}'`;
    else
    nxvalue=`echo "scale=8; (((8.0*$NCXY)-(8.0*$NCY))/(8*$NCX))" | bc -l | awk '{printf "%f", $0}'`;
  fi
  #
  rm -f N_NCD-X.paq8kx N_NCD-Y.paq8kx N_NCD-XY.paq8kx TMP-NREP-PAQ;
  #
  printf "$nxvalue\n" > N_NCD_MATRIX_TMP;
  }
#
echo "Running ...";
for((x=0 ; x<=50 ; ++x));
  do
  if(( $x == 0 ));
    then
    cp $PNAME1.jpg.pgm $PNAME1.noise$x.jpg.pgm
    cp $PNAME2.jpg.pgm $PNAME2.noise$x.jpg.pgm
    cp $PNAME3.jpg.pgm $PNAME3.noise$x.jpg.pgm
    else
    #
    #convert $PNAME1.jpg.pgm -seed 1000 -attenuate $x.00 +noise Uniform $PNAME1.noise$x.jpg.pgm;
    #convert $PNAME2.jpg.pgm -seed 1000 -attenuate $x.00 +noise Uniform $PNAME2.noise$x.jpg.pgm;
    #convert $PNAME3.jpg.pgm -seed 1000 -attenuate $x.00 +noise Uniform $PNAME3.noise$x.jpg.pgm;
    #
    RATE=`echo "scale=12; ($x/100.0)" | bc -l | awk '{printf "%f\n", $0}'`;
    #
    ./AddUniformNoise2Img2 -m -p $RATE $PNAME1.jpg.pgm
    gunzip img+noise.pgm.gz
    mv img+noise.pgm $PNAME1.noise$x.jpg.pgm
    #
    ./AddUniformNoise2Img2 -m -p $RATE $PNAME2.jpg.pgm
    gunzip img+noise.pgm.gz
    mv img+noise.pgm $PNAME2.noise$x.jpg.pgm
    #
    ./AddUniformNoise2Img2 -m -p $RATE $PNAME3.jpg.pgm
    gunzip img+noise.pgm.gz
    mv img+noise.pgm $PNAME3.noise$x.jpg.pgm
    fi
  #
  ./paq8kx_v7.exe -8 archive_1_NC_$x $PNAME1.noise$x.jpg.pgm;
  ./paq8kx_v7.exe -8 archive_2_NC_$x $PNAME2.noise$x.jpg.pgm;
  ./paq8kx_v7.exe -8 archive_3_NC_$x $PNAME3.noise$x.jpg.pgm;
  #
  # FALTA DIVIDIR PELO TAMANHO...
  NC1=`ls -la archive_1_NC_$x.paq8kx | awk '{ print $5;}'`;
  NC2=`ls -la archive_2_NC_$x.paq8kx | awk '{ print $5;}'`;
  NC3=`ls -la archive_3_NC_$x.paq8kx | awk '{ print $5;}'`;
  #
  NSIZE1=`ls -la $PNAME1.noise$x.jpg.pgm | awk '{ print $5;}'`;
  NSIZE2=`ls -la $PNAME2.noise$x.jpg.pgm | awk '{ print $5;}'`;
  NSIZE3=`ls -la $PNAME3.noise$x.jpg.pgm | awk '{ print $5;}'`;
  #
  F_NC1=`echo "scale=12; (($NC1*8)/(6.0*($NSIZE1*8)))" | bc -l | awk '{printf "%f\n", $0}'`;
  F_NC2=`echo "scale=12; (($NC2*8)/(6.0*($NSIZE2*8)))" | bc -l | awk '{printf "%f\n", $0}'`;
  F_NC3=`echo "scale=12; (($NC3*8)/(6.0*($NSIZE3*8)))" | bc -l | awk '{printf "%f\n", $0}'`;
  #
  NCD "$PNAME1.noise0.jpg.pgm" "$PNAME1.noise$x.jpg.pgm";
  NCD1=`cat N_NCD_MATRIX_TMP | awk '{print $1}'`;
  NCD "$PNAME2.noise0.jpg.pgm" "$PNAME2.noise$x.jpg.pgm";
  NCD2=`cat N_NCD_MATRIX_TMP | awk '{print $1}'`;
  NCD "$PNAME3.noise0.jpg.pgm" "$PNAME3.noise$x.jpg.pgm";
  NCD3=`cat N_NCD_MATRIX_TMP | awk '{print $1}'`;
  #
  printf "$x\t$NCD1\t$NCD2\t$NCD3\n" >> ../../REPORT_NOISE_NCD;
  printf "$x\t$F_NC1\t$F_NC2\t$F_NC3\n" >> ../../REPORT_NOISE_NC;
  #
  done
cd ../../
#
gnuplot << EOF
  reset
  set terminal pdfcairo enhanced color font 'Verdana,12'
  set output "Editions.pdf"
  set style line 101 lc rgb '#000000' lt 1 lw 4
  set border 3 front ls 101
  set tics nomirror out scale 0.75
  set format '%g'
  set size ratio 0.8
  set key outside horiz center top
  set xtics 5
  set yrange [0:1] 
  set xrange [0:50.5]
  set ytics 0.2
  set grid 
  set ylabel "NCD"
  set xlabel "Uniform pixel edition (%)"
  set border linewidth 1.5
  set style line 1 lc rgb '#0060ad' lt 1 lw 4 pt 5 ps 0.4 # --- blue
  set style line 2 lc rgb '#009900' lt 1 lw 4 pt 6 ps 0.4 # --- green
  set style line 3 lc rgb '#dd181f' lt 1 lw 4 pt 7 ps 0.5 # --- red
  plot "REPORT_NOISE_NCD" using 2 with linespoints ls 1 title "THEODORE GERICAULT 40", "REPORT_NOISE_NCD" using 3 with linespoints ls 2 title "MARC CHAGALL 23", "REPORT_NOISE_NCD" using 4 with linespoints ls 3 title "RENE MAGRITTE 30"
EOF

