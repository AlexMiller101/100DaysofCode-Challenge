// Print the sum of the even fibonacci numbers
// It is not optimal or efficient for n >= 40

#include<stdio.h>
#include<stdlib.h>

int fibonacci(n)
{
    if(n <= 1){
        return n;
    }
    else{
        return fibonacci(n-1) + fibonacci(n-2);
    }
}

int main(int argc, char* argv[])
{
    int i = 1;
    int n = atoi(argv[1]);
    int sum = 0;

    for(i=1; i<=n; i++){
        if(fibonacci(i) % 2 == 0){
            if(fibonacci(i)==2){
                printf("%d", fibonacci(i));
            }else{
                printf("+%d", fibonacci(i));
            }
            sum = sum + fibonacci(i);
        }
    }

    printf(" =");
    printf(" %d", sum);
    printf("\n");

    return 0;
}