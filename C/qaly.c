#include<stdio.h>

int main(){
    int n;
    float res = 0;
    scanf("%d", &n);
    if (1 <= n && n <= 100){
        for(int i = 0; i < n; i++){
            float a, b;
            scanf("%f %f",&a,&b);
            if (0 < a && a <= 1 && 0 < b && b <= 100){
                float mul;
                mul = a * b;
                res += mul;
            }
        }
    }
    printf("%f", res);
}
