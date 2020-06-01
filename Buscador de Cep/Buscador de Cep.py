from tkinter import *
from tkinter import ttk
import pycep_correios


class Product:
    def __init__(self, root):
        self.wind = root
        self.wind.title('Buscador de Endereço Pelo CEP')
        self.wind.geometry('300x150')
        self.wind.resizable(False, False)

        self.cep = Label(self.wind, text='CEP:').place(x=48, y=10)
        self.cep = ttk.Entry(self.wind)
        self.cep.bind('<Return>', self.enter)
        self.cep.place(x=80, y=10)

        self.enderecolabel = Label(self.wind, text='Endereço:')
        self.enderecolabel.place(x=18, y=35)
        self.endereco = Label(self.wind, text='')
        self.endereco.place(x=80, y=35)

        self.bairrolabel = Label(self.wind, text='Bairro:')
        self.bairrolabel.place(x=35, y=55)
        self.bairro = Label(self.wind, text='')
        self.bairro.place(x=80, y=55)

        self.cidadelabel = Label(self.wind, text='Cidade:')
        self.cidadelabel.place(x=30, y=75)
        self.cidade = Label(self.wind, text='')
        self.cidade.place(x=80, y=75)

        self.uflabel = Label(self.wind, text='UF:')
        self.uflabel.place(x=52, y=95)
        self.uf = Label(self.wind, text='')
        self.uf.place(x=80, y=95)

        self.status = Label(self.wind, text='Desenvolvido por Rafael Marciano', bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

    def enter(self, *args):
        end = pycep_correios.get_address_from_cep(self.cep.get())

        self.endereco['text'] = end['logradouro']
        self.bairro['text'] = end['bairro']
        self.cidade['text'] = end['cidade']
        self.uf['text'] = end['uf']


if __name__ == '__main__':
    root = Tk()
    application = Product(root)
    root.mainloop()