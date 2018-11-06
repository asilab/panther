#!/bin/bash
# 
# RUN TRIANGULAR ================================================================================
#
shopt -s globstar
rm -f REPORT_TRIANGULAR;
cd Paintings91/Images/
cp ../../paq8kx_v7.exe .
#
# ===============================================================================================
RANDOM=0;
SUBSAMPLE=100;
declare -a PAINTINGS;
readarray PAINTINGS < <(ls -d *.jpg.pgm)
for((i = 0 ; i < SUBSAMPLE ; ++i));
  do
  x=${PAINTINGS[$RANDOM % ${#PAINTINGS[@]}]};
  y=${PAINTINGS[$RANDOM % ${#PAINTINGS[@]}]};
  z=${PAINTINGS[$RANDOM % ${#PAINTINGS[@]}]};
  #
  rm -fr archive_c_xy.paq8kx archive_c_yz.paq8kx archive_c_xz.paq8kx archive_c_z.paq8kx
  #
  ./paq8kx_v7.exe -8 archive_c_xy $x $y;
  ./paq8kx_v7.exe -8 archive_c_yz $y $z;
  ./paq8kx_v7.exe -8 archive_c_xz $x $z;
  ./paq8kx_v7.exe -8 archive_c_z  $z;
  #
  Cxy=`ls -la archive_c_xy.paq8kx | awk '{ print $5;}'`;
  Cyz=`ls -la archive_c_yz.paq8kx | awk '{ print $5;}'`;
  Cxz=`ls -la archive_c_xz.paq8kx | awk '{ print $5;}'`;
  Cz=`ls -la archive_c_z.paq8kx | awk '{ print $5;}'`;
  #
  if [[ "$(($Cxz+$Cyz))" -lt "$(($Cxy+$Cz))"  ]]; then
    echo "INVALID: it does not respect the distributivity property!" >> ../../REPORT_TRIANGULAR;
    exit;
  else
    echo "VALID TRAINGULAR INNEQUALITY!" >> ../../REPORT_TRIANGULAR;
  fi
  done
cd ../../
#
