import socket
import cv2
import os
import numpy as np


class Servidor():
    """
    Classe Servidor - API Socket
    """

    def __init__(self, host, port):
        """
        Construtor da classe servidor
        """
        self._host = host
        self._port = port

    def start(self):
        """
        Método que inicializa a execução do servidor
        """
        self.__tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #familia de endereços (faixa de clientes que podem se conectar ao servidor), parametro que permite escolher qual camada de transporte (TCP (socket.SOCK_STREAM), UDP(socket.SOCK_DGRAM))
        endpoint = (self._host, self._port) # união entre IP e porta (tupla, usa parênteses, tupla é imutável, logo não pode ser alterado)
        try: #caminho alternativo
            self.__tcp.bind(endpoint)
            self.__tcp.listen(1)
            print("Servidor iniciado em ", self._host, ": ", self._port)
            while True:
                con, client = self.__tcp.accept() # accept é um comando bloqueante
                self._service(con, client)
        except Exception as e: # caso geral
            print("Erro ao inicializar o servidor", e.args)

    def _service(self, con, client):
        """
        Método que implementa o serviço de processamento de imagens
        :param con: objeto socket utilizado para enviar e receber dados
        :param client: é o endereço do cliente
        """
        print("Atendendo cliente ", client)
        while True:
            try:
                tam_img = con.recv(1024)
                tam = int.from_bytes(tam_img, 'big')
                cont = 1024
                img_rec = con.recv(1024)

                while(cont<=tam):
                    img_rec += con.recv(1024)
                    cont += 1024
                img = cv2.imdecode(np.frombuffer(img_rec, np.uint8), cv2.IMREAD_COLOR)
                # processamento
                xml_classificador = os.path.join(os.path.relpath(
                   cv2.__file__).replace('__init__.py', ''), 'data\haarcascade_frontalface_default.xml')
                face_cascade = cv2.CascadeClassifier(
                   xml_classificador)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                
                # Desenha retângulos nas áreas onde as faces foram detectadas
                for (x, y, w, h) in faces:
                   cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                # codificação para bytes
                _, img_bytes = cv2.imencode('.jpg', img)
                img_bytes = bytes(img_bytes)
                tamanho_da_imagem_codificado = len(img_bytes).to_bytes(4, 'big')
                con.send(tamanho_da_imagem_codificado)
                con.send(img_bytes)
                print(client, " -> requisição atendida")

            except OSError as e:
                print("Erro de conexão ", client, ": ", e.args)
                return
            except Exception as e:
                print("Erro nos dados recebidos pelo cliente ",
                      client, ": ", e.args)
                con.send(bytes("Erro", 'ascii'))
                return
      
