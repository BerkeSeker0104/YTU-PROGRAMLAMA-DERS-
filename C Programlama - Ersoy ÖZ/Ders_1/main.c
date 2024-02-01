#include <stdio.h>
#include <stdlib.h>

int main()
{

    // 1.Proje

    int a,b,alan,cevre;

    printf("Bir kenar uzunluðu giriniz \n");
    scanf("%d", &a);

    printf("Diger kenar uzunlugunu giriniz \n");
    scanf("%d", &b);

    cevre=2*(a+b);
    alan=a*b;

    printf("Dikdortgenin cevresi: %d ve alani: %d \n", cevre,alan);

    // 2. Proje

    int x,y,z,enb;
    printf("Lutfen bir x sayisi giriniz:");
    scanf("%d", &x);
    printf("Lutfen bir y sayisi giriniz:");
    scanf("%d", &y);
    printf("Lutfen bir z sayisi giriniz:");
    scanf("%d", &z);

    if(x>y){
        if(x>z){
            enb=x;
        }else{
            enb=z;
        }

    }else{
        if(y>z){
            enb=y;
        }else{
            enb=z;
        }
    }

    printf("En buyuk sayi: %d", enb);


    return 0;
}
