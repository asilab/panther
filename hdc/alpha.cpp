#include <vector>
#include <iostream>
#include <math.h>
#include "alpha.h"

Alpha::Alpha(std::vector<std::pair<int,double>> hdc){
auto log_hdc = log_of_vect(hdc);
auto pair = best_fit(log_hdc);

this->m = pair.first;
this->b = pair.second;
this->alpha = comp_alpha();
}

std::vector<std::pair<double,double>> Alpha::log_of_vect( std::vector<std::pair<int,double> > hdc){
    std::vector<std::pair<double,double>> hdr_log;
    for (auto pair: hdc){
        double r = log10(pair.first);
        double gr =  log10(pair.second);
        std::pair<double, double> log_hdr(r,gr);
        hdr_log.push_back(log_hdr);
    }
    return hdr_log;
}
std::pair<double,double> Alpha::best_fit(std::vector<std::pair<double,double>> hdc){

    double x_sum=0;
    double y_sum=0;
    double sample_len =hdc.size();

    for (auto pair: hdc){
        x_sum+=pair.first;
        y_sum+=pair.second;
    }

    double xbar = x_sum/ sample_len;
    double ybar = y_sum/ sample_len;

    double num=0;
    double den=0;

    for (auto pair:hdc){    
        num += (pair.first * pair.second);
        den += (pair.first*pair.first);
    }

    double numerator = num - (sample_len*xbar*ybar);
    double denominator = den - (sample_len*xbar*xbar);

    double m = numerator / denominator;
    double b = ybar - (m * xbar);
    std::pair<double, double> fit(m,b);
    return fit;
}

double Alpha::comp_alpha(){
    return this->m/2;
}

double Alpha::getAlpha(){
    return this->alpha;
}

void Alpha::printAlpha(){
    std::cout<<this->alpha<< std::endl;
}
void Alpha::print_fit(){
    std::cout << "y = " << this->m << "x + " << this->b << std::endl; 
}


//numer = sum([xi*yi for xi,yi in zip(X, Y)]) - (n * xbar * ybar)
//denum = sum([xi**2 for xi in X]) - (n * xbar**2)

// # sample points 
// X = [0, 5, 10, 15, 20]
// Y = [0, 7, 10, 13, 20]

// # solve for a and b
// def best_fit(X, Y):

//     xbar = sum(X)/len(X)
//     ybar = sum(Y)/len(Y)
//     n = len(X) # or len(Y)

//     numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
//     denum = sum([xi**2 for xi in X]) - n * xbar**2

//     b = numer / denum
//     a = ybar - b * xbar

//     print('best fit line:\ny = {:.2f} + {:.2f}x'.format(a, b))

//     return a, b

// # solution
// a, b = best_fit(X, Y)
