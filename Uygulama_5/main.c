#include <stdio.h>
#include <stdlib.h>

int main()
{
    // disaridan girilen n elemanli bir dizideki elemanlarin toplamini bulan program yaziniz.

    int n, toplam, dizi[100];
    printf("Dizimizin kac elemanli olacagini yaziniz : \n");
    scanf("%d", &n);

    toplam=0;

    for(int i=0;i<n;i++){  //for dongusu ile dizimize eleman atadik
        printf("Dizi[%d]=",i);
        scanf("%d", &dizi[i]);
    }

     for(int i=0;i<n;i++){  //for dongusu ile dizimizi bastirdik
        printf("Dizimizin elemanlari : dizi[%d] = %d\n",i,dizi[i]);

    }

    for(int i=0;i<n;i++){
        toplam=toplam + dizi[i];
    }

    printf("Dizimizin elemanlarinin toplami = %d \n", toplam);



    return 0;
}
