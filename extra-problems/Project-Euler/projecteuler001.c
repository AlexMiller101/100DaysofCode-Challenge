// Find the sum of multiples of 3 and 5 below 1000

#include<stdio.h>
#include<stdlib.h>

int multiples(int n)
{
  int sum = 0;
  int i = 0;

  for(i = 1; i<n; i++){
      if(i % 3 == 0 || i % 5 == 0){
        sum = sum + i; 
      }
    }
  return sum;
}

int main(int argc, char* argv[])
{
  int n = atoi(argv[1]);
  int sum = multiples(n);
  printf("The Sum is: %d \n", sum);

  return 0;
}
