#include <stdio.h>
#include <stdlib.h>

int main()
{
    //Disaridan girilen MxN elemanli bir matristeki pozitif elemanlarin ortalamasini bulan program yaziniz.
    int m,n, mat[m][n];

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

    int ptoplam=0;
    int padet=0;

    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if(mat[i][j]>0){
                ptoplam=ptoplam+mat[i][j];
                padet=padet+1;
            }
        }
    }

    int ort= ptoplam/padet;
    printf("dizinin pozitif elemanlarinin ortalamasi %d", ort);


    return 0;
}
