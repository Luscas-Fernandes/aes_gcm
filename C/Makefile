CC=gcc
CFLAGS=-Wall -g

main: main.o aes.o
	$(CC) $(CFLAGS) main.o aes.o -o main

#aes.o: aes.c
#	$(CC) $(CFLAGS) -c aes.c

#main.o: main.c
#	$(CC) $(CFLAGS) -c main.c

clean:
	rm -f main *.o