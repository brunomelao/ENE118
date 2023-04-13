#ifndef BANCO_H
#define BANCO_H

#include "conta.h"
// Adiciona Conta =  Cria um vetor dinamico maior copia dado anterior, deleta o antigo e adiciona o novo 
#define NUMCONTAS 100 //Define que a palavar NUMCONTAS passa a valer como escrever 100
class Banco
{
private:
    Conta* contas;
    int senhaGerente;
    int numContas;
public:
    Banco();
    ~Banco();
    Conta* buscaConta(int numero); //Metodo que retorna o endereço do objeto conta que possui o mesmo numero informado
    void atendimento();
    bool atendimentoCliente();
    bool atendimentoGerente();
    void cadastraConta(int senha, int numero, std::string titular, std::string tipo, double saldo);
    void removeConta(int numero);
    
};


#endif
