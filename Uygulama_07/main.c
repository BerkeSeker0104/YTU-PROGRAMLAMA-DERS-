#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Disaridan girilen n elemanli bir dizinin elemanlarinin ortalamasinin ustunde kac eleman oldugunu bulan bir program yaziniz.

    int n, dizi[100];
    printf("Lutfen dizimizin kac elemanli olacagini giriniz : \n");
    scanf("%d", &n);

    for(int i=0;i<n;i++){
        printf("dizi[%d]:",i);
        scanf("%d", &dizi[i]);
    }

    int toplam=0;

    for(int i=0;i<n;i++){
        toplam=toplam+dizi[i];
    }

    int ort=toplam/n;
    int buyuk=0;

    for(int i=0;i<n;i++){
        if(dizi[i]>ort){
            buyuk=buyuk+1;
        }
    }
    printf("ortalamadan buyuk %d kadar elemanimiz var.", buyuk);

    return 0;
}
