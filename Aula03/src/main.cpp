#include <iostream>
#include <iomanip>
#include "mylib.h"

using namespace std;

int main()
{
	char nome[100];
	cout<<"Digite seu nome: ";
	cin>>nome;
	inverteNome(nome);
	cout<<"Seu nome invertido e: "<<nome;
}

