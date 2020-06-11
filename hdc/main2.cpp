#include <iostream> // cout, cerr
#include <chrono>
#include "PGMRead.h"
#include "hdc.h"
#include "alpha.h"

int main(int argc, char *argv[]) {

    if (argc !=2){
        exit(44);
    }
    std::string imagePath(argv[1]);        
    PGMRead img(imagePath);
    HDC hdc(img,10, .3);
    Alpha alpha(hdc.getData());
    alpha.printAlpha();
}
