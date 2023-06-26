import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.core.window import Window

class MyWidget(BoxLayout):
    op = ''
    valor=0
    def sete(self):
        if(self.ids.lb.text == "0"):
            self.ids.lb.text = "7"
        else:
            self.ids.lb.text = self.ids.lb.text + "7"
    def oito(self):
        if(self.ids.lb.text == "0"):
            self.ids.lb.text = "8"
        else:
            self.ids.lb.text = self.ids.lb.text + "8"
    def nove(self):
        if(self.ids.lb.text == "0"):
            self.ids.lb.text = "9"
        else:
            self.ids.lb.text = self.ids.lb.text + "9"
    def quatro(self):
        if(self.ids.lb.text == "0"):
            self.ids.lb.text = "4"
        else:
            self.ids.lb.text = self.ids.lb.text + "4"
    def cinco(self):
        if(self.ids.lb.text == "0"):
            self.ids.lb.text = "5"
        else:
            self.ids.lb.text = self.ids.lb.text + "5"
    def seis(self):
        if(self.ids.lb.text == "0"):
            self.ids.lb.text = "6"
        else:
            self.ids.lb.text = self.ids.lb.text + "6"
    def um(self):
        if(self.ids.lb.text == "0"):
            self.ids.lb.text = "1"
        else:
            self.ids.lb.text = self.ids.lb.text + "1"
    def dois(self):
        if(self.ids.lb.text == "0"):
            self.ids.lb.text = "2"
        else:
            self.ids.lb.text = self.ids.lb.text + "2"
    def tres(self):
        if(self.ids.lb.text == "0"):
            self.ids.lb.text = "3"
        else:
            self.ids.lb.text = self.ids.lb.text + "3"
    def zero(self):
        if(self.ids.lb.text == "0"):
            self.ids.lb.text = "0"
        else:
            self.ids.lb.text = self.ids.lb.text + "0"
    def soma(self):
        self.valor=float(self.ids.lb.text)
        self.op='+'
        self.ids.lb.text = ""
        
    def subtracao(self):
        self.valor=float(self.ids.lb.text)
        self.op='-'
        self.ids.lb.text = ""
    def multiplicacao(self):
        self.valor=float(self.ids.lb.text)
        self.op='*'
        self.ids.lb.text = ""
    def divisao(self):
        self.valor=float(self.ids.lb.text)
        self.op='/'
        self.ids.lb.text = ""
    def igual(self):
        if(self.op=='+'):
            self.ids.lb.text = str(self.valor+float(self.ids.lb.text))
        elif(self.op=='-'):
            self.ids.lb.text = str(self.valor-float(self.ids.lb.text))
        elif(self.op=='*'):
            self.ids.lb.text = str(self.valor*float(self.ids.lb.text))
        elif(self.op=='/'):
            self.ids.lb.text = str(self.valor/float(self.ids.lb.text))
        else:
            self.ids.lb.text = "0"
    def deletar(self):
        self.ids.lb.text = self.ids.lb.text[:-1]
    def c(self):
        self.ids.lb.text = "0"
    def ponto(self):
        self.ids.lb.text = self.ids.lb.text + "."
class BasicApp(App):
    def build(self):
        """
        Método para construção do aplicativo com base no widget criado
        """
        return MyWidget()
 
if __name__ == '__main__':
    Config.set('graphics','resizable',True)
    BasicApp().run()