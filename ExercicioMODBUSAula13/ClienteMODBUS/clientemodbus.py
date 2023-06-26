from pyModbusTCP.client import ModbusClient
from time import sleep
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.constants import Endian

class ClienteMODBUS():
    """
    Classe Cliente MODBUS
    """
    #lista_bits=[int(x) for x in '{0:016b}'.format(num)]
    
    def __init__(self, server_ip,porta,scan_time=1):
        """
        Construtor
        """
        self._cliente = ModbusClient(host=server_ip,port = porta)
        self._scan_time = scan_time

    def atendimento(self):
        """
        Método para atendimento do usuário
        """
        self._cliente.open()
        try:
            atendimento = True
            while atendimento:
                sel = input("Deseja realizar uma leitura, escrita ou configuração? (1- Leitura | 2- Escrita | 3- Configuração |4- Sair): ")
                
                if sel == '1':
                    tipo = input ("""Qual tipo de dado deseja ler? (1- Holding Register) |2- Coil |3- Input Register |4- Discrete Input| 5- Float|6- Holding Register com bit individual):""")
                    addr = input (f"Digite o endereço da tabela MODBUS: ")
                    nvezes = input ("Digite o número de vezes que deseja ler: ")
                    for i in range(0,int(nvezes)):
                        print(f"Leitura {i+1}: {self.lerDado(int(tipo), int(addr))}")
                        sleep(self._scan_time)
                elif sel =='2':
                    tipo = input ("""Qual tipo de dado deseja escrever? (1- Holding Register) |2- Coil|3- Float| 4- Holding register com bit individual) :""")
                    addr = input (f"Digite o endereço da tabela MODBUS: ")
                    valor = input (f"Digite o valor que deseja escrever: ")
                    self.escreveDado(int(tipo),int(addr),int(valor))

                elif sel=='3':
                    scant = input("Digite o tempo de varredura desejado [s]: ")
                    self._scan_time = float(scant)

                elif sel =='4':
                    self._cliente.close()
                    atendimento = False
                else:
                    print("Seleção inválida")
        except Exception as e:
            print('Erro no atendimento: ',e.args)

    def lerDado(self, tipo, addr):
        """
        Método para leitura de um dado da Tabela MODBUS
        """
        if tipo == 1:
            return self._cliente.read_holding_registers(addr,1)[0]

        if tipo == 2:
            return self._cliente.read_coils(addr,1)[0]

        if tipo == 3:
            return self._cliente.read_input_registers(addr,1)[0]

        if tipo == 4:
            return self._cliente.read_discrete_inputs(addr,1)[0]
        if tipo == 5:
            return self.lerFloat(addr)
        
        if tipo ==6:
            return self.lerMultplosBits(addr)
        
    def escreveDado(self, tipo, addr, valor):
        """
        Método para a escrita de dados na Tabela MODBUS
        """
        if tipo == 1:
            return self._cliente.write_single_register(addr,valor)

        if tipo == 2:
            return self._cliente.write_single_coil(addr,valor)
        if tipo == 3:
            return self.escreveFloat(addr,float(valor))
        
        if tipo == 4:
            return self.escreveMultiplosBits(addr,int(valor))
    
    def escreveFloat(self,addr,float):
        """
        Método para a escrita de um "float" na tabela MODBUS
        """
        builder = BinaryPayloadBuilder()
        builder.add_32bit_float(float)
        payload = builder.to_registers()
        return self._cliente.write_multiple_registers(addr,payload)
    
    def lerFloat(self,addr):
        """
        Método para a leitura de um "float" na tabela MODBUS
        """
        result = self._cliente.read_holding_registers(addr,2)
        decoder = BinaryPayloadDecoder.fromRegisters(result, byteorder=Endian.Big, wordorder=Endian.Little)
        decoded = decoder.decode_32bit_float()
        return decoded
    
    def lerMultplosBits(self,addr):
        """
        Método para leitura de um registrador como um conjunto de bits
        """
        result = self._cliente.read_holding_registers(addr,1)
        print(result)
        # decoder = BinaryPayloadDecoder.fromRegisters(result)
        # decoded = decoder.decode_bits()
        # return decoded
        list_bits = [int(x) for x in '{0:016b}'.format(result[0])]
        print(self.converteListaInt(list_bits))
        return list_bits
    
    def escreveMultiplosBits(self,addr,valor):
        """
        Método para escrita de um bit no registrador
        """
        list = self.lerMultplosBits(addr)
        bit = int(input("Digite o bit que deseja alterar: "))
        list[bit] = valor
        val = self.converteListaInt(list)
        self._cliente.write_single_register(addr,int(val))
        

    def converteListaInt(self,lista):
        """
        Método para converter a lista em inteiro
        """    
        cont=15
        res = 0
        for x in range(0,15):
            res = res + lista[x]*2**cont
            cont = cont - 1
        return res