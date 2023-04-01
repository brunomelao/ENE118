#include "banco.h"
#include <iostream>
#include <string>
using namespace std;

Banco::Banco() //O construtor criara 4 contas
{
    this->contas[0] = Conta(1234, 1, "Joao", "Corrente", 300);
    this->contas[1] = {4567, 2, "Jose", "Poupanca", 800};
    this->contas[2] = {7890, 3, "Maria", "Corrente", 1000};
    this->contas[3] = {8956, 4, "Madalena", "Poupanca", 2000};
    this->senhaGerente = 4545;
    this->numContas = 4;
}

Banco::~Banco()
{
}

Conta *Banco::buscaConta(int numero)//Retorna o endereço da conta que possuir o mesmo numero informado
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
bool Banco::atendimentoCliente() //Realiza o atendimento ao cliente(Função chamada na main)
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

    contaCliente = this->buscaConta(numC); //Chama o Metodo buscaConta() do banco para achar o objeto conta que possui o numero numC

    if (contaCliente == nullptr)//Se não achar nenhuma conta que corresponda entra nesse if
    {
        cout << "Conta invalida" << endl;
    }
    else
    {
        cout << "Digite a sua senha: ";
        cin >> senhain;

        if (contaCliente->validaSenha(senhain))
        {
            cout << "Ola " << contaCliente->titular <<","<< endl;
            while (atendimento) //Realiza o atendimento
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
            cout << "Senha invalida" << endl;
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
    cout<<"Digite a senha:";
    cin>>senhaGer;
    if(this->senhaGerente == senhaGer){
        int op;
        cout<<"Qual operacao deseja fazer? (1 - Cadastrar conta, 2 - Sair): ";
        cin>>op;
        switch(op){
            case 1:
                
                cout<<"Digite a senha, titular, tipo e saldo da conta que deseja cadastrar: ";
                cin>>senha>>titular>>tipo>>saldo;
                 this->CadastraConta(senha,this->numContas+1,titular,tipo,saldo);
                 atendimento=false;
            break;

            case 2: atendimento=false;
            break;
        }
        
    }
    else{
        cout<<"Senha invalida"<<std::endl;
    }
    return atendimento;
}

void Banco::CadastraConta(int senha, int numero, std::string titular, std::string tipo, double saldo){  
    this->contas[this->numContas] = {senha, numero, titular, tipo, saldo};
    cout<<"Conta cadastrada com sucesso"<<endl;
    this->numContas++;
}
