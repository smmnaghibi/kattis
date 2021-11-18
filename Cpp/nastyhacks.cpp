#include<iostream>
#include<math.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    if (1 <= n && n <= 100){
        for (int i = 0; i < n ; i++){
            int a, b, c;
            cin >> a >> b >> c;
            if (-(pow(10,6)) <= a && a <= pow(10,6) && -(pow(10,6)) <= b && b <= pow(10,6) && -(pow(10,6)) <= c && c <= pow(10,6)){
                if(b - c > a) cout << "advertise" << endl;
                else if(b - c == a) cout << "does not matter" << endl;
                else if(b - c < a) cout << "do not advertise" << endl;
            }   
        }
    }
}
