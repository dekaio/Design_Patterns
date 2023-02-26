#include<iostream>


int square(int x){
    
    return x*x;
}

template <typename T>
T square(T x){
    return x*x;
}



int main(){
    std::cout<<square(5)<<std::endl;
    std::cout<<square(5.5)<<std::endl;
    std::cout<<square<double>(5.5)<<std::endl;
}