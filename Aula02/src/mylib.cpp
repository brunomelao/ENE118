float potencia(float b, int exp) 
{
	float r = b;
	for(int i=1;i<exp;i++)
	{
		r *=b;
	}
	return r;
}
float fatorial(float num) 
{
	float fat=1;

	for(int cont=1;cont<num;cont++){
		fat=fat*(cont+1);
	}
	return fat;
}
float y(float x){
	float val;
	val=fatorial(5)*potencia(x,3)+fatorial(4)*potencia(x,2)+fatorial(3)*x+fatorial(2);
	return val;
}
