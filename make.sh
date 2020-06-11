#!/bin/bash
# 
chmod +x ./src/
cd hdc;
make clean all;
mv hdc ../bins;
mv div ../bins
cd ../bitbit/
cargo build --release
cp ./target/release/bitbit ../bins/
cd ../
bash ./src/Install_programs.sh
