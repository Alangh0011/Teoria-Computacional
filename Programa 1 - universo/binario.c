#include <stdio.h>
#include <math.h>


int decabin (int n,int cont) {
          
    if (n) {
    	 if((n%2)==1)
        	cont++;	
        cont = decabin(n / 2,cont);
        printf("%d", n % 2);
    }		
    return cont;
}

void main(){
	int var=0;
	do
	{
	
	/*CREACION DE FICHEROS*/
	FILE *fichero;
    fichero = fopen("cordenadas1.txt", "w+");
    if(fichero == NULL ) {
        printf("No fue posible abrir/crear el archivo\n");
        return;
   }
   FILE *fichero2;
   fichero2 = fopen("cordenadas2.txt", "w+");
    if(fichero == NULL ) {
        printf("No fue posible abrir/crear el archivo\n");
        return;
   }
	
	/*INSTANCIA DE VALORES Y OBTENCION DE DATOS*/
    int numero=0,j=0,n=0;
    char unos[100000];
    do{/*while que nos ayudara a validar valores fuera del parametro*/
    
    printf("Ingrese un entero si se ingresa 0 se dara un numero aleatorio: ");
    scanf("%d", &numero);
    
    }while(numero<0 || numero>1000);
	
    if( numero == 0){
		numero = rand() % 1000;
		printf("Numero aleatorio:%d\n",numero);
	}
	
	/*REALIZACION DEL DESARROLLO */
	int pt = pow(2,numero);
	
	printf("{0");
    for (j = 0;j < pt ; j++)
    {
    n = decabin(j,n);/*-----------> LLAMADA A LA FUNCION*/
    /*GUARDAMOS EN EL FICHERO*/
    fprintf(fichero,"%d       %d\n",j+1,n);
    fprintf(fichero2,"%d\n",n);

     printf(",");
     unos[j] = n;
     n=0;
    }
	printf("]\n");
	
	/*MOSTRAR DATOS*/
	
	printf("Numero de unos por numero:\n{");
	for (j = 0;j < pt ; j++){
		printf("%d,",unos[j]);
	}
	printf("}\n");
	
	/*VALIDACION SI SE INGRESARA OTRO NUMERO*/
	printf("\n\n ¿Se ingresara otra cadena? \nsi = presione 1 \nno = presione 0\n");
	scanf("%d",&var);
	system("cls");
	
}while(var==1);


}

