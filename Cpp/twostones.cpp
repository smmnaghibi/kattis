#include<iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    if (1<= n && n <= 10000000){
        if (n % 2 == 0) cout << "Bob";
        else cout << "Alice";
    }
}