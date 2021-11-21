#include<iostream>
using namespace std;

int main(){
    int a, b, c;
    cin >> a >> b >> c;
    if (1 <= a && a < b && b <= c && c <= 100){
        for (int i = 1; i < c+1; i++){
            if (i % a == 0 && i % b != 0) cout << "Fizz" << endl;
            else if(i % b == 0 && i % a != 0) cout << "Buzz" << endl;
            else if(i % a == 0 && i % b == 0) cout << "FizzBuzz" << endl;
            else cout << i << endl;
        }
    }
}
