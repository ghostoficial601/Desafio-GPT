# Sistema de Gerenciamento de Biblioteca
# Crie um sistema para gerenciar uma biblioteca que permita:

import json
import os

if not os.path.exists('biblioteca.json'):
    with open('biblioteca.json', 'w', encoding='UTF-8') as f:
        json.dump([], f)


if not os.path.exists('dados.json'):
    with open('dados.json', 'w', encoding='UTF-8') as f:
        json.dump([],f)  


def salvar(caminho, dados):
    with open(caminho, 'w', encoding='UTF-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def carregar_dados(caminho):
    with open(caminho, 'r', encoding='UTF-8') as f:
        return json.load(f)
# ======================================================================

class Seguranca:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def login(self):
        caminhoo = 'dados.json'
        usuarios = carregar_dados(caminho=caminhoo)
        procurando = False
        for usuario in usuarios:
            if usuario["nome"] == self.nome and usuario["email"] == self.email and usuario["senha"] == self.senha:

                return True, "acesso concedido"
            
            elif usuario["nome"] != self.nome and usuario["email"] != self.email and usuario["senha"] != self.senha:
                print("\nInválido!!\n")
                for i in range(2):
                    nome = str(input("Digite seu nome de cadastro: "))
                    email = str(input("Digite seu email: "))
                    senha = str(input("digite sua senha: "))
                    if usuario["nome"] != nome and usuario["email"] != email and usuario["senha"] != senha:
                        print("Inválido!!")
                    if usuario["nome"] == nome and usuario["email"] == email and usuario["senha"] == senha:
                        return True, "acesso concedido"
            elif not procurando:
                return False,"\n-- Acesso Negado --\n"
            
            
    def cadastro(self):
        arquivo = 'dados.json'
        usuarios = carregar_dados(caminho='dados.json')
        usuario = {
                "nome": self.nome ,
                "email": self.email,
                "senha": self.senha
            }
        usuarios.append(usuario)
        salvar(caminho=arquivo, dados=usuarios)
        return "Cadastro feito com sucesso"




















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
        livros = carregar_dados(caminho=arquivo)
        
        
        livros.append(self.livro)
        salvar(caminho=arquivo, dados=livros)
        return "Livro adicionado"
    
    
class Biblioteca:
    def __init__(self, verificacao):
        self.verificacao = verificacao
          
            
    




     
        
           
    


#  ========================= Interface ===========================================================


while True:
    aprovacao = False
    pergunta = str.lower(input('''
vc gostaria de:
                               1. Cadastro
                               2. Login
                --> '''))
    if pergunta in ["1" or "cadastro"]:
        nome = str(input("Digite seu nome de cadastro: "))
        email = str(input("Digite seu email: "))
        senha = str(input("digite sua senha: "))
        cadastro = Seguranca(nome,email,senha)
        print(cadastro.cadastro())
    if pergunta in ["2", "login"]:
        nome = str(input("Digite seu nome de cadastro: "))
        email = str(input("Digite seu email: "))
        senha = str(input("digite sua senha: "))
        tentativa = Seguranca(nome,email,senha)
        aprovacao = tentativa.login()
        if aprovacao:
            while True:
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
            
        
    if not aprovacao:
        print("Acesso Negado")
        break





    
    
    
        
    


