 for y in *.pdf
    do
    
    x=${y%.pdf}
    convert $y -verbose -density 1000 /home/mikejpeg/Documents/PhD/jorgemfs.github.io/assets/img/fingerprint/1024/$x.png
    done
