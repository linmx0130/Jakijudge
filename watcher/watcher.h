#include <unistd.h>
#include <sys/resource.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <getopt.h>
#include <signal.h>
#include <sys/time.h>
#include <errno.h>
#include <sys/wait.h>
#include <sys/types.h>
#define VAR_DATA "0.0Alpha"
void argument_get(int argc, char **argv);
void check_int_string(char *s);
void wait_process(int pid);
void help_show();
