#include <stdio.h>

int Max(int x, int y){
    if (x > y) return x;
    else return y;
}

int Min(int x, int y){
    if (x > y) return y;
    else return x;
}

int main(){
    int a, b;
    scanf("%d %d", &a ,&b);
    if (4 <= a && a <= 20 && 4 <= b && b <= 20){
        int m = Max(a, b);
        int k = Min(a, b);
        if (a != b){
            for (int i = (k + 1); i < (m + 2); i++){
                printf("%d\n" , i);
            }
        }
        else printf("%d\n", k + 1);
    }
}
