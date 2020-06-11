#!/bin/bash
RESIZE_AND_CONVERT=1;
PRE_PROCESSING=1;
if [[ "$PRE_PROCESSING" -eq "1" ]];
  then
  if [[ "$RESIZE_AND_CONVERT" -eq "1" ]];
    then
      #resize
      shopt -s globstar
      cd ../MiscellaneousDataset;
      declare -a FOLDER=("AP1_img" "AP2_img")
      for x in "${FOLDER[@]}" 
          do
          cd $x;
          pwd
          for y in *.jpg;
          do
              echo "Converting $y ...";
              convert $y $y.pgm;
          done
          cd ..
      done
      declare -a FOLDER=("AP1_img" "AP2_img" "CR_img" "DR_img" "NA_img")
      for x in "${FOLDER[@]}" 
          do
          cd $x;
          for y in *.pgm; do echo Converting $y...;  convert $y -resize 256 ${y}; done
          cd ..
      done
  fi 

  # Quantitizing
  cd ../MiscellaneousDataset;

  echo "Quantitizing to 6 bits..."
  QValue=6;
  Value=$(echo $((2 ** 6)));
  declare -a FOLDER=("AP1_img" "AP2_img" "CR_img" "DR_img" "NA_img")
  for x in "${FOLDER[@]}" 
      do
      cd $x;
      rm *_6bitQ.pgm
      for x in *.pgm;
          do 
          file=$(basename "${x}");
          ../../bins/LMQ -n $Value $x
          gunzip lloydMaxQuantizedImg.pgm.gz
          mv lloydMaxQuantizedImg.pgm ${file}"_6bitQ.pgm"
      done           
      cd ..
  done


  #./Trimm_and_Binarization.sh
  for y in "${FOLDER[@]}"
    do
    cd $y;
    for x in *_6bitQ.pgm;
      do
      echo "Running $x ...";
      file=$(basename "${x}");
      rm -f $x.PROCESSED.bin;
      convert -colorspace gray $x TEMP-IMG.PGM;
      width=$(identify -format "%w" "TEMP-IMG.PGM")> /dev/null;
      height=$(identify -format "%h" "TEMP-IMG.PGM")> /dev/null;
      convert -compress none TEMP-IMG.PGM TEMP2-IMG.PGM
      printf "geometry format (Width x Height): $width x $height\n";
      #
      printf "Binarizing image ...\n";
      tail -n +4 TEMP2-IMG.PGM | ../../bins/binarization $width > $file.PROCESSED.bin;
      rm -f TEMP-IMG.PGM TEMP2-IMG.PGM;
      printf "Done!\n";
    done
    cd ../;
  done
  cd ../src

  function COMPRESS_NC_NBDM(){
  rm -f ../reports/REPORT_DIVERSE_COMPLEXITY_$1;
  cd $1
  for x in *PROCESSED.bin;
      do
      echo "Running $x ... in $1...";
      original=`ls -la $x | awk '{ print $5;}'`;
      ../../paq8kx_v7.exe -8 $x
      compressed=`ls -la $x.paq8kx | awk '{ print $5;}'`;
      entropy=`echo "scale=10; ($compressed * 8.0) / $original" | bc -l | awk '{printf "%f", $0}'`;
      NBDM=$(python3 ../../python/nbdm2d1.py $x| awk '{printf "%f", $0}');   
      echo "$1 : $entropy" : $NBDM >> ../../reports/REPORT_DIVERSE_COMPLEXITY_$1;
    done
  cd ../
  }

  cd ../MiscellaneousDataset;

  COMPRESS_NC_NBDM "CA_img"
  COMPRESS_NC_NBDM "AP1_img" 
  COMPRESS_NC_NBDM "AP2_img" 
  COMPRESS_NC_NBDM "CR_img" 
  COMPRESS_NC_NBDM "DR_img"
  COMPRESS_NC_NBDM "NA_img"
fi


gnuplot << EOF
  reset
  set terminal pdfcairo enhance color
  set term pdfcairo font 'Tahoma,7'
  set key under nobox
  set style histogram clustered gap 1 title offset 1,0.25
  set style fill solid noborder
  unset xtics
  set output 'Diverse_Complexity.pdf'
  set auto
  set boxwidth 1
  set style fill solid 1.00
  set grid ytics lc rgb '#C0C0C0'
  set key ins horiz font 'Tahoma,8'
  set key center top
  set style fill solid 1.0 border 0.5
  set xtics rotate nomirror
  set tics textcolor rgb 'black'
  set yrange[0:1]
  set xrange[0:1]
  set size square
  set ylabel 'NBDM' font 'Tahoma,8'
  set xlabel 'NC' font 'Tahoma,8'
  set key outside
  set style line 1 lw 1.5 lc rgb '#B5651D' pt 5  pointsize 0.55
  set style line 2 lw 1.5 lc rgb '#34495e' pt 2   pointsize 0.6
  set style line 3 lw 1.5 lc rgb '#FFC300' pt 3   pointsize 0.6
  set style line 4 lw 1.5 lc rgb '#FF5733' pt 13   pointsize 0.6
  set style line 5 lw 1.5 lc rgb '#C70039' pt 9  pointsize 0.6
  set style line 6 lw 1.5 lc rgb '#2ecc71' pt 7   pointsize 0.6

  set datafile separator ":"
  plot '../reports/REPORT_DIVERSE_COMPLEXITY_CA_img' using 2:3 title 'Cellular Automata' with points ls 1 , \
  '../reports/REPORT_DIVERSE_COMPLEXITY_AP1_img' using 2:3 title 'Artistic Paintings Dataset I' with points ls 2, \
  '../reports/REPORT_DIVERSE_COMPLEXITY_AP2_img' using 2:3 title 'Artistic Paintings Dataset II' with points ls 3, \
  '../reports/REPORT_DIVERSE_COMPLEXITY_CR_img' using 2:3 title 'Computed Radiography' with points ls 4, \
  '../reports/REPORT_DIVERSE_COMPLEXITY_DR_img' using 2:3 title 'Diabetic Retinopathy' with points ls 5, \
  '../reports/REPORT_DIVERSE_COMPLEXITY_NA_img' using 2:3 title 'Natural Images' with points ls 6
EOF
mv Diverse_Complexity.pdf ../plots/;

