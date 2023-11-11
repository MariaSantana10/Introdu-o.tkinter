import requests
from tkinter import *
def começo():
    print('olá, vc esta conseguindo')
janela = Tk() #abrir janela

janela.title('Experimento')

informaçoes_janela= Label(janela, text = 'To aprendendo')
informaçoes_janela.grid(column=0,row=0)

botao=Button(janela, text = 'clique aqui', command=começo)
botao.grid(column=0,row=1)

janela.mainloop() #para fechar a janela (fica no final do codigo)