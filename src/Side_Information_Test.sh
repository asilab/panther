python3 ../python/side_info_amplifier.py ../MiscellaneousDataset/NA_img/NA4.pgm_6bitQ.pgm.PROCESSED.bin > TMP
cat TMP;
P=$!
wait $P
original=`ls -la image.txt | awk '{ print $5;}'`;
../paq8kx_v7.exe -8 image.txt
compressed=`ls -la image.txt.paq8kx | awk '{ print $5;}'`;

original_amp=`ls -la amplified_image.txt | awk '{ print $5;}'`;
../paq8kx_v7.exe -8 amplified_image.txt
compressed_amp=`ls -la amplified_image.txt.paq8kx | awk '{ print $5;}'`;

echo "compressed :" $compressed;
echo "new compressed :" $compressed_amp;
rm image.txt amplified_image.txt TMP;

