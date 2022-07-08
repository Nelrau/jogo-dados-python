import random

class Dado: #cria o objeto
  def __init__(self): #função que inicia o objeto
    self.inicio = 1
    self.fim = 6
    self.mensagem ='Quer jogar?'

  def iniciar(self): # inicia o evento jogar o dado
    resposta = input(self.mensagem)
    if resposta == 'sim'or resposta == 's':
      print(random.randint(self.inicio,self.fim))
      dado.iniciar()
    elif resposta == 'nao' or resposta == 'não' or resposta == 'n':
      print('Obrigado')
    else:
      print('tente sim ou não')
      dado.iniciar()
    
dado = Dado()# instancia
dado.iniciar()
