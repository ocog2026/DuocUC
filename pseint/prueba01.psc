Proceso prueba01
	Definir a,b,s,i,r Como Entero;
	Escribir "Escribir un valor A";
	Leer a;
	Escribir 'Escribir un valor B';
	Leer b;
	s = a + b;
	Escribir 'el resultado de la suma es = ', s;
	
	Si s > 0 Entonces
		Escribir "la suma es mayor que cero";
	SiNo
		Escribir "la suma es menor que cero";
	FinSi
	i = 1;r=1;
	Mientras i < s Hacer
		r = r * 2;
		i=i+1;
	FinMientras
	Escribir 'el resultado del ciclo es = ', r;
FinProceso
