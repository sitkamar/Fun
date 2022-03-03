#include<iostream>
using namespace std;
int main(){
    int a = 10,b;
    b = (a=50) +10;
    cout << a << '$' << b;
    return 0;
}