#include <fstream>
#include <algorithm>
#include "PGMWrite.h"

PGMWrite::PGMWrite(std::vector<std::vector<int> > pixel_data, std::string pathToImage, std::pair<int,int> min_max){
    this->pixel_data = pixel_data;
    this->maxValue=min_max.second;
    this->numcols = get_cols();
    this->numrows = get_rows();
    write(pathToImage);

}  

int PGMWrite::determine_max_value(){
    int max_value = 0;
    for (auto line:this->pixel_data){
        for (auto pixel: line){
            if (pixel > max_value){
                max_value = pixel;
            }
        }
    }
    return max_value;
}

unsigned int  PGMWrite::get_rows(){
    return this->pixel_data.size();
}

unsigned int  PGMWrite::get_cols(){
    return this->pixel_data[0].size();
}

void PGMWrite::write(std::string pathToImage){
     std::ofstream f(pathToImage,std::ios_base::out
                              |std::ios_base::binary
                              |std::ios_base::trunc
                   );
    f << "P5\n" << this->numcols << " " << this->numrows << "\n" << this->maxValue << "\n";
    for(auto line:this->pixel_data){
        for (auto pixel: line){
            unsigned char l = static_cast<unsigned char>(pixel);
            f<<l;
        }
    }
        f << std::flush;
}