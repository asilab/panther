#pragma once
#include <vector>
#include "PGMRead.h"
class HDC
{
    public:
        HDC(PGMRead img, unsigned int start_radius=1, double percentage_radious=1);
        std::vector<std::pair<int,double>> get_hdc() const;
        void printData();
        void print_hdc() const;
        
    protected:
    private:
        unsigned int numrows;
        unsigned int numcols;
        unsigned int max_radius;
        std::vector<std::vector<int>> pixel_data;
        std::vector<std::pair<int,double>> hdc;       
        
        std::vector<std::pair<int,double>> hdc_comp(unsigned int radious_start);
        double hdc_radius(int radius);
        std::vector<int> hdc_point(unsigned int row, unsigned int col, int radius);
        int get_max_radius(double percentage);
        std::vector<int> get_border(unsigned int row, unsigned int col, int radius);
        std::vector<int> compute_quadratic_diff(unsigned int central_pixel, std::vector<int> border);//can be done in cache
};

