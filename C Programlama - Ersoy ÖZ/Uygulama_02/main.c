#include <stdio.h>
#include <stdlib.h>

int main()
{
    // disaridan girilen uc degiskenden en buyuk olani bulan programini yaziniz.

    int a, b, c;
    printf("Lutfen uc adet sayi giriniz : \n");
    scanf("%d%d%d", &a, &b, &c);

    if(a>b && a>c){

        printf("En buyuk sayi a:%d . \n", a);
    }else{
        if(b>c){
            printf("En buyuk sayi b:%d", b);
        }else{
            printf("En buyuk sayi c:%d", c);
        }
    }




    return 0;
}
