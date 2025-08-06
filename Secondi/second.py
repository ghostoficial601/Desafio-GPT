# Sistema de Gerenciamento de Biblioteca
# Crie um sistema para gerenciar uma biblioteca que permita:

import json
import os

if not os.path.exists('biblioteca.json'):
    with open('biblioteca.json', 'w', encoding='UTF-8') as f:
        json.dump([], f)


def salvar(caminho, arquivo):
    with open(caminho, 'w', encoding='UTF-8') as f:
        json.dump(arquivo,f, ensure_ascii=False, indent=4)

def carregar_dados(arquivo):
    with open(arquivo, 'r', encoding='UTF-8') as f:
        return json.load(f)
# ======================================================================


class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano 
        self.livro = {
            "nome": self.titulo,
            "autor": self.autor,
            "ano": self.ano,
            "disponivel": True
        }

    def adicionar_livro(self):
        arquivo = 'biblioteca.json'
        livros = carregar_dados(arquivo=arquivo)
        
        
        livros.append(self.livro)
        salvar(caminho=arquivo, arquivo=livros)
        return "Livro adicionado"
    
    
class Biblioteca:
    def __init__(self, verificacao):
        self.verificacao = verificacao
          
            
    


class Seguranca:
    def __init__(self, nome, email, senha):
        self.usuario = nome
        self.nome = nome
        self.email = email
        self.senha = senha

    def login(self):
        usuarios = carregar_dados(arquivo='dados.json')
        procurando = False
        for usuario in usuarios:
            if usuario["nome"] != nome and usuario["email"] != email and usuario["senha"] != senha:
                return False
            if usuario["nome"] == nome and usuario["email"] == email and usuario["senha"] == senha:
                procurando = True
                self.nome = nome
                self.email = email
                self.senha = senha
                return True
            
    def cadastro(self):
        usuarios = carregar_dados(arquivo='dados.json')
        usuario = {
                "nome": self.nome ,
                "email": self.email,
                "senha": self.senha
            }
        usuarios.append(usuario)
        salvar(caminho='dados.json', arquivo=usuarios)
        return "Cadastro feito com sucesso"

        
        
           
    


#  ========================= Interface ===========================================================


while True:
    pergunta = str.lower(input("Vc tem Cadastro em nossa biblioteca?"))
    if pergunta in ["sim" or "Sim" or "s"]:
        nome = str(input("Digite seu nome de cadastro: "))
        email = str(input("Digite seu email: "))
        senha = str(input("digite sua senha: "))
        usuario = Seguranca(nome,email,senha)
        if usuario:
            print("Entramos!!!")








    question = str.lower(input('''
vc gostaria de:
                         1. Ver livros
                         2. Adicionar livro
                         3. Reservar Livro
                         4. Devolver livro
                         0. Encerrar programa
->'''))
    if question in ['0' or 'encerrar' or 'encerrar programa']:
        break
        
    elif question in ['1' or 'ver' or 'ver livro']:
        print("teve umas mudanças, calma")


    elif question in ['2' or 'adiconar' or 'adicionar livro']:
        titulo = str(input("Nome do livro:\n-> "))
        auto = str(input("Auto do livro:\n-> "))
        ano = int(input("Ano do livro:\n-> "))
        meio = Livro(titulo,auto,ano)
        print(meio.adicionar_livro())
    
    
        
    


