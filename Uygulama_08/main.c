#include <stdio.h>
#include <stdlib.h>


int main()
{
  // Disaridan girilen MxN elemanli bir matristeki en buyuk elemani ve bu elemanin oldugu satir ve sutun adreslerini bulan program yaziniz.

  int m,n,i,j,mat[m][n];

  printf("Lutfen satir sayisini giriniz : \n");
  scanf("%d",&m);
  printf("Lutfen sutun sayisini giriniz : \n");
  scanf("%d",&n);


  for(i=0;i<m;i++){
    for(j=0;j<n;j++){
      printf("mat[%d][%d] :", i,j);
      scanf("%d",&mat[i][j]);
    }
  }

  int enb=mat[0][0];
  int sat=-1;
  int sut=-1;

  for(i=0;i<m;i++){
    for(j=0;j<n;j++){
      if(enb<mat[i][j]){
        enb=mat[i][j];
        sat=i;
        sut=j;
      }
    }
  }

  for(i=0;i<m;i++){
    for(j=0;j<n;j++){
      printf("%6d", mat[i][j]);
      printf("\n");
    }
  }

  printf("En buyuk sayi : %d", enb);
  printf("Bulundugu satir : %d", sat);
  printf("Bulundugu sut : %d", sut);


  return 0;
}
