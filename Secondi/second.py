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
    

