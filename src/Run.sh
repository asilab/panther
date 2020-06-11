#!/bin/bash
#
########################
chmod +x *.sh
########################
./Dataset.sh
./Quantize.sh 
./Trimm_and_Binarization.sh
./BDM.sh
./Compress.sh
./HDC.sh
./Average_Complexity.sh
./Region_Complexity.sh
########################