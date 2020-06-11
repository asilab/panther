#pragma once
#include <string>
#include<vector>
class DivideImage
{
    public:
        DivideImage(std::vector<std::vector<int>> pixel_value, unsigned int number_of_blocks);
        std::vector<std::vector<std::vector<int>>>  get_data();
        unsigned int get_rows();
        unsigned int get_cols();

    protected:
    private:
        std::vector<std::vector<std::vector<int>>>  data_blocks;
        unsigned int numcols;
        unsigned int numrows;
        std::vector<std::vector<int>> pixel_data;

};