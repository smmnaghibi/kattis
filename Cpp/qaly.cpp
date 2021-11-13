#include<iostream>
using namespace std;

int main(){
    int n;
    double res = 0;
    cin >> n;
    if (1 <= n && n <= 100){
        for(int i = 0; i < n; i++){
            double a, b;
            cin >> a >> b;
            if (0 < a && a <= 1 && 0 < b && b <= 100){
                double mul;
                mul = a * b;
                res += mul;
            }
        }
    }
    cout << res;
}
