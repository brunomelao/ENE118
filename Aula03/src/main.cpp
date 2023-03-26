#include <iostream>
#include <iomanip>
#include "mylib.h"
using namespace std;

#define TAMVET 5 //define que a palavra "TAMVET" é equivalente a 5

int main()
{
	
	int var = 10;

	//Passagem por valor
	cout<<"Valor de var: "<<var<<endl;//Imprime 10	
	passagemValor(var);//Não altera a variavel
	cout<<"Valor de var: "<<var<<endl; //Imprime 10
	
	//Passagem por ponteiro
	cout << "Valor de var: " << var << endl;//Imprime 10
	passagemPonteiro(&var);//Altera a variavel
	cout << "Valor de var: " << var << endl;//Imprime 11

	//Passagem por referência
	cout << "Valor de var: " << var << endl;//Imprime 10
	passagemReferencia(var);//Altera a variavel
	cout << "Valor de var: " << var << endl;//Imprime 11
	return 0;
}

