from contas import Conta, ContaPoupanca

c1=Conta(1,"João","1234",1000)
c1.deposito(100)
c1.saque("1234",200)
c1.exibeDados("1234")

# Utilizando a classe ContaPoupanca
cp=ContaPoupanca(2,"Maria","4321",1200)
cp.exibeDados("4321")
cp.simulaRendimento(12)