
#include "PGMRead.h"
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <iostream>
#include <stdexcept>
#include <algorithm> 


PGMRead::PGMRead(std::string pathToImage){
    std::cout << pathToImage << std::endl;
    size_t lastindex = pathToImage.find_first_of("."); 
    this->filename = pathToImage.substr(0, lastindex);
    std::ifstream fin(pathToImage.c_str());
    std::string fileType;
    std::string dimensions;
    getline(fin, fileType);
    if(fileType != "P5" ) {
        std::cerr << " Only P5 Version suported" << std::endl;
        throw std::invalid_argument("Invalid PGM image type: " + fileType);
    }
    getline(fin,dimensions);
    auto elem = removeDupWord(dimensions);
    numcols = elem[0];
    numrows = elem[1];

    std::string value;
    getline(fin,value);
    elem = removeDupWord(value);
    originalmaxValue = elem[0];
    std::stringstream buffer;
    buffer << fin.rdbuf();
    std::string contents(buffer.str());
    std::vector<int> data;
    for (auto letter:contents){
        auto a = (unsigned char)letter;
        data.push_back((int) a);
    }
    auto max_pointer = std::max_element(data.begin(),data.end());
    auto min_pointer = std::min_element(data.begin(),data.end()); 
    unsigned int index = std::distance(data.begin(), max_pointer);
    this->max = data[index];
    index = std::distance(data.begin(), min_pointer);
    this->min = data[index];
    std::vector<int> line;
    auto counter =0u;
    for (auto val: data){
        line.push_back(val);
        ++counter;
        if(counter==this->numcols){
            pixel_data.push_back(line);
            line.clear();
            counter=0;
        }       
    }
    
    if (this->numrows!=pixel_data.size() || this->numcols!=pixel_data[0].size()){
        std::cerr << "Dimensions mismatch" <<std::endl;
    }
    fin.close();
    find_real_min_max();
}

 std::vector<std::vector<int>> PGMRead::getData()
{
    return pixel_data;
}

std::string PGMRead::get_new_filename() const{
    return this->filename;
}

std::vector<int> PGMRead::removeDupWord(std::string str) 
{ 
    // Used to split string around spaces. 
    std::istringstream ss(str); 
    std::vector<int> elem;
    int word; 
    // Traverse through all words 
    while (ss >> word) { 
        elem.push_back(word);
    } 
    return elem;
} 
unsigned int PGMRead::get_cols()const{
    return this->numcols;
}

unsigned int PGMRead::get_rows()const{
    return this->numrows;
}

std::pair<int, int> PGMRead::get_min_max() const{
    return std::pair<int,int>(this->real_min, real_max);
}


void PGMRead::printImgInfo()const{

    std::cout<<"Number of Columns: " << this->pixel_data.size() <<std::endl;
    std::cout<<"Number of Rows: " << this->pixel_data[0].size() <<std::endl;
    std::cout<<"min pixel intensity: " << this->min << "\n"; 
    std::cout<<"max pixel intensity: " << this->max << "\n"; 

}
void PGMRead::printData() const {    
    for(std::vector<int> line:this->pixel_data) {
        for (auto elem:line){
        std::cout<< elem << " ";
        }
        std::cout<< std::endl;
    }
}

void PGMRead::find_real_min_max(){
    int min = 0;
    int max = 0;
    for (auto line:this->pixel_data){
        for(auto pixel:line){
            if(pixel > max){
                max = pixel;
            }
            if(pixel < min){
                min = pixel;
            }
        }
    }
    this->real_max = max;
    this->real_min = min;
}
