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
# INSTALL pgmnorm ===================================================================================
##Ubunto distro:

#sudo apt-get update -y
#sudo apt-get install -y netpbm
cd ../tools
tar zxvf backups.tgz
cd netpbm-10.73.33/
## Other distros
#For most typical platforms, you can just do
./configure
#followed by
make
#To build all the programs.  Then
make package
#To gather all the installable parts into a specified directory, and finally
./installnetpbm

cd ../../src/
