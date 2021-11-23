#include<stdio.h>

int main(){
    int a , b;
    scanf("%d %d", &a, &b);
    if (1 <= a && a <= 100 && 1 <= b && b <= 100){
        int res = (b - 1) * a;
        printf("%d", res + 1);
    }
}
