#include <iostream> // cout, cerr
#include <chrono>
#include "PGMRead.h"
#include "hdc.h"
#include "alpha.h"

int main(int argc, char *argv[]) {

    if (argc >3 || argc <2){
        exit(44);
    }
    else if(argc ==2){
        std::string imagePath(argv[1]);        
        PGMRead img(imagePath);
        HDC hdc(img,10, .3);
        Alpha alpha(hdc.get_hdc());
        alpha.printAlpha();
    }
    else if(argc ==3 && std::string(argv[2]) == "p"){
        std::string imagePath(argv[1]);        
        PGMRead img(imagePath);
        HDC hdc(img,1, .3);
        hdc.print_hdc();
    }
}
