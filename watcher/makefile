CC=gcc
CFLAG= -O2
CLIBS= 

all: watcher
clean: 
	rm watcher
install:all
	cp watcher /usr/bin/
uninstall:
	rm /usr/bin/watcher
.PHONY: all clean install uninstall
watcher:watcher.c watcher.h
	gcc -o $@ $< $(CFLAG) $(CLIBS)

