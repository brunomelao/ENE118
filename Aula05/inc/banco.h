#ifndef BANCO_H
#define BANCO_H

#include "conta.h"
#define NUMCONTAS 100
class Banco
{
private:
    Conta* contas;
    int senhaGerente;
    int numContas;
public:
    Banco();
    ~Banco();
    Conta* buscaConta(int numero); 
    void atendimento();
    bool atendimentoCliente();
    bool atendimentoGerente();
    void cadastraConta(int senha, int numero, std::string titular, std::string tipo, double saldo);
    void removeConta(int numero);
    
};


#endif
