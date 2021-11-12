#include<iostream>
using namespace std;

int main(){
    int r1, s, temp;
    cin >> r1 >> s;
    if (-1000 <= r1 && r1 <= 1000 && -1000 <= s && s <= 1000){
        temp = s - r1;
        cout << temp + s;
    }
}
