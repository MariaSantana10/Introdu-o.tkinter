import requests
from tkinter import *
def começo():
    texto= 'olá, vc esta conseguindo'
    text_exibir['text']=texto

janela = Tk() #abrir janela

janela.title('Experimento')
janela.geometry('400x400')


informaçoes_janela= Label(janela, text = 'To aprendendo')
informaçoes_janela.grid(column=0,row=0,padx=10,pady=10)

botao=Button(janela, text = 'clique aqui', command=começo)
botao.grid(column=0,row=1,padx=10,pady=10)

text_exibir= Label(janela, text='')
text_exibir.grid(column=0,row=2,padx=10,pady=10)

janela.mainloop() #para fechar a janela (fica no final do codigo)