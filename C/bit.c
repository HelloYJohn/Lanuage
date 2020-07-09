#include <stdio.h>

int main() {
    int BITS_ON[7];
    int BITS_OFF[7];
    for(int i = 0, bit = 1; i < 7; i++, bit <<=1) {
        BITS_ON[i] = bit;
        BITS_OFF[i] = ~bit;
    }
    for (int i = 0; i < 7; i++) {
        printf("BITS_ON[%d] = %d \t", i, BITS_ON[i]);
    }
    for (int i = 0; i < 7; i++) {
        printf("BITS_OFF[%d] = %d \t", i, BITS_OFF[i]);
    }
    return 0;
}
