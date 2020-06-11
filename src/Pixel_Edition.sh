#!/bin/bash
# 
# RUN PIXEL EDITIONS ============================================================================
#
CREATE_NOISE_LIST=0;
cd ../Paintings91/;



chmod +x ../bins/AddUniformNoise2Img2 ;
#
# ===============================================================================================
PNAME1="THEODORE_GERICAULT_40";
PNAME2="MARC_CHAGALL_23";
PNAME3="RENE_MAGRITTE_30";
#
function BIN_IMG(){
    convert -colorspace gray $1 TEMPIMG.PGM;
    width=$(identify -format "%w" "TEMPIMG.PGM")> /dev/null;
    height=$(identify -format "%h" "TEMPIMG.PGM")> /dev/null;
    convert -compress none TEMPIMG.PGM TEMP2IMG.PGM
    printf "geometry format (Width x Height): $width x $height\n";
    #
    printf "Binarizing image ...\n";
    tail -n +4 TEMP2IMG.PGM | ../../bins/binarization $width > $1.PROCESSED.bin;
    rm -f TEMPIMG.PGM TEMP2IMG.PGM;
    printf "Done!\n";
  }

#
#
if [[ "$CREATE_NOISE_LIST" -eq "1" ]];
  then
    rm -f ../reports/REPORT_NOISE_NC;
    rm -f ../reports/REPORT_NOISE_PYNBDM;
    rm -r Noise
    mkdir Noise;
    cd Noise

    echo "Running ...";
    for((x=0 ; x<=50 ; ++x));
    do
    if (( $x == 0 ));
      then
      cp ../Images/$PNAME1.jpg $PNAME1.noise$x.jpg
      convert $PNAME1.noise$x.jpg $PNAME1.noise$x.jpg.pgm;

      cp ../Images/$PNAME2.jpg $PNAME2.noise$x.jpg
      convert $PNAME2.noise$x.jpg $PNAME2.noise$x.jpg.pgm;

      cp ../Images/$PNAME3.jpg $PNAME3.noise$x.jpg;
      convert $PNAME3.noise$x.jpg $PNAME3.noise$x.jpg.pgm;

      rm $PNAME1.noise$x.jpg  $PNAME2.noise$x.jpg $PNAME3.noise$x.jpg;

    else
      #
      RATE=`echo "scale=12; ($x/100.0)" | bc -l | awk '{printf "%f\n", $0}'`;
      #
      ../../bins/AddUniformNoise2Img2 -m -p $RATE $PNAME1.noise0.jpg.pgm
      gunzip img+noise.pgm.gz
      mv img+noise.pgm $PNAME1.noise$x.jpg.pgm
      #
      ../../bins/AddUniformNoise2Img2  -m -p $RATE $PNAME2.noise0.jpg.pgm
      gunzip img+noise.pgm.gz
      mv img+noise.pgm $PNAME2.noise$x.jpg.pgm
      #
      ../../bins/AddUniformNoise2Img2  -m -p $RATE $PNAME3.noise0.jpg.pgm
      gunzip img+noise.pgm.gz
      mv img+noise.pgm $PNAME3.noise$x.jpg.pgm;
      fi

    BIN_IMG "$PNAME1.noise$x.jpg.pgm";    
    BIN_IMG "$PNAME2.noise$x.jpg.pgm";
    BIN_IMG "$PNAME3.noise$x.jpg.pgm";
   
   # NC
    ../../paq8kx_v7.exe -8 archive_1_NC_$x $PNAME1.noise$x.jpg.pgm.PROCESSED.bin;
    ../../paq8kx_v7.exe -8 archive_2_NC_$x $PNAME2.noise$x.jpg.pgm.PROCESSED.bin;
     ../../paq8kx_v7.exe -8 archive_3_NC_$x $PNAME3.noise$x.jpg.pgm.PROCESSED.bin;
    
    NC1=`ls -la archive_1_NC_$x.paq8kx | awk '{ print $5;}'`;
    NC2=`ls -la archive_2_NC_$x.paq8kx | awk '{ print $5;}'`;
    NC3=`ls -la archive_3_NC_$x.paq8kx | awk '{ print $5;}'`;
    
    NSIZE1=`ls -la $PNAME1.noise$x.jpg.pgm.PROCESSED.bin | awk '{ print $5;}'`;
    NSIZE2=`ls -la $PNAME2.noise$x.jpg.pgm.PROCESSED.bin | awk '{ print $5;}'`;
    NSIZE3=`ls -la $PNAME3.noise$x.jpg.pgm.PROCESSED.bin | awk '{ print $5;}'`;
    
    F_NC1=`echo "scale=12; (($NC1*8)/($NSIZE1))" | bc -l | awk '{printf "%f\n", $0}'`;
    F_NC2=`echo "scale=12; (($NC2*8)/($NSIZE2))" | bc -l | awk '{printf "%f\n", $0}'`;
    F_NC3=`echo "scale=12; (($NC3*8)/($NSIZE3))" | bc -l | awk '{printf "%f\n", $0}'`;
    
    # BDM
    NBDM1_1=$(python3 ../../python/nbdm2d1.py $PNAME1.noise$x.jpg.pgm.PROCESSED.bin| awk '{printf "%f", $0}');
    NBDM2_1=$(python3 ../../python/nbdm2d1.py $PNAME2.noise$x.jpg.pgm.PROCESSED.bin| awk '{printf "%f", $0}');
    NBDM3_1=$(python3 ../../python/nbdm2d1.py $PNAME3.noise$x.jpg.pgm.PROCESSED.bin| awk '{printf "%f", $0}');
    
    NBDM1_2=$(python3 ../../python/nbdm2d2.py $PNAME1.noise$x.jpg.pgm.PROCESSED.bin| awk '{printf "%f", $0}');
    NBDM2_2=$(python3 ../../python/nbdm2d2.py $PNAME2.noise$x.jpg.pgm.PROCESSED.bin| awk '{printf "%f", $0}');
    NBDM3_2=$(python3 ../../python/nbdm2d2.py $PNAME3.noise$x.jpg.pgm.PROCESSED.bin| awk '{printf "%f", $0}');

    printf "$x\t$F_NC1\t$F_NC2\t$F_NC3\n" >> ../../reports/REPORT_NOISE_NC;
    printf "$x\t$NBDM1_1\t$NBDM2_1\t$NBDM3_1\n" >> ../../reports/REPORT_NOISE_NBDM_1;
    printf "$x\t$NBDM1_2\t$NBDM2_2\t$NBDM3_2\n" >> ../../reports/REPORT_NOISE_NBDM_2;

    done
