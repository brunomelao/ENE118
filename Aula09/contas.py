class Conta():
    _saldo = 0.0
    def __init__(self, numero,titular, senha, saldoi=0.0):
        self.numero=numero
        self.titular=titular
        self.__senha=senha
        self._saldo=saldoi

    def getSaldo(self,senha):
        if senha==self.__senha:
            return self._saldo
    def setSaldo(self,valor):
        self._saldo=valor
    def setSenha(self,novaSenha):
        self.__senha=novaSenha
    def saque(self, senha, valor):
        if senha==self.__senha:
            if self._saldo>=valor:
                self._saldo-=valor
                print(f"Saque no valor de R$ {valor} realizado com sucesso")
            else:
                print("Saldo insuficiente")
        else:
            print("Senha inválida")
    def deposito(self, valor):
        if valor>0:
            self._saldo+=valor
        else:  
            print("Valor inválido")
        
        print(f"Depósito no valor de R$ {valor} realizado com sucesso")
    def exibeDados(self, senha):
        if senha==self.__senha:
            print(f"Número: {self.numero}")
            print(f"Titular: {self.titular}")
            print(f"Saldo: {self._saldo}")
        else:
            print("Senha inválida")
    def validaSenha(self,senha):
        return senha==self.__senha

class ContaPoupanca(Conta):
    def __init__(self, numero,titular, senha, saldoi=0.0, taxa=0.002):
        super().__init__(numero,titular, senha, saldoi)
        self.__taxa=taxa
    def simulaRendimento(self, meses):
        if meses>0:
            saldo_final=self._saldo*(1+self.__taxa)**meses
            print(f"Saldo após {meses} meses: R$ {saldo_final:.2f}")
        else:
            print("Quantidade de meses deve ser maior que zero")
        return self._saldo*(1+self.__taxa)**meses-self._saldo
    