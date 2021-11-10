#include<stdio.h>

int main(){
   int x, n, p, res;
    scanf("%d", &x);
    res = x;
    if (1 <= x && x <= 100){
        scanf("%d", &n);
        if (1 <= n && n <= 100){
            for (int i = 0 ; i < n ; i++){
                scanf("%d", &p);
                res = res + (x - p);
            }
        }
    }
    printf("%d",res);
}
