#include<iostream>
using namespace std;

int main(){
    int x, n, p, res;
    cin >> x;
    if (1 <= x && x <= 100){
        cin >> n;
        if (1 <= n && n <= 100){
            for (int i = 0 ; i < n ; i++){
                cin >> p;
                res += x -p;
            }
        }
    }
    cout << res;
}