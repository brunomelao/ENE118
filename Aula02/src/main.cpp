#include <iostream> //inclui biblioteca de entrada/saída de dados
#include "mylib.h"
#include <string>
using namespace std;//inclusão do espaço de nomes std
class C1{
	public:
		C1(){}
		C1(int arg){
			attr1 = arg;
		}
		void setAtributo(int valor){
			this->attr1=valor;
		}
		void getAtributo(){
			cout<<"Attr1:"<<attr1<<endl;
		}
	protected:
		int attr1;
};
class C2:public C1{
	public:
		C2(int arg){
			attr1 = arg;
		}
};


// int foo(int* a,int& b){
// 	int soma=*a+b;
// 	*a=16;
// 	// int* bptr=&b;
// 	// *bptr=70
// 	b=70;
// 	return soma;
// }
int main()
{
	// float a;
	// cin>>a;
	// cout<<"y(25) = "<< y(25)<<endl;
	// cout<<"y(7!) = "<< y(fatorial(7))<<endl;
	// cout<<"y(2.5^3) = "<< y(potencia(2.5,3))<<endl;
	// cout<<"y("<<a<<") = "<<y(a)<<endl;
	// int a=5;
	// int b=10;
	// int s=foo(&a,b);
	// cout<<"s:"<<s<<"\na:"<<a<<"\nb:"<<b<<endl;
	// int tam;
	// cout<<"Digite o tamanho do vetor:";
	// cin>>tam;
	// string* vetor=new string[tam];
	// for(int i=0;i<tam;i++){
	// 	vetor[i]="Bruno";
	// }
	// for(int i=0;i<tam;i++){
	// 	cout<<"Na posicao "<<i<<" a string e: "<<vetor[i]<<endl;
	// }
	// delete [] vetor;
	C1 instanciaC1(2);
	C2 instanciaC2(3);
	instanciaC1.getAtributo();
	instanciaC1.setAtributo(5);
	instanciaC1.getAtributo();
	instanciaC2.getAtributo();
	instanciaC2.setAtributo(5);
	instanciaC2.getAtributo();

	return 0;
}