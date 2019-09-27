#include<stdio.h>
void main()
{
	int i;
	char inch[10];
	scanf("%s",&inch);
	for(i = 0; inch[i] != '\0'; ++i);
	printf("%d",i);	
}
