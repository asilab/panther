#pragma once
#include <string>
#include<vector>

class PGMWrite
{
    public:
        PGMWrite(std::vector<std::vector<int> > pixel_data,std::string pathToImage);  
        void write(std::string pathToImage);    
        int determine_max_value();
        unsigned int get_rows();
        unsigned int get_cols();

    protected:
    private:
        unsigned int numrows;
        unsigned int numcols;
        unsigned int maxValue;
        std::vector<std::vector<int>> pixel_data;

};