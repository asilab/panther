#include <iostream> // cout, cerr
#include "PGMRead.h"

int main(int argc, char *argv[]) {

    if (argc !=2){
        exit(44);
    }
    std::string imagePath(argv[argc - 1]);        
    PGMRead img(imagePath);
    auto max_min = img.get_min_max();
    std::cout << max_min.first << "\t" << max_min.second << "\t" << max_min.second-max_min.first <<"\n";
}