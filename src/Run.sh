#!/bin/bash
#
########################
chmod +x *.sh
########################
./Dataset.sh                        # Downloads and unzips dataset
./Quantize.sh                       # Quantizes images of the dataset to 8, 6, 4 and 2 bits.
./normalize_images.sh               # Normalizes 0 to 256 the 8 bit images.
./Trimm_and_Binarization.sh         # Trims and Binarizes images of the dataset.
./BDM.sh                            # Computes NBDM (1 and 2) for all quantized images of the dataset.
./Compress.sh                       # Computes NC for all quantized images of the dataset.
./HDC.sh                            # Computes HDC alpha for 8 bit quantized images of the dataset.
./Average_Complexity.sh             # Computes average information based measures for each author
./Region_Complexity.sh              # Computes regional NC for 8 bit quantized images of the dataset.
./Average_Regional_Complexity.sh    # Computes fingerprint of each author
########################