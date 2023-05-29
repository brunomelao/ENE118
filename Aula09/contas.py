class Conta():
    """
    Classe Conta
    """
    _saldo = 0.0
    def __init__(self, numero,titular, senha, saldoi=0.0):
        """
        Construtor da classe
        :param numero: número da conta
        :param titular: nome do titular
        :param senha: senha da conta
        :param saldoi: saldo inicial da conta (padrão = 0.0)
        """
        self.numero=numero
        self.titular=titular
        self.__senha=senha
        self._saldo=saldoi

    def getSaldo(self,senha):
        """
        Método para obtenção do saldo da conta
        :param senha: senha da conta
        :return: saldo da conta
        """
        if senha==self.__senha:
            return self._saldo
    def setSaldo(self,valor):
        """
        Método para configuração do saldo
        :param valor: valor desejado para o saldo
        """
        self._saldo=valor
    def setSenha(self,novaSenha):
        """
        Método para configuração da senha
        :param novaSenha: nova senha desejada
        """
        self.__senha=novaSenha
    def saque(self, senha, valor):
        """
        Método para saque na conta
        :param senha: senha da conta
        :param valor: valor do saque
        """
        if senha==self.__senha:
            if self._saldo>=valor:
                self._saldo-=valor
                print(f"Saque no valor de R$ {valor} realizado com sucesso")
            else:
                print("Saldo insuficiente")
        else:
            print("Senha inválida")
    def deposito(self, valor):
        """
        Método para depósito na conta
        :param valor: valor do depósito
        """
        if valor>0:
            self._saldo+=valor
        else:  
            print("Valor inválido")
        
        print(f"Depósito no valor de R$ {valor} realizado com sucesso")
    def exibeDados(self, senha):
        """
        Método para exibição dos dados da conta
        :param senha: senha da conta
        """
        if senha==self.__senha:
            print(f"Número: {self.numero}")
            print(f"Titular: {self.titular}")
            print(f"Saldo: {self._saldo}")
        else:
            print("Senha inválida")
    def validaSenha(self,senha):
        """
        Método para validação da senha
        :param senha: senha da conta
        """
        return senha==self.__senha

class ContaPoupanca(Conta):
    """
    Classe ContaPoupanca
    """
    def __init__(self, numero,titular, senha, saldoi=0.0, taxa=0.002):
        """
        Construtor da classe
        :param numero: número da conta
        :param titular: nome do titular
        :param senha: senha da conta
        :param saldoi: saldo inicial da conta (padrão = 0.0)
        :param taxa: taxa de rendimento mensal (padrão = 0.002)
        """
        super().__init__(numero,titular, senha, saldoi)
        self.__taxa=taxa
    def simulaRendimento(self, meses):
        """
        Método para simulação de rendimento do saldo em um determinado número de meses	
        :param meses: quantidade de meses para simulação
        """
        if meses>0:
            saldo_final=self._saldo*(1+self.__taxa)**meses
            print(f"Saldo após {meses} meses: R$ {saldo_final:.2f}")
        else:
            print("Quantidade de meses deve ser maior que zero")
        return self._saldo*(1+self.__taxa)**meses-self._saldo
    