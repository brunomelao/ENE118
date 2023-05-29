from contas import Conta, ContaPoupanca
class Banco():
    """
    Classe para representação de um banco
    """
    def __init__(self):
        self.__contasBanco=[]
        self.__numeroContas=0
        self.__numeroContasPoupanca=0
        self.__senhaGerente=4545
        self.cadastraConta(1, "Joao",1234 , "Corrente", 300)
        self.cadastraConta( 2, "Jose",4567, "Poupanca", 800)
        self.cadastraConta( 3, "Maria", 7890,"Corrente", 1000)
        self.cadastraConta(4, "Madalena",8956,  "Poupanca", 2000)
    def cadastraConta(self, numero,titular,senha,tipo,saldoi):
        """
        Método para adição de uma conta ao banco
        :param Conta: objeto da classe Conta
        """
        for conta in self.__contasBanco:
            if conta.numero==numero:
                print("Conta ja existente")
                return
        if tipo =="Poupança" or tipo=="poupança" or tipo=="Poupanca" or tipo=="poupanca":
            novaConta=ContaPoupanca(int(numero),titular,int(senha),int(saldoi))
            self.__numeroContasPoupanca+=1
        else:
            novaConta=Conta(int(numero),titular,int(senha),int(saldoi))
            self.__numeroContas+=1
        self.__contasBanco.append(novaConta)
        print("Conta cadastrada com sucesso")
    def removeConta(self, numero):
        """
        Método para remoção de uma conta do banco
        :param numero: número da conta
        """
        for conta in self.__contasBanco:
            if conta.numero==numero:
                self.__contasBanco.remove(conta)
                if isinstance(conta, ContaPoupanca):
                    self.__numeroContasPoupanca-=1
                else:
                    self.__numeroContas-=1
                break
    def transfere(self, senha, numCdest, valor,numCAtual):
        """
        Método para transferência entre contas
        :param senha: senha da conta
        :param numCdest: número da conta destino
        :param valor: valor da transferência
        """
        
        for conta in self.__contasBanco:
            if conta.numero==numCAtual:
                conta.saque(senha,valor)
            if conta.numero==numCdest:
                conta.deposito(valor)
                break
    def atendimento(self):
        """
        Método para atendimento ao cliente
        """
        print("Bem-vindo ao sistema de atendimento do banco")
        opcao=input("Voce e um cliente ou gerente (0 - Cliente, 1 - gerente, 2 - Sair):")
        while(opcao!="2"):
            if opcao=="0":
                self.atendimentoCliente()
            elif opcao=="1":
                self.atendimentoGerente()
            opcao=input("Voce e um cliente ou gerente (0 - Cliente, 1 - gerente, 2 - Sair):")
        print("Obrigado por utilizar o banco!")
    def atendimentoCliente(self):
        numC=input("Digite o numero da sua conta:")
        for conta in self.__contasBanco:
            if conta.numero == int(numC):
                senha=input("Digite sua senha:")
                if(conta.validaSenha(int(senha))):
                    print(f"Olá {conta.titular}, escolha a operacao desejada:")
                    print("1 - Saque")
                    print("2 - Deposito")
                    print("3 - Exibir dados")
                    print("4 - Transferencia")
                    print("5 - Sair")
                    opcao=input("Digite a opcao desejada:")
                    while(int(opcao) != 5):
                        if int(opcao)==1:
                            valor=input("Digite o valor do saque:")
                            conta.saque(int(senha),float(valor))
                        elif int(opcao)==2:
                            valor=input("Digite o valor do deposito:")
                            conta.deposito(float(valor))
                        elif int(opcao)==3:
                            conta.exibeDados(int(senha))
                        elif int(opcao)==4:
                            numCdest=input("Digite o numero da conta destino:")
                            valor=input("Digite o valor da transferencia:")
                            self.transfere(int(senha),int(numCdest),float(valor),int(numC))
                        print("Deseja realizar outra operacao:")
                        print("1 - Saque")
                        print("2 - Deposito")
                        print("3 - Exibir dados")
                        print("4 - Transferencia")
                        print("5 - Sair")
                        opcao=input("Digite a opcao desejada:")
                    break

                else:
                    print("Senha invalida")
                    break
    def atendimentoGerente(self):
        senha=input("Digite a senha do gerente:")
        if int(senha)==self.__senhaGerente:
            print("Olá gerente, escolha a operacao desejada:")
            print("1 - Cadastrar conta")
            print("2 - Remover conta")
            print("3 - Exibir numero de contas")
            print("4 - Mudar senha do gerente")
            print("5 - Sair")
            opcao=input("Digite a opcao desejada:")
            while int(opcao) != 5:
                if int(opcao)==1:
                    numero=input("Digite o numero da conta:")
                    titular=input("Digite o nome do titular:")
                    senha=input("Digite a senha da conta:")
                    tipo=input("Digite o tipo da conta:")
                    saldo=input("Digite o saldo inicial:")
                    self.cadastraConta(int(numero),titular,int(senha),tipo,int(saldo))
                elif int(opcao)==2:
                    numero=input("Digite o numero da conta:")
                    self.removeConta(int(numero))
                elif int(opcao)==3:
                    print(f"Numero de contas: {self.__numeroContas}")
                    print(f"Numero de contas poupanca: {self.__numeroContasPoupanca}")
                elif int(opcao)==4:
                    senha=input("Digite a nova senha do gerente:")
                    self.mudaSenhaGer(int(senha))
                print("Deseja realizar outra operacao:")
                print("1 - Cadastrar conta")
                print("2 - Remover conta")
                print("3 - Exibir numero de contas")
                print("4 - Mudar senha do gerente")
                print("5 - Sair")
                opcao=input("Digite a opcao desejada:")
        else:
            print("Senha invalida")
    def mudaSenhaGer(self, senha):
        """
        Método para mudança da senha do gerente
        :param senha: senha atual
        """
        self.__senhaGerente=senha
    
    