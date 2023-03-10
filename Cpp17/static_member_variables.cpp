#include <iostream>
// Static makes the memebre keep it's value during program execution.
// Static members are not associated with class objects. They are created when the program starts and destroyed when the 
// program ends
int generateID(){
    static int s_id{0};
    return ++s_id;
}

class Something{
    public:
        static int s_value;
};

int Something::s_value{1};
int main(){
    Something first;
    Something second;
    first.s_value = 2;
    std::cout<<"First.value"<<first.s_value<<'\n';
    std::cout<<"Second value"<<second.s_value<<'\n';

    Something::s_value = 5;
    std::cout<<"First.value"<<first.s_value<<'\n';
    std::cout<<"Second value"<<second.s_value<<'\n';
    return 0;
}
