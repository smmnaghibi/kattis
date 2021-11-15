#include<stdio.h>

int pow(int a, int b){
    int mul = 1;
    for (int i = 0; i < b; i++){
        mul *= a;
    }
    return mul;
}

int main(){
    int n, res = 0;
    scanf("%d", &n);
    for (int i = 0 ; i < n ; i++){
        int inp;
        scanf("%d", &inp);
        if (10 <= inp && inp <= 9999){
            res += pow(inp/10,inp%10);
        }
    }
    printf("%d",res);
}
