#include <stdio.h>

int main(void) {
    int interations = 0;
	int soma = 0;
	int PA = 0 , PB = 0;
	float G1 = 0 , G2 = 0;
	int i = 0;

	scanf("%d",&interations);
	
	for(i=0;i<interations;i++){

		soma = 0;

		scanf("%d %d %f %f",&PA,&PB,&G1,&G2);
		
		while(1){		
			if(PA>PB){
					if(soma>100){
						printf("Mais de 1 seculo.");
						break;
					}
				printf("%d anos.",soma);
				break;
			}
			else{
				soma+=1;
				PA += (int) PA*(G1/100);
				PB += (int) PB*(G2/100);
			}
			
			
		
		}
	}
	return 0;
}