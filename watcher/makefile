CC=gcc
CFLAG= -O2
CLIBS= 

all: watcher
clean: 
	rm watcher
.PHONY: all clean
watcher:watcher.c watcher.h
	gcc -o $@ $< $(CFLAG) $(CLIBS)
