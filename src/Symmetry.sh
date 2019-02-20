#!/bin/bash
# 
# RUN SYMMETRY ==================================================================================
#
shopt -s globstar
rm -f REPORT_SYMMETRY;
cd Paintings91/Images/
cp ../../paq8kx_v7.exe .
#
# ===============================================================================================
RANDOM=0;
SUBSAMPLE=100;
declare -a PAINTINGS;
readarray PAINTINGS < <(ls -d *.jpg | shuf -n $SUBSAMPLE)
#
for j in "${PAINTINGS[@]}"
  do
  echo "Compressing $j ...";
  rm -fr archive_xy.paq8kx archive_yx.paq8kx
  i=${PAINTINGS[$RANDOM % ${#PAINTINGS[@]}]};
  ./paq8kx_v7.exe -8 archive_xy $j $i;
  ./paq8kx_v7.exe -8 archive_yx $i $j;
  COMPRESSED_SIZExy=`ls -la archive_xy.paq8kx | awk '{ print $5;}'`; 
  COMPRESSED_SIZEyx=`ls -la archive_yx.paq8kx | awk '{ print $5;}'`; 
  if (( $COMPRESSED_SIZExy < $COMPRESSED_SIZEyx ));
    then
    echo "scale=12; ($COMPRESSED_SIZExy/$COMPRESSED_SIZEyx)*100.0" | 
    bc -l | awk '{printf "%f\n", $0}'  >> ../../REPORT_SYMMETRY;
    else
    echo "scale=12; ($COMPRESSED_SIZEyx/$COMPRESSED_SIZExy)*100.0" | 
    bc -l | awk '{printf "%f\n", $0}'  >> ../../REPORT_SYMMETRY;
  fi
  done; 
cd ../../
cat REPORT_SYMMETRY | awk '{for(i=1;i<=NF;i++) {sum[i] += $i; sumsq[i] += ($i)^2}} 
  END {for (i=1;i<=NF;i++) {
  printf "Average: %f ; Standard deviation: %f ;\n", sum[i]/NR, sqrt((sumsq[i]-sum[i]^2/NR)/NR)}
  }'
#
