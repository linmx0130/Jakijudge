#include "watcher.h"
int time_limit,memory_limit,stack_limit,file_limit;
char exec_filename[1000];
const struct option argument_option[]=
{
	{"help",0,NULL,'h'},
	{"time",required_argument,NULL,'t'},
	{"memory",required_argument,NULL,'m'},
	{"stack",required_argument,NULL,'s'},
	{"file",required_argument,NULL,'f'},
	{"exec",required_argument,NULL,'e'}
};
const char* argument_option_short="ht:m:s:f:e:";


int main(int argc,char **argv)
{
	argument_get(argc, argv);
//only for debug
	printf("%d\n",time_limit);
	printf("%d\n",memory_limit);
	printf("%d\n",stack_limit);
	printf("%d\n",file_limit);
	printf("%s\n",exec_filename);
}


void argument_get(int argc, char 
				**argv)
{
	//default setting:
	time_limit=1000;
	memory_limit=131072;
	stack_limit=8192;
	file_limit=50;
	int c;
	int option_index=0;
	while (c=getopt_long(argc,argv,argument_option_short,argument_option,&option_index))
	{
		if (c==-1) break;
		switch(c)
		{
			case 'h':
				//help
				break;
			case 't':
				check_int_string(optarg);
				time_limit=atoi(optarg);
				break;
			case 'm':
				check_int_string(optarg);
				memory_limit=atoi(optarg);
				break;
			case 's':
				check_int_string(optarg);
				stack_limit=atoi(optarg);
				break;
			case 'f':
				check_int_string(optarg);
				file_limit=atoi(optarg);
				break;
			case 'e':
				strncpy(exec_filename,optarg,strlen(optarg));
				break;
			case '?':
				//getopt_long will puts something to stderr
				exit(1);
		}
	}
}
void check_int_string(char *s)
{
	char *c;
	for (c=s;*c;c++)
	{
		if (!((*c>='0')&&(*c<='9')))
		{
			fprintf(stderr,"Wrong Argument!\n");
			exit(1);
		}
	}
}
