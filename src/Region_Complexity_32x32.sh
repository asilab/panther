    #!/bin/bash
# 
# ===============================================================================================
# RUN Regional Complexity ===============================================================================
# ===============================================================================================

function BLOCK(){
  cd $1
    while read x; do
    #   echo "Running $x ... in $1...";
        printf "$x: ">> ../../reports/$4;
        ../../bins/div $2 $x
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
            printf "$entropy \t" >> ../../reports/$4;
            rm $y*;
        done
        printf "\n" >> ../../reports/$4;
    done <../$3
  cd ../
}

shopt -s globstar

cd ../Paintings91/Quantizing8
# Work out lines per file.
N=10;
ls *.jpg.pgm>../FILES_TO_COMPRESS;
total_lines=$(cat ../FILES_TO_COMPRESS|wc -l)
((lines_per_file = (total_lines + N - 1) / N))
echo $lines_per_file
# Split the actual file, maintaining lines.
cd ..;
wc -l FILES_TO_COMPRESS
split --lines=${lines_per_file} FILES_TO_COMPRESS FL_CMP.
rm FILES_TO_COMPRESS
cnt=0;

for file_to_read in FL_CMP.*;
    do
    filename="Regional_complexity_part_"${cnt};
    BLOCK "Quantizing8" 1024 ${file_to_read} ${filename} &
    ((cnt = cnt + 1))
done
P=$!
wait $P
rm FL_CMP.*
for fl in ../reports/Regional_complexity_part_*
    cat ${fl} >> ../reports/REPORT_REGIONAL_COMPLEXITY_1024_Quantizing8

cd ../
#
