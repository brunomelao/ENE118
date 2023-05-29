#Objetos imutáveis:
#nome(variável) | Objeto
a=3
b=a
b=4
print("Valor: ",a)
print("Identificador",id(a))
a+=3
print("Valor: ",a)
print("Identificador",id(a))

a="Informática"
print("Valor: ",a)
print("Identificador",id(a))

#Objetos mutáveis:
#nome(variável) | Objeto
a=[1,2,3]
b=a
b.append(4)
print("Valor: ",a)
print("Identificador",id(a))
print("Valor: ",b)
print("Identificador",id(b))

a.append(5)
print("Valor: ",b)

