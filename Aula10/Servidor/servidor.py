import socket

class Servidor():
    """
    Classe Servidor - Calculadora remota - API Socket
    """
    def __init__(self,host,port):
        """
        Construtor da classe Servidor
        """
        self._host = host
        self._port = port
        self.tcp= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        """
        Inicia o servidor
        """
        endpoint=(self._host,self._port)
        try:
            self.tcp.bind(endpoint)
            self.tcp.listen(1)
            print("Servidor foi iniciado em ", self._host,":",self._port)
            while True:
                con, client=self.tcp.accept()
                self._service(con,client)
        except Exception as e:
            print("Erro ao inicializar o servidor ",e.args)
    def _service(self,con,client):
        """
        Método que implementa o serviço da calculadora remota
        :param con: objeto socket utilizado para enviar e receber dados
        :param client: é o endereço e porta do cliente
        """
        print("Atendendo cliente ",client)
        operadores = ['+','-','*','/']
        while True:
            try:
                msg=con.recv(1024)
                msg_s=str(msg.decode('ascii')) #op1 operacao op2
                op='none'
                for x in operadores:
                    if msg_s.find(x)>0:
                        op=x
                        msg_s=msg_s.split(op) # ['15','10']
                        break
                if op == '+':
                    resp=float(msg_s[0])+float(msg_s[1])
                elif op == '-':
                    resp=float(msg_s[0])-float(msg_s[1])
                elif op == '*':
                    resp=float(msg_s[0])*float(msg_s[1])
                elif op == '/':
                    resp=float(msg_s[0])/float(msg_s[1])
                else:
                    resp= "Operacao invalida"
                con.send(bytes(str(resp),'ascii'))
                print(client,"-> requisição atendida")
            except OSError as e:
                print("Erro na conexão", client , ": ", e.args)
                return
            except Exception as e:
                print("Erros nos dados recebidos do cliente",client,": ",e.args)
                con.send(bytes('Erro','ascii'))