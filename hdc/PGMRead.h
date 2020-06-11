#pragma once
#include <string>
#include<vector>
class PGMRead
{
    public:
        PGMRead(std::string pathToImage);
      
        std::vector<std::vector<int>>  getData();
        void printData();
        void printImgInfo();
        unsigned int get_rows();
        unsigned int get_cols();

    protected:
    private:
        unsigned int numrows;
        unsigned int numcols;
        unsigned int max;
        unsigned int min;
        unsigned int originalmaxValue;
        std::vector<std::vector<int>> pixel_data;
        std::vector<int> removeDupWord(std::string);

};