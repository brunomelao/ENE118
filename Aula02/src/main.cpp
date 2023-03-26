#include <iostream> //inclui biblioteca de entrada/saída de dados
#include "mylib.h"
using namespace std;//inclusão do espaço de nomes std

int main()
{
	float a;
	cin>>a;
	cout<<"y(25) = "<< y(25)<<endl;
	cout<<"y(7!) = "<< y(fatorial(7))<<endl;
	cout<<"y(2.5^3) = "<< y(potencia(2.5,3))<<endl;
	cout<<"y("<<a<<") = "<<y(a)<<endl;
	return 0;
}