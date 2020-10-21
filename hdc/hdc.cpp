#include <algorithm>
#include <iostream>
#include<numeric>
#include <iterator>
#include "hdc.h"

template<typename T>
void printVector(const T& t) {
    std::copy(t.cbegin(), t.cend(), std::ostream_iterator<typename T::value_type>(std::cout, ", "));
}

template<typename T>
void printVectorInVector(const T& t) {
    std::for_each(t.cbegin(), t.cend(), printVector<typename T::value_type>);
}


HDC::HDC(PGMRead img, unsigned int start_radius, double percentage_radious){
    this->pixel_data = img.getData();
    this->numrows = img.get_rows();
    this->numcols = img.get_cols();
    this->max_radius=get_max_radius(percentage_radious);
    if(pixel_data.empty() || numcols ==0 || numrows == 0 || max_radius ==0){
        std::cerr<< " Problem " << std::endl;
        exit(88);
    }
    this->hdc=hdc_comp(start_radius);
}

std::vector<std::pair<int,double>> HDC::hdc_comp(unsigned int radius_start){
    std::vector<std::pair<int,double>>  hdc;
    for (auto r=radius_start;r<=this->max_radius;++r){
        std::pair<int,double> val(r,hdc_radius(r));
        hdc.push_back(val);
    }
    return hdc;
}
void HDC::print_hdc() const{
    auto v = get_hdc();
    for (auto&hdc:this->hdc){
        std::cout << "(" << hdc.first << ","<< hdc.second << ")\t";
    }
}

double HDC::hdc_radius(int radius){
    std::vector<int> hdc_quadratic_diff;
    for (auto row=0u; row<this->numrows; ++row){
        for (auto col=0u; col<this->numcols;++col){
            auto region_diff =hdc_point(row, col, radius);
            // printVector(region_diff);
            // std::cout<<std::endl;
            hdc_quadratic_diff.insert( hdc_quadratic_diff.end(),
                                         region_diff.begin(),
                                          region_diff.end() );
        }
    }
    long long unsigned int sum_all_elem=0;
    for (auto a:hdc_quadratic_diff){
        sum_all_elem+=a;
    }
    long long unsigned int num_elm = hdc_quadratic_diff.size();
    // std::cerr << "sum all elem : "<< sum_all_elem << std::endl;
    // std::cerr << "num_elm : "<< num_elm << std::endl;
    //printVector(hdc_quadratic_diff);
    return static_cast<double>(sum_all_elem)/static_cast<double>(num_elm);
}

int HDC::get_max_radius(double percentage){
    auto max_possible_radius = std::min(numrows,numcols)-1;
    return max_possible_radius*percentage;
}

std::vector<int> HDC::hdc_point(unsigned int row,unsigned int col, int radius){
    unsigned int central_pixel = this->pixel_data[row][col];    
    auto border = get_border(row, col, radius);
    return compute_quadratic_diff(central_pixel, border);
}


std::vector<int> HDC::get_border(unsigned int row, unsigned int col, int radius){
    std::vector<int> neighbors;
    std::vector<int> border_pixels;
    int i_min = std::max(0, signed(row) - signed(radius));
    int i_max = std::min(this->numrows - 1, row + radius);
    int j_min = std::max(0, signed(col) - signed(radius));
    int j_max = std::min(this->numcols - 1, col + radius);
    
    int lower_i = std::max(i_min, ( signed(row) - signed(radius) ) + 1);
    int higher_i = std::min(i_max, ( signed(row) + signed(radius) ) - 1);
    int lower_j = std::max(j_min, (signed(col) - signed(radius)) + 1);
    int higher_j = std::min(j_max, (signed(col) + signed(radius)) - 1);

    std::vector<int> possible_i;
    std::vector<int> possible_j;
    
    auto bound_ini = higher_i + 1;
    auto bound_end = i_max + 1;
    for (auto i=i_min; i<lower_i;++i){
        possible_i.push_back(i);
    }
    for (auto i=bound_ini; i<bound_end;++i){
        possible_i.push_back(i);
    }
    bound_ini = higher_j + 1;
    bound_end = j_max + 1;
    for (auto i=j_min; i<lower_j;++i){
        possible_j.push_back(i);
    }
    for (auto i=bound_ini; i<bound_end;++i){
        possible_j.push_back(i);
    }

    for (auto i:possible_i){
        for (auto j=j_min;j<=j_max;++j){
            border_pixels.push_back(this->pixel_data[i][j]);
        }
    }
    for (auto j:possible_j){
        for (auto i=lower_i;i<=higher_i;++i){
            border_pixels.push_back(this->pixel_data[i][j]);
        }
    }
    return border_pixels;
}

std::vector<int> HDC::compute_quadratic_diff(unsigned int central_pixel, std::vector<int> border){
    std::vector<int> quadratic_diff;
    for(auto element : border){
        if (element<0){std::cerr<<"BORDER ERROR"<< std::endl; exit(88);}
        element -= central_pixel;
        element *= element;
        quadratic_diff.push_back(element);
    }
    return quadratic_diff;
}


void HDC::printData(){
    std:: cout<< "Radius" << "\t" << "HDC" << std::endl;
    for (auto pair:this->hdc){
        std:: cout<< pair.first << "\t" << pair.second << std::endl;
    }
}

std::vector<std::pair<int,double>> HDC::get_hdc() const{
    return this->hdc;
}
