# ==================DESAFIO DO ChatGPT===========================



class Texto:
    def __init__(self, texto):
        self.texto = texto
        

    def especiais(self):
        contador = 0
        caracteres = ['.', ',', '!', '?', ':', ';']
        for caracter in caracteres:
            contador += self.texto.count(caracter)
        return contador
    
    def vogais(self):

        contador = 0
        vogais = ["a","e","i","o","u"]
        for vogal in vogais:
            contador += self.texto.count(vogal)    
        return contador
            
        
        

    def consoantes(self):
        contador = 0
        consoantes = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
        for consoante in consoantes:
            contador += self.texto.count(consoante)
        return contador



    def espacos(self):
        if " " in self.texto:
            contador = self.texto.count(' ')
            return contador


texto = Texto("Era uma vez uma casa muito engraçada, não tinha teto, não tinha nada.")

print(f"""
Temos:
      {texto.especiais()} caracteres especiais;
      {texto.vogais()} vogais;
      {texto.consoantes()} consoantes; 
      {texto.espacos()} espaços 
      """)






