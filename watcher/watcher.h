#include <unistd.h>
#include <sys/resource.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <getopt.h>
#include <signal.h>
#include <sys/time.h>
#include <errno.h>
void argument_get(int argc, char **argv);
void check_int_string(char *s);
void wait_process(int pid);
