#!/bin/bash
BUILD_BINARY = 0;

if [[ "$BUILD_BINARY" -eq "1" ]];
   then
    cd bitbit/
    cargo build --release
    cp ./target/release/bitbit ../bins/
    cd ../
fi

shopt -s globstar
cd ../Paintings91/
declare -a NAMES=("Quantizing2" "Quantizing4" "Quantizing6" "Quantizing8" "normalize_Quantizing8");

for y in "${NAMES[@]}"
  do
  cd $y;
  for x in *.jpg.pgm;
    do
    echo "Running $x ...";
    file=$(basename "${x}");

    rm -f $file.PROCESSED.bin;
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
