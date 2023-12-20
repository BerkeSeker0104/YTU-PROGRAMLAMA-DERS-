#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Disaridan girilen N elemanli bir dizideki pozitif elemanlarin ortlamasini bulan program yaziniz.

    int n, dizi[100];

    printf("Lutfen dizimiz kac elemanli olacak giriniz : \n");
    scanf("%d", &n);

    for(int i=0; i<n; i++){
        printf("dizi[%d] : ",i);
        scanf("%d", &dizi[i]);
    }

    int toplam=0;

    for(int i=0; i<n; i++){
        toplam=toplam+dizi[i];
    }

    int ort=toplam/n;
    printf("dizimizin ortalamasi : %d ", ort);

    return 0;
}
