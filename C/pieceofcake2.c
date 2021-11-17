#include<stdio.h>

int main(){
    int n, h, v, x, y;
    scanf("%d %d %d", &n, &h, &v);
    if (2 <= n && n <= 10000 && 0 < h && h < n && 0 < v && v < n){
        if (n - h > h) x = n - h;
        else x = h;
        if (n - v > v) y = n - v;
        else y = v;
    }
    printf("%d", x * y * 4);
}
