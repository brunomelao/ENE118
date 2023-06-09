import socket
import cv2
import os
import numpy as np

class Cliente():
    """
    Classe Cliente - API Socket
    """
    def __init__(self, server_ip, port):
        """
        Construtor da classe Cliente
        """
        self.__server_ip = server_ip
        self.__port = port
    
    def start(self,caminho_imagem):
        """
        Método que inicializa a execução do Cliente
        """
        self.__tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        endpoint = (self.__server_ip,self.__port)
        try:
            self.__tcp.connect(endpoint)
            print("Conexão realizada com sucesso!")
            self.__method(caminho_imagem)
        except:
            print("Servidor não disponível")

    
    def __method(self, caminho_imagem):
        """
        Método que implementa as requisições do cliente
        """
        try:
             # leitura da imagem
             #caminho_imagem = 'faces/image_0001.jpg'
            img = cv2.imread(caminho_imagem)

            # codificação para bytes
            _, img_bytes = cv2.imencode('.jpg', img)
            img_bytes = bytes(img_bytes)
            tamanho_da_imagem_codificado = len(img_bytes).to_bytes(4, 'big')
            self.__tcp.send(tamanho_da_imagem_codificado)
            self.__tcp.send(img_bytes)
            tam_img = self.__tcp.recv(1024)
            tam = int.from_bytes(tam_img, 'big')
            cont = 1024
            img_rec = self.__tcp.recv(1024)

            while(cont<=tam):
                    img_rec += self.__tcp.recv(1024)
                    cont += 1024
            img2 = cv2.imdecode(np.frombuffer(img_rec, np.uint8), cv2.IMREAD_COLOR)
            cv2.imshow('Imagem Processada', img2)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            self.__tcp.close()
        except Exception as e:
            print("Erro ao realizar comunicação com o servidor", e.args)

 