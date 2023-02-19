# include<iostream>
/*
class Something
{
    private:
        int m_value1 {};
        double m_value2 {};
        char m_value3 {};
    
    public:
        Something()
    {
        // These are all assignments, not initializations
        m_value1 = 1;
        m_value2 = 2.2;
        m_value3 = 'c';
    }
};

int main(){

    return 0;
}
*/

/*
class Something {
    private:
    int m_value1{};
    double m_value2{};
    char m_value3{} ;

    public:
        Something(): m_value1{1}, m_value2{2.2}, m_value3{'c'} // Constructor Member Initializer Lists
        {
            // No need for assignment because variables are initialized
        }
        void print(){
            std::cout<<"m_value1"<<m_value1<<"m_value2"<<m_value2<<"m_value3"<<m_value3<<std::endl;
        }
        Something(int value1, double value2, char value3='c'):
        m_value1{value1}, m_value2{value2}, m_value3{value3}{

        }

};

int main(){
    Something something;
    something.print();
    Something something2;
    Something otherthing{2,4.4,'f'};
    otherthing.print();
    return 0;
}
*/

// Initializing array members with member initializer lists

class Something{
    private:
    const int m_array[5];
    public:
        Something(): m_array{1,2,3,4,5}{
            // Uniform initialization to initialize member array
        }
};