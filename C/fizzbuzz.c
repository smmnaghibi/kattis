#include<stdio.h>

int main(){
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    if (1 <= a && a < b && b <= c && c <= 100){
        for (int i = 1; i < c+1; i++){
            if (i % a == 0 && i % b != 0) printf("Fizz\n");
            else if(i % b == 0 && i % a != 0) printf("Buzz\n");
            else if(i % a == 0 && i % b == 0) printf("FizzBuzz\n");
            else printf("%d\n", i);
        }
    }
}
