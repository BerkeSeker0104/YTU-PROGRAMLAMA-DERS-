#include <stdio.h>
#include <stdlib.h>

int main()
{
    // MxN boyutundaki bir matris disaridan giriliyor. Bu matrisdeki disaridan girilen bir x sayisindan buyuk olan elemanlari
    // B dizisine atayan programi yaziniz.

    int m,n,mat[m][n];

    printf("Lutfen satir giriniz: \n");
    scanf("%d", &m);
    printf("Lutfen sutun giriniz: \n");
    scanf("%d", &n);

    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            printf("mat[%d][%d] : ",i,j);
            scanf("%d",&mat[i][j]);
        }
    }

    int x, esayisi=0, b[esayisi];
    printf("Lutfen x tamsayisi giriniz: \n");
    scanf("%d",&x);

    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if(mat[i][j]>x){
                b[esayisi]=mat[i][j];
                esayisi=esayisi+1;
            }
        }
    }

    for(int i=0;i<esayisi;i++){
        printf("b[%d] : %d \n",i,b[i] );
    }

    return 0;
}
