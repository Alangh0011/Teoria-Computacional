#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <unistd.h>

void main(){
	
	/*CREACION DE FICHEROS*/
	FILE *fichero;
    fichero = fopen("Cadenas.txt", "w+");
    if(fichero == NULL ) {
        printf("No fue posible abrir/crear el archivo\n");
        return;
   }
   FILE *fichero2;
    fichero2 = fopen("Validas.txt", "w+");
    if(fichero2 == NULL ) {
        printf("No fue posible abrir/crear el archivo\n");
        return;
   }
   FILE *fichero3;
    fichero3 = fopen("no_validas.txt", "w+");
    if(fichero3 == NULL ) {
        printf("No fue posible abrir/crear el archivo\n");
        return;
   }
	

    int j=0, n=0, i=0;
    char unos = 0;
    char ceros = 0;
    int numero[65];

	int generador = pow(10,6);
	

	for (i = 0;i < generador ; i++)
	{
    	printf("\nel numero binario es:");
		for (j = 0;j < 64 ; j++)
    	{
    		  numero[j] = rand() % 2;
    		  printf("%d",numero[j]);
    		  
			  fprintf(fichero,"%d",numero[j]);
             
			 if(numero[j] == 1){
         	unos++;
        	}else{
	   	     ceros++;
    	    }
	    }
	    fprintf(fichero,"\n");
	        /**/
	        	if(unos % 2 == 0){
	        		if(ceros % 2 == 0)
	        		{
	        	for (j = 0;j < 64 ; j++){
	        	fprintf(fichero2,"%d",numero[j]);	
				}
    	    	fprintf(fichero2,"\n");	
    	    }else{
    	    	for (j = 0;j < 64 ; j++){
	        	fprintf(fichero3,"%d",numero[j]);	
				}
    	    	fprintf(fichero3,"\n");	
			}
    	    /**/
			} else{
				for (j = 0;j < 64 ; j++){
	        	fprintf(fichero3,"%d",numero[j]);	
				}
    	    	fprintf(fichero3,"\n");	
			}
		    //usleep(10000);
			unos  = 0;
			ceros = 0;
	}
    
  

   return;


}
