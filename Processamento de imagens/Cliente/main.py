from cliente import Cliente

c = Cliente("127.0.0.1",9000)

#c = Cliente("192.168.43.216",9000)

caminho_imagem = 'faces/image_0004.jpg'

c.start(caminho_imagem)