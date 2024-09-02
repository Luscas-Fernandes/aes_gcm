#pragma once
#ifndef configs
#define configs
#define DEBUG 1

#include <stdio.h>
#include <string.h>
#include <stdlib.h> 

//char **block_text(char *plain_text);
unsigned char **block_text(char *plain_text);
unsigned char **sub_bytes(unsigned char **block_text);

#define KEY_LENGHT_128 128 // example
#define PLAIN_TEXT_LENGHT 16 // 16 bytes

#endif // configs