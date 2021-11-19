#include<stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    if (1 <= n && n <= 1000){
        for (int i = 0; i < n; i++){
                   double b, p;
        scanf("%lf %lf", &b, &p);
        double x = 60.0 / p;
        double xb = x * b;
        printf("%.6f %.6f %.6f\n", xb - x, xb, xb + x); 
        }
    }
}
