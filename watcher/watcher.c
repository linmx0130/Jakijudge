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
	int pid=fork();
	if (pid==0)
	{
		struct rlimit rlimit_data;
		rlimit_data.rlim_max=rlimit_data.rlim_cur=time_limit;
		setrlimit(RLIMIT_CPU,&rlimit_data);
		rlimit_data.rlim_max=rlimit_data.rlim_cur=memory_limit*1024*4;
		//The program is given the memory 4 times of the limit.
		setrlimit(RLIMIT_AS,&rlimit_data);
		if (execlp(exec_filename,exec_filename,(char*)0)==-1)
		{
			fprintf(stderr,"System Error:%s\n",strerror(errno));
			return 2;
		}
	}
	else
	{
		wait_process(pid);
	}
	return 0;
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
void wait_process(int pid)
{
	int status;
	struct rusage child_rusage;
	sleep((time_limit+999)/1000);
	//Time Limit Excceed Test
	if (!wait4(pid,&status,WNOHANG,&child_rusage))
	{
		kill(pid,SIGKILL);
		puts("1:Time Limit Exceeded");
		return ;
	}

	//Runtime Error Test
	if (WEXITSTATUS(status)||WIFSIGNALED(status))
	{
		puts("2:Runtime Error!");
		return ;
	}
	if ((int)child_rusage.ru_minflt*(getpagesize()>>10)>memory_limit)
	{
		puts("3:Memory Limit Exceeded");
		return ;
	}
	puts("0:Finished Succeed!");
	printf("Time Used: %d ms\n",
			(child_rusage.ru_utime.tv_sec+
			 child_rusage.ru_stime.tv_sec)*1000+
			(child_rusage.ru_utime.tv_usec+
			child_rusage.ru_stime.tv_usec)/1000);
	printf("Memory Used:%d KB\n",(int)child_rusage.ru_minflt*(getpagesize()>>10));

}