cd ../
fi
cd ../
#
gnuplot << EOF
  reset
  set terminal pdfcairo enhanced color font 'Verdana,12'
  set output "NBDM1_NC_NOISE.pdf"
  set style line 101 lc rgb '#000000' lt 1 lw 4
  set border 3 front ls 101
  set tics nomirror out scale 0.75
  set format '%g'
  set size ratio 0.8
  set key outside horiz center top
  set xtics 5
  set yrange [0:1.4] 
  set xrange [0:50.5]
  set ytics 0.2
  set grid 
  set ylabel "NC - NBDM1"
  set xlabel "Uniform noise (%)"
  set border linewidth 1.5
  set style line 1 lc rgb '#0060ad' lt 1 lw 4 pt 0 ps 0.4 # --- blue
  set style line 2 lc rgb '#dd181f' lt 1 lw 4 pt 0 ps 0.4 # --- purple
  set style line 3 lc rgb '#009900' lt 1 lw 4 pt 0 ps 0.4 # --- green
  set for [i=1:5] linetype i dt i
  set style line 4 lc rgb '#808000' linetype 10 lw 4 pt 0 ps 1 # --- olive
  set style line 5 lc rgb '#6a0dad' linetype 10 lw 4 pt 0 ps 1 # --- red
  set style line 6 lc rgb "#FFA500" linetype 10 lw 4 pt 0 ps 1 # --- orange
  plot "./reports/REPORT_NOISE_NC" using 1:2 with linespoints ls 1 title "NC-THEODORE\_GERICAULT_40" noenhanced, \
   "./reports/REPORT_NOISE_NBDM_1" using 1:2 with linespoints ls 5 title "NBDM1-THEODORE\_GERICAULT_40" noenhanced, \
   "./reports/REPORT_NOISE_NC" using 1:3 with linespoints ls 3 title "NC-MARC\_CHAGALL_23" noenhanced, \
   "./reports/REPORT_NOISE_NBDM_1" using 1:3 with linespoints ls 4 title "NBDM1-MARC_CHAGALL_23" noenhanced, \
   "./reports/REPORT_NOISE_NC" using 1:4 with linespoints ls 2 title "NC-RENE\_MAGRITTE_30" noenhanced, \
   "./reports/REPORT_NOISE_NBDM_1" using 1:4 with linespoints ls 6 title "NBDM1-RENE\_MAGRITTE_30" noenhanced
EOF

