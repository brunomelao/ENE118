from pymodbusTCP.client import Client
from time import sleep

class ClienteMODBUS():
    """
    Classe Cliente MODBUS
    """
    def __init__(self, server_ip,porta, scan_time):
        """
        Construtor da classe ClienteMODBUS
        """
        self._cliente = ModbusClient(host=server_ip, port=porta)
        self._scan_time = scan_time
    def atendimento(self):
        """
        Método que realiza o atendimento do cliente MODBUS
        """
        self._cliente.open()
        
        try:
            atendimento = True
            while atendimento:
                sel= input(f"Deseja realizar uma leitura,escrita ou configuração? (1- Leitura | 2- Escrita | 3- Configuração | 4- Sair): ")
                if sel == "1":
                    tipo= input(f"Qual tipo de dado deseja ler? (1- Holding Register | 2- Coil | 3- Input Register | 4- Discrete Input): ")
                    addr=input(f"Digite o endereço da tabela MODBUS: ")
                    nvezes = input("Digite o número de vezes que deseja ler: ")
                    for i in range(0,int(nvezes)):
                        print(f"Leitura {i+1}: {self.lerDado(int(tipo),int(addr))}")
                        sleep(self._scan_time) 
                elif sel == "2":
                    tipo= input(f"Qual tipo de dado deseja escrever? (1- Holding Register | 2- Coil): ")
                    addr=input(f"Digite o endereço da tabela MODBUS: ")
                    valor=input(f"Digite o dado que deseja escrever: ")
                    self.escreveDado(int(tipo),int(addr),int(valor))
                elif sel == "3":
                    scant=input(f"Digite o tempo de varredura desejado: ")
                    self._scan_time = float(scant)
                elif sel == "4":
                    self._cliente.close()
                    atendimento = False
                else:  
                    print("Seleção inválida!")
        except Exception as e:
            print(f"Erro: {e}")
            self._cliente.close()
    def lerDado(self, tipo,addr):
        """
        Método que realiza a leitura de um dado da tabela MODBUS
        """
        if tipo == 1:
            return self._cliente.read_holding_registers(addr,1)[0]
        
        if tipo == 2:
            return self._cliente.read_coils(addr,1)[0]
        if tipo == 3:
            return self._cliente.read_input_registers(addr,1)[0]
        if tipo == 4:
            return self._cliente.read_discrete_inputs(addr,1)[0]
    def escreveDado(self, tipo,addr,valor):
        """
        Método que realiza a escrita de um dado da tabela MODBUS
        """
        if tipo == 1:
            return self._cliente.write_holding_register(addr,valor)[0]
        
        if tipo == 2:
            return self._cliente.write_coils(addr,valor)[0]
    