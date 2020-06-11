#!/bin/bash
# 
# INSTALL PAQ BINARIES ==========================================================================
#
#sudo apt-get install g++-multilib
rm -fR paq;
git clone https://github.com/JohannesBuchner/paq.git
cd paq
make paq8kx_v7.exe
chmod +x *.exe
cp paq8kx_v7.exe ..
cd ..
#
# INSTALL BDM ===================================================================================
#
# rm -fr BDM_SRC;
# mkdir BDM_SRC/
# cd BDM_SRC/
# wget https://www.algorithmicdynamics.net/uploads/4/3/8/0/43802527/bdmcpp.zip
# unzip bdmcpp.zip
# cd bdmcpp
# g++ -o BDM.exe BDM.cpp -lgmp -lm
# mv BDM.exe ../..
# mv complexities.txt ../..
# cd ../../
# pwd
# ===============================================================================================
