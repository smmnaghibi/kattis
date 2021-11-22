#include<stdio.h>

int reverse(int n){
    int reverse=0, rem; 
    while(n!=0){    
        rem=n%10;      
        reverse=reverse*10+rem;    
        n/=10;    
    }
    return reverse;  
}

int Max(int x, int y){
    if (x > y) return x;
    else return y;
}

int main(){
    int a, b;
    scanf("%d %d", &a, &b);
    if (100 <= a && a <= 999 && a != b){
        printf("%d\n", Max(reverse(a), reverse(b)));
    }
}
