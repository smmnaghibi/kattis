#include<iostream>
using namespace std;

int Max(int x, int y){
    if (x > y) return x;
    else return y;
}

int Min(int x, int y){
    if (x > y) return y;
    else return x;
}

int main(){
    int a, b;
    cin >> a >> b;
    if (4 <= a && a <= 20 && 4 <= b && b <= 20){
        int m = Max(a, b);
        int k = Min(a, b);
        if (a != b){
            for (int i = (k + 1); i < (m + 2); i++){
                cout << i << endl;
            }
        }
        else cout << k + 1 << endl;
    }
}
