#include<iostream>
using namespace std;

int main(){
    int n, h, v, x, y;
    cin >> n >> h >> v;
    if (2 <= n && n <= 10000 && 0 < h && h < n && 0 < v && v < n){
        if (n - h > h) x = n - h;
        else x = h;
        if (n - v > v) y = n - v;
        else y = v;
    }
    cout << x * y * 4;
}
