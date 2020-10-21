    #!/bin/bash
# 
# ===============================================================================================
# GET MIN AND MAX PIXEL VALUES ===============================================================================
# ===============================================================================================
function MINMAX(){
  rm -f ../reports/MIN_MAX;

  cd $1
  for x in *.jpg.pgm;
      do
        echo "Running $x ... in $1...";
        MinMax=$(../../bins/maxmin $x);
        echo "$x : $MinMax" >> ../../reports/MIN_MAX;
    done
  cd ../
}

shopt -s globstar
cd ../Paintings91/
MINMAX "Quantizing8" &
P=$!
wait $P
cd ../
#