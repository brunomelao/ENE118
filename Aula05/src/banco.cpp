#include "banco.h"
#include <iostream>
#include <string>
using namespace std;
// Adicionar conta depois que remove uma conta está com erro

Banco::Banco()
{   
    this->senhaGerente = 4545;
    this->numContas = 0;
    this->numContasGlobal=0;
    cadastraConta(1234, 1, "Joao", "Corrente", 300);
    cadastraConta(4567, 2, "Jose", "Poupanca", 800);
    cadastraConta(7890, 3, "Maria", "Corrente", 1000);
    cadastraConta(8956, 4, "Madalena", "Poupanca", 2000);

}

Banco::~Banco()
{
    delete[] this->contas;
}

Conta *Banco::buscaConta(int numero)
{
    for (int i = 0; i < this->numContas; i++)
    {
        if (numero == this->contas[i].numero)
        {
            return &this->contas[i];
        }
    }

    return nullptr;
}
void Banco::atendimento(){
    int pessoa;
    bool saida=false;
    while(!saida){
    cout << "Bem vindo ao sistema de atendimento do banco" << endl;
    cout <<"Voce e um cliente ou gerente (0 - cliente, 1 - gerente, 2 - Sair)"<<endl;
    cin>> pessoa;
    switch(pessoa){
        case 0: saida=this->atendimentoCliente();
        break;
        case 1: saida=this->atendimentoGerente();
        break;
        case 2:
            saida=true;
            break;
    }
    }

}
bool Banco::atendimentoCliente()
{
    Conta *contaCliente;
    Conta *contaTransfer;
    int numC = 0;
    int senhain;
    int senha=0;
    bool atendimento = true;
    int numContaTransferir;

    cout << "Digite o numero da sua conta: ";
    cin >> numC;

    contaCliente = this->buscaConta(numC);
    if (contaCliente == nullptr)
    {
        cout << "Conta invalida" << endl;
        return false;
    }
    else
    {
        cout << "Digite a sua senha: ";
        cin >> senhain;

        if (contaCliente->validaSenha(senhain))
        {
            cout << "Ola " << contaCliente->titular <<","<< endl;
            while (atendimento)
            {
                int op;
                double valor;
                cout << "Qual operacao deseja fazer? (1 - Saque, 2 - Deposito, 3 - Ver Saldo, 4- Transferencia, 5 - Sair): ";
                cin >> op;
                switch (op)
                {
                case 1:
                    cout << "Digite o valor: ";
                    cin>>valor;
                    contaCliente->saque(senhain,valor);
                    break;
                case 2:
                    cout << "Digite o valor: ";
                    cin>>valor;
                    contaCliente->deposito(valor);
                    break;
                case 3:
                    cout << "Saldo: R$"<<contaCliente->getSaldo(senhain)<<endl;
                    break;

                case 4:
                    cout << "Digite o valor da transferencia e o numero da conta que quer transferir:";
                    cin>>valor;
                    cin>>numContaTransferir;
                    contaTransfer = this->buscaConta(numContaTransferir);
                    if(contaTransfer==nullptr){
                        cout<<"Conta Invalida"<<endl;
                    }
                    else{
                        contaCliente->transferir(valor,senhain,contaTransfer);
                    }
                    break;
                case 5:
                    atendimento = false;
                    break;
                }
            }
        }
        else
        {
            cout << "Senha invalida." << endl;
        }
    }
    return atendimento;
}
bool Banco::atendimentoGerente(){
    int senhaGer;
    bool atendimento=true;
    int senha;
    string titular,tipo;
    double saldo;
    int contaRemove;
    cout<<"Digite a senha:";
    cin>>senhaGer;
    if(this->senhaGerente == senhaGer){
        int op;
        cout<<"Qual operacao deseja fazer? (1 - Cadastrar conta, 2 - Remover conta, 3 - Sair): ";
        cin>>op;
        switch(op){
            case 1:
                
                cout<<"Digite a senha, titular, tipo e saldo da conta que deseja cadastrar: ";
                cin>>senha>>titular>>tipo>>saldo;
                 this->cadastraConta(senha,this->numContasGlobal+1,titular,tipo,saldo);
                 atendimento=false;
            break;
            case 2: 
                cout<<"Digite o numero da conta que deseja remover:";
                cin>>contaRemove;
                if(buscaConta(contaRemove)==nullptr){
                    cout<<"Conta Invalida"<<endl;
                    atendimento=false;
                }
                else{
                    removeConta(contaRemove);
                    atendimento=false;
                }
            break;
            case 3: atendimento=false;
            break;
        }
        
    }
    else{
        cout<<"Senha invalida"<<std::endl;
    }
    return atendimento;
}

void Banco::cadastraConta(int senha, int numero, std::string titular, std::string tipo, double saldo){  
    Conta *novaConta= new Conta[(this->numContas)+1];
    int i;
    for(i=0;i<this->numContas;i++){
        novaConta[i]=this->contas[i];
    }
    novaConta[i]={senha,numero,titular,tipo, saldo};
    if(numContas>0){
        delete [] contas;
    }
    this->numContas++;
    this->numContasGlobal++;
    this->contas= novaConta;
    cout<<"adicionou, numcontas:"<<this->numContas<<endl;
}

void Banco::removeConta(int numero){
    Conta *contaRemovida = new Conta[this->numContas-1];
    int cont=0;
    for(int i=0;i<this->numContas ;i++){
        if(i==(numero-1))continue;
        contaRemovida[cont]=this->contas[i];
        cont++;
    }
    delete [] contas;
    this->numContas--;
    this->contas=contaRemovida;
    cout<<"removeu, numcontas:"<<this->numContas<<endl;

}
