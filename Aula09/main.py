import numpy as np
from matplotlib import pyplot as plt
"""
f=60 # frequencia 

t=1/f
A=220*np.sqrt(2)
t=np.arange(0,2*t,t/200)
y=A*np.sin(2*np.pi*f*t)

plt.title("Demonstração Matplotlib")
plt.xlabel("Tempo (s)")
plt.ylabel("Tensão (V)")
plt.plot(t,y)
plt.show()
"""
 #listas

lista=[1,2,"Bruno",4,5,6,7,8,9,10]
for x in lista:
    print(x)
lista.append("Melão")
lista[0]=55

for x in range(0,len(lista)):
    if(x==2):
        continue
print(lista[x])
dicionario={"nome":"Bruno","idade":21,"sexo":"M"} 

tupla=(1,2,3,4,5,6,7,8,9,10)

print(tupla[0])
# Diferença entre tupla e lista é que a tupla é imutavel

pilha=[]
for i in range(0,10):
    pilha.append(i)
for i in range(0,10):
    print(pilha.pop(), end=" ")
# Pilha é uma estrutura de dados que segue o conceito de LIFO (Last In First Out), ou seja, o último elemento a entrar é o primeiro a sair.

from collections import deque
fila=deque()
for i in range(0,10):
    fila.append(i)
for i in range(0,10):
    print(fila.popleft(), end=" ")
# Fila é uma estrutura de dados que segue o conceito de FIFO (First In First Out), ou seja, o primeiro elemento a entrar é o primeiro a sair. 