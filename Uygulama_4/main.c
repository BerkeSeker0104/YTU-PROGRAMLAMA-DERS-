#include <stdio.h>
#include <stdlib.h>

int main()
{
    // disaridan girilen bir N tamsayisina kadar olan tamsayilarin toplamini bulan programini yaziniz.

    int n, toplam;
    printf("Lutfen bir n tamsayisi giriniz: \n");
    scanf("%d", &n);

    toplam=0;
    for(int i=0;i<=n;i++){
        toplam=toplam+i;
    }

    printf("n tamsayisina kadar olan sayilarin toplami = %d \n", toplam);

    return 0;
}
