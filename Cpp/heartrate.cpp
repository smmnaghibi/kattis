#include<iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    if (1 <= n && n <= 1000){
        for (int i = 0; i < n; i++){
            int a;
            float b;
            cin >> a >> b;
            if (2 <= a && a <= 1000 && 0 < b && b < 1000){
                float bpm, abpmm, abpmmax;
                bpm = (float)(60 * a) / b;
                abpmm = (float)(bpm - 60 / b);
                abpmmax = (float)(bpm + 60 / b);
                cout << abpmm << ' ' << bpm << ' ' << abpmmax << endl;
            }
        }
    }
}
