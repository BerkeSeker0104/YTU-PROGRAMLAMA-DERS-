#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#define  pi 3.14


int main()
{
    // yaricapi disaridan girilen bir dairenin cevresini ve alanini bulan program yazin.


    float r, cevre, alan;
    printf("yaricap : \n");
    scanf("%f", &r);

    cevre = 2*pi*r;
    alan = pi*r*r;

    printf("Dairemizin cevresi : %.2f \n", cevre);
    printf("Dairemizin alani : %.2f \n", alan);


    return 0;
}
