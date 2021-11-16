#include<stdio.h>

int pow(int a, int b){
    int x = 1;
    for (int i = 0; i < b; i++) x *= a;
    return x;
}

int main(){
    int n, res = 2;
    scanf("%d", &n);
    if (1 <= n && n <= 15){
        for (int i = 0; i < n ;i++){
            res += pow(2,i);
        }
    }
    printf("%d", res * res);
}
