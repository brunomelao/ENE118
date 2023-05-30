import socket

class Cliente():
    """
    Classe Cliente - Calculadora Remota - API socket
    """
    def __init__(self, server_ip,port):
        """
        Construtor da classe Cliente
        :param server_ip: endereço IP do servidor
        :param port: porta do serviço
        """
        self._server_ip=server_ip
        self._port=port
        self.tcp=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def start(self):
        """
        Inicia o cliente
        """
        endpoint=(self._server_ip,self._port)
        try:
            self.tcp.connect(endpoint)
            print("Conexão realizada com sucesso")
            self.__method()
        except Exception as e:
            print("Erro na conexão com o servidor ",e.args)
    def __method(self):
        """
        Método que implementa as requisições do cliente e a IHM
        """
        try:
            msg=''
            while msg != 'x':
                msg=input("Digite a expressão (x para sair): ")
                if msg == '':
                    continue
                elif msg == 'x':
                    break
                self.tcp.send(bytes(msg,'ascii'))
                resp=self.tcp.recv(1024)
                print("=  ",resp.decode('ascii'))
            self.tcp.close()
        except Exception as e:
            print("Erro na conexão com o servidor. ",e.args)