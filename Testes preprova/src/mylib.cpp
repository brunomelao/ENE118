#include "mylib.h"
#include <iostream>
using namespace std;
int numNome(char* nome){
    int i=0;
    for(i=0; nome[i]!='\0';i++){
    }
    cout<<i;
    return i;
}

void inverteNome(char* nome){ 
    int tam=numNome(nome),i;
    char nomeInvertido[100];
    for(i =0;i<tam;i++){
        nomeInvertido[i]=nome[tam-i-1];
    }
    for(i =0;i<tam;i++){
        nome[i]=nomeInvertido[i];
    }
    nome[i]='\0';
    cout<<"Seu nome invertido e: "<<nomeInvertido<<endl;
}
