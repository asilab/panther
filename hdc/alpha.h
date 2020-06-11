#pragma once
#include <vector>

class Alpha
{
    public:
        Alpha(std::vector<std::pair<int,double>> hdc);
        double getAlpha();
        void printAlpha();
        void print_fit();
        
    protected:
    private:
        double alpha;
        double m;
        double b;
        std::pair<double,double>  best_fit(std::vector<std::pair<double,double>> hdc);
        double comp_alpha();
        std::vector<std::pair<double,double>> log_of_vect(std::vector<std::pair<int,double>> hdc);   
};