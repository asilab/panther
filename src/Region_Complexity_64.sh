#!/bin/bash
# 
# ===============================================================================================
# RUN Regional Complexity ===============================================================================
# ===============================================================================================

function BLOCK(){
  # rm -f ../reports/REPORT_REGIONAL_COMPLEXITY_$1;

  cd $1
  for x in *.jpg.pgm;
      do
        printf "$x: ">> ../../reports/REPORT_REGIONAL_COMPLEXITY_$2_$1; 
        echo "Running $x ... in $1...";
        ../../bins/div $2 $x;
        
        fname=$(basename $x)
        fbname=${fname%.*}
        fname=$(basename $fbname)
        fbname=${fname%.*}

        for y in ${fbname}_block_*.pgm;
          do            
            width=$(identify -format "%w" "$y")
            convert -compress none $y TEMP2IMG.PGM
            tail -n +4 TEMP2IMG.PGM | ../../bins/binarization $width > $y.PROCESSED.bin;
            original=`ls -la $y.PROCESSED.bin | awk '{ print $5;}'`;
            ../../paq8kx_v7.exe -8 $y.PROCESSED.bin
            compressed=`ls -la $y.PROCESSED.bin.paq8kx | awk '{ print $5;}'`;
            entropy=`echo "scale=10; ($compressed * 8.0) / $original" | bc -l | awk '{printf "%f", $0}'`;
            if [ -z "$entropy" ]
            then
                entropy=0.0;
            fi
            printf "$entropy \t" >> ../../reports/REPORT_REGIONAL_COMPLEXITY_$2_$1;
          rm $y*;
        done
        printf "\n" >> ../../reports/REPORT_REGIONAL_COMPLEXITY_$2_$1;
        rm Block_*.pgm;
    done
  cd ../
}

shopt -s globstar
cd ../Paintings91/
BLOCK "Quantizing8" 64 &
P=$!
wait $P
cd ../
#
