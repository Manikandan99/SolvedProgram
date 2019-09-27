#include<stdio.h>
void main()
{
	int n,i,j,m,t,o=0;
	scanf("%d",&n);
	char input[n],output[10];
	scanf("%s",input);
	m=n/2;
	for(i=0;i<m;i++)
	{
		output[o++]=input[i];
		output[o++]=input[n-i-1];
	}
	if (n%2!=0)
	{
		output[o++]=input[i];
	}
	output[o]='\0';
	printf("%s",output);
}
