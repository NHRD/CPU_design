#include <stdio.h>

int main(void) {
    short sum;
    
    asm("
            mov ax, 0
            mov bx, 1
    LOOP1:  cmp bx, 11
            je MOUT
            add ax, bx
            inc bx
            jmp LOOP1
    MOUT:   mov sum, ax
    ");
    
    printf("sum = %d\n" ,sum);
    return 0;
}