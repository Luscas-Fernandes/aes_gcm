#include <stdio.h>
#include "configs.h"


// Implementation of an AES
// AES working with 128bits block encryption
// Therefore 128bits keys 

// 0123456789ABCDEF

int main()
{
    unsigned char *a;
    unsigned char **block;

    a = (char *) malloc(17 * sizeof(char)); // 16 bits + '\0' char

    printf("New string to a (16 bytes): ");
    scanf(" %s", a);

    block = block_text(a);


    #ifdef DEBUG
        printf("Text is multiple of 16 bytes!\n");

        for(int i = 0; i < 4; i++)
        {
            for(int j = 0; j < 4; j++)
                {
                    printf("block[%d][%d]: %c\t", j, i, block[j][i]);                 
                }
            printf("\n");
        }
    #endif 

    printf("End of program\n");

    return 0;
}