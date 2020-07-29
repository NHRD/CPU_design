#include <stdio.h>

int i;
int sum;

int main(void){
    sum = 0;
    for(i = 1; i <= 10; i++) {
        sum = sum + i;
    }
    printf("sum = %d \n" , sum);
    return 0;
}