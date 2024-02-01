#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Disaridan uc kenarinin uzunlugu girilen bir ucgenin ne cesit bir ucgen (eskenar,ikizkenar,cesitkenar)
    // oldugunu bulan programi yazin.

    int a, b, c, ucgen;
    printf("Ucgenin kenarlari icin uc adet kenar giriniz : \n");
    scanf("%d%d%d", &a,&b,&c);

    if(a==b){
        if(a==c){
            ucgen=1; //eskenar ucgene 1 dedim
        }else{
            ucgen=2; //ikizkenara 2 dedim
        }
    }else if(a==c){
        ucgen=2;
    }else if(b==c){
        ucgen=2;
    }else{
        ucgen=3; //cesitkenar ucgene 3 dedim
    }

    switch(ucgen){

    case 1:
        printf("Ucgenimiz eskenar ucgen. \n");
        break;
    case 2:
        printf("Ucgenimiz ikizkenar ucgen. \n");
        break;
     default:
        printf("Ucgenimiz cesitkenar ucgen. \n");
        break;

    }




    return 0;
}