gnuplot << EOF
  reset
  set terminal pdfcairo enhanced color font 'Verdana,12'
  set output "NBDM2_NC_NOISE.pdf"
  set style line 101 lc rgb '#000000' lt 1 lw 4
  set border 3 front ls 101
  set tics nomirror out scale 0.75
  set format '%g'
  set size ratio 0.8
  set key outside horiz center top
  set xtics 5
  set yrange [0:1.4] 
  set xrange [0:50.5]
  set ytics 0.2
  set grid 
  set ylabel "NC - NBDM2"
  set xlabel "Uniform noise (%)"
  set border linewidth 1.5
  set style line 1 lc rgb '#0060ad' lt 1 lw 4 pt 0 ps 0.4 # --- blue
  set style line 2 lc rgb '#dd181f' lt 1 lw 4 pt 0 ps 0.4 # --- purple
  set style line 3 lc rgb '#009900' lt 1 lw 4 pt 0 ps 0.4 # --- green
  set for [i=1:5] linetype i dt i
  set style line 4 lc rgb '#808000' linetype 10 lw 4 pt 0 ps 1 # --- olive
  set style line 5 lc rgb '#6a0dad' linetype 10 lw 4 pt 0 ps 1 # --- red
  set style line 6 lc rgb "#FFA500" linetype 10 lw 4 pt 0 ps 1 # --- orange
  plot "./reports/REPORT_NOISE_NC" using 1:2 with linespoints ls 1 title "NC-THEODORE\_GERICAULT_40" noenhanced, \
   "./reports/REPORT_NOISE_NBDM_2" using 1:2 with linespoints ls 5 title "NBDM2-THEODORE\_GERICAULT_40" noenhanced, \
   "./reports/REPORT_NOISE_NC" using 1:3 with linespoints ls 3 title "NC-MARC\_CHAGALL_23" noenhanced, \
   "./reports/REPORT_NOISE_NBDM_2" using 1:3 with linespoints ls 4 title "NBDM2-MARC_CHAGALL_23" noenhanced, \
   "./reports/REPORT_NOISE_NC" using 1:4 with linespoints ls 2 title "NC-RENE\_MAGRITTE_30" noenhanced, \
   "./reports/REPORT_NOISE_NBDM_2" using 1:4 with linespoints ls 6 title "NBDM2-RENE\_MAGRITTE_30" noenhanced
EOF

gnuplot << EOF
  reset
  set terminal pdfcairo enhanced color font 'Verdana,12'
  set output "NBDM1_NBDM2_NOISE.pdf"
  set style line 101 lc rgb '#000000' lt 1 lw 4
  set border 3 front ls 101
  set tics nomirror out scale 0.75
  set format '%g'
  set size ratio 0.8
  set key outside horiz center top
  set xtics 5
  set yrange [0:1.4] 
  set xrange [0:50.5]
  set ytics 0.2
  set grid 
  set ylabel "NBDM1 - NBDM2"
  set xlabel "Uniform noise (%)"
  set border linewidth 1.5
  set style line 1 lc rgb '#808000' lt 1 lw 4 pt 0 ps 0.4 # --- blue
  set style line 2 lc rgb '#6a0dad' lt 1 lw 4 pt 0 ps 0.4 # --- purple
  set style line 3 lc rgb '#FFA500' lt 1 lw 4 pt 0 ps 0.4 # --- green
  set for [i=1:5] linetype i dt i
  set style line 4 lc rgb '#808000' linetype 10 lw 4 pt 0 ps 1 # --- olive
  set style line 5 lc rgb '#6a0dad' linetype 10 lw 4 pt 0 ps 1 # --- red
  set style line 6 lc rgb "#FFA500" linetype 10 lw 4 pt 0 ps 1 # --- orange
  plot "./reports/REPORT_NOISE_NBDM_1" using 1:2 with linespoints ls 5 title "NBDM1-THEODORE\_GERICAULT_40" noenhanced, \
       "./reports/REPORT_NOISE_NBDM_2" using 1:2 with linespoints ls 2 title "NBDM2-THEODORE\_GERICAULT_40" noenhanced, \
       "./reports/REPORT_NOISE_NBDM_1" using 1:3 with linespoints ls 4 title "NBDM1-MARC\_CHAGALL_23" noenhanced, \
       "./reports/REPORT_NOISE_NBDM_2" using 1:3 with linespoints ls 1 title "NBDM2-MARC_CHAGALL_23" noenhanced, \
       "./reports/REPORT_NOISE_NBDM_1" using 1:4 with linespoints ls 6 title "NBDM1-RENE\_MAGRITTE_30" noenhanced, \
       "./reports/REPORT_NOISE_NBDM_2" using 1:4 with linespoints ls 3 title "NBDM2-RENE\_MAGRITTE_30" noenhanced
EOF

mv NBDM1_NC_NOISE.pdf plots/
mv NBDM2_NC_NOISE.pdf plots/
mv NBDM1_NBDM2_NOISE.pdf plots/