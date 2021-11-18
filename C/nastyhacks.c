#include<stdio.h>
#include<math.h>

int main(){
    int n;
    scanf("%d", &n);
    if (1 <= n && n <= 100){
        for (int i = 0; i < n ; i++){
            int a, b, c;
            scanf("%d %d %d", &a, &b, &c);
            if (-(pow(10,6)) <= a && a <= pow(10,6) && -(pow(10,6)) <= b && b <= pow(10,6) && -(pow(10,6)) <= c && c <= pow(10,6)){
                if(b - c > a) printf("advertise\n");
                else if(b - c == a) printf("does not matter\n");
                else if(b - c < a) printf("do not advertise\n");
            }   
        }
    }
}
