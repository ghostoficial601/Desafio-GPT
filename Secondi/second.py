# Sistema de Gerenciamento de Biblioteca
# Crie um sistema para gerenciar uma biblioteca que permita:

import json
import os

if not os.path.exists('biblioteca.json'):
    with open('biblioteca.json', 'w', encoding='UTF-8') as f:
        json.dump([], f)


def salvar(caminho, arquivo):
    with open(caminho, 'w', encoding='UTF-8') as f:
        json.dump(arquivo, ensure_ascii=False, indent=4)

def carregar_dados(arquivo):
    with open(arquivo, 'r', encoding='UTF-8') as f:
        return json.load(f)

class Livro:
    def __init__(self, titulo, autor, ano,disponivel):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano 
        self.disponivel = disponivel





def adicionar_livro():
    arquivo = 'biblioteca.json'
    livros = carregar_dados(arquivo=arquivo)
    nome = str(input("Nome do livro:\n-> "))
    auto = str(input("Auto do livro:\n-> "))
    ano = int(input("Ano do livro:\n-> "))
    livro = {
        "nome": nome,
        "autor": auto,
        "ano": ano,
        "disponivel": True
    }
    livros.append(livro)
    salvar(caminho=arquivo, arquivo=livros)
    return "Livro adicionado"

