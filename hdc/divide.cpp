#include <iostream>
#include <cmath>
#include "divide.h"

template<typename T>
std::vector<std::vector<T>> SplitVector(const std::vector<T>& vec, size_t n)
{
    std::vector<std::vector<T>> outVec;

    size_t length = vec.size() / n;
    size_t remain = vec.size() % n;

    size_t begin = 0;
    size_t end = 0;

    for (size_t i = 0; i < std::min(n, vec.size()); ++i)
    {
        end += (remain > 0) ? (length + !!(remain--)) : length;

        outVec.push_back(std::vector<T>(vec.begin() + begin, vec.begin() + end));

        begin = end;
    }

    return outVec;
}

std::vector<std::vector<std::vector<int>>>  SplitVectorVector(const std::vector<std::vector<std::vector<int>>>& group_images, size_t n){
    std::vector<std::vector<std::vector<int>>> output_group_image;    

    for (auto image:group_images){
    std::vector<std::vector<std::vector<int>>> untangled_group_image(n);    

        for (auto line:image){
            auto split_line = SplitVector(line,n);
            //  std::cout<<"split_line.size: "<< split_line.size() << std::endl;
            for (auto counter=0u; counter<split_line.size();++counter){
                // std::cout<<"here"<< std::endl;
                auto be =untangled_group_image[counter];
                // std::cout<<"be"<< std::endl;
                auto ce = split_line[counter];
                // std::cout<<"ce"<< ce.size()<< std::endl;
                untangled_group_image[counter].push_back(split_line[counter]);
            }
        }
        for (auto image:untangled_group_image){
            output_group_image.push_back(image);
        }
    }
    return output_group_image;
}

DivideImage::DivideImage(std::vector<std::vector<int>> pixel_value, unsigned int number_of_blocks){
    this->pixel_data = pixel_value;
    this->numcols = get_cols();
    this->numrows = get_rows();
    auto number_blocks = static_cast<int>(std::sqrt(number_of_blocks));

    auto line_divisions = SplitVector(pixel_value,number_blocks);
    this->data_blocks = SplitVectorVector(line_divisions,number_blocks );
}
std::vector<std::vector<std::vector<int>>>  DivideImage::get_data(){
    return this->data_blocks;
}

unsigned int  DivideImage::get_rows(){
    return this->pixel_data.size();
}

unsigned int  DivideImage::get_cols(){
    return this->pixel_data[0].size();
}