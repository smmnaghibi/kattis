#include<stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    if (1<= n && n <= 10000000){
        if (n % 2 == 0) printf("Bob");
        else printf("Alice");
    }
}