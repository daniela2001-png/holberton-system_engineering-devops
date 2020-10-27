#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * infinite_while - Infinite loop with 1min of delay
 *
 * Return: 0
 *
 **/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point
 *
 * Return: Always return 0
 *
 **/
int main(void)
{
	pid_t child_pid;
	int count;

	for (count = 0; count < 5; count++)
	{
		child_pid = fork();
		if (child_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
		}
		else if (child_pid == 0)
		{
			exit(0);
		}
	}
	infinite_while();

	return (0);
}
