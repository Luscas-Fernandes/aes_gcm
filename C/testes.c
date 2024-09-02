#include <stdio.h>

unsigned char mini_s_box[2][2] = 
{
    {0x01, 0x04},
    {0x03, 0x02}
};


int main()
{
    unsigned char a = 'j', b = '8';

    printf("char: %02x\tchar2: %02x\n", a, b);
    printf("char: %d\tchar2: %d\n", a, b);

    return 0;
}