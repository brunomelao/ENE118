def soma(op1,op2):
    """
    Função que soma dois números
    :param op1: operando 1
    :param op2: operando 2
    :return: soma dos operandos
    """
    return op1+op2
def divisao(dividendo,divisor):
    """
    Função que divide dois números
    :param dividendo: dividendo
    :param divisor: divisor
    :return: quociente
    """
    return dividendo/divisor
lista=[x**2 for x in range(0,10)]
if __name__=="__main__": # Não executa quando importado
    import sys 
    if sys.argv[3]=="+":
        print(soma(float(sys.argv[1]),float(sys.argv[2])))
    elif sys.argv[3]=="/":
        print(divisao(float(sys.argv[1]),float(sys.argv[2])))
    else:
        print("Operação inválida")