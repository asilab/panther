#pragma once
#include <string>
#include<vector>
class PGMRead
{
    public:
        PGMRead(std::string pathToImage);
      
        std::vector<std::vector<int>>  getData();
        void printData() const;
        void printImgInfo() const;
        unsigned int get_rows() const;
        unsigned int get_cols() const;
        std::pair<int, int> get_min_max() const;
        std::string get_new_filename() const;

    protected:
    private:
        unsigned int numrows;
        unsigned int numcols;
        unsigned int max;
        unsigned int min;
        int real_min;
        int real_max;
        std::string filename;
        unsigned int originalmaxValue;
        std::vector<std::vector<int>> pixel_data;
        std::vector<int> removeDupWord(std::string);
        void find_real_min_max();
};