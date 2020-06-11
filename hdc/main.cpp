#include <iostream> // cout, cerr
#include <chrono>
#include "PGMRead.h"
#include "divide.h"
#include "PGMWrite.h"
int main(int argc, char *argv[]) {

    if (argc !=3){
        exit(44);
    }
    std::string imagePath(argv[argc - 1]);        
    PGMRead img(imagePath);
    DivideImage div(img.getData(),atoi(argv[argc - 2]));
    auto Test = div.get_data();
    unsigned int counter = 0;
    std::string main_sv = "Block_";
    std::string ext = ".pgm";
    std::string sv_str;
    for (auto block:Test){
        sv_str = main_sv + std::to_string(counter) + ext;
        PGMWrite wrt(block,sv_str);
        ++counter;
    }
}
