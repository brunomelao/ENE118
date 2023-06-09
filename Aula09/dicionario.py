dicionario={"P0000":{"Acesso aos parâmetros":"0 a 9000"},"P0001":{"Referência Velocidade":"0 a 65535"},"P0002":{"Velocidade de saída(motor)":"0 a 65535"},"P0003":{"Corrente do motor":"0.0 a 200.0 A"}}

for key,value in dicionario.items():
    print(key,":")
    for key2, value2 in value.items():
        print(key2,":",value2)