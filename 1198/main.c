#include <stdio.h>

int main(void) {
  while (getchar() != EOF) {
    int i1 = 0;
    int i2 = 0;
    int diferenca = 0;
    scanf("%d",&i1);
		scanf("%d",&i2);
		
		printf("%d %d",i1,i2);
		
    diferenca = i2 - i1;
		
    if (diferenca < 0) {
      diferenca = diferenca * -1;
    }
    printf("%d", diferenca);
  }
  return 0;
}