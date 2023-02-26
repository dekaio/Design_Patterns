#include<iostream>
using namespace std;


int square(int x){
    
    return x*x;
}

template <typename T>
T square(T x){
    return x*x;
}

template <typename T>
class BoVector{
    T arr[1000];
    int size;
    public:
        BoVector(): size(0){}
        void push(T x){arr[size] = x; size++;}
        T get(int i) const {return arr[i];}
        int getSize() const {return size;}
        void print() const {for (int i=0;i <size; i++) {cout<<arr[i]<<endl;}}
};
template <typename T>
BoVector<T> operator*(const BoVector<T> &rhs1, BoVector<T> &rhs2){
    BoVector<T> ret;
    for (int i=0;i<rhs1.getSize();i++){
        ret.push(rhs1.get(i)*rhs2.get(i));
    }
    return ret;
}
int main(){
    std::cout<<square(5)<<std::endl;
    std::cout<<square(5.5)<<std::endl;
    std::cout<<square<double>(5.5)<<std::endl; //No need to specify type for function calling

    BoVector<int> bv; //Data type has to be passed for class template
    bv.push(2);
    bv.push(3);
    bv.push(4);
    bv.print();
    bv = square(bv);
    bv.print();



}