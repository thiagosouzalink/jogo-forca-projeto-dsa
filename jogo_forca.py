"""
Jogo da Força
"""
from  random import choice


board = ['''

>>>>>>>>>>Hangman<<<<<<<<<< 

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========''']

class JogoDaForca:

    def __init__(self, palavra):
        self.palavra = palavra
        self.total_tentativas = len(board)
        self.tentativas = 1
        self.letras_certas = []
        self.letras_erradas = []

    # Recebe letra digitada no jogo
    def receber_letra(self, letra):
        letra = letra.lower()
        if letra in self.letras_certas or letra in self.letras_erradas:
            print("\nVocê já digitou essa letra\n")
        elif letra in self.palavra:
            self.letras_certas.append(letra)
        else:
            self.letras_erradas.append(letra)
            self.tentativas += 1

    # Esconder letras não acertadas
    def esconder_letras(self):
        palavra_secreta = ''
        for letra in self.palavra:
            if letra in self.letras_certas:
                palavra_secreta += letra
            else:
                palavra_secreta += '_'
        return palavra_secreta

    # Verifica se o jogo encerrou
    def verificar_fim_jogo(self):
        if not self.verficar_jogador_venceu() and self.tentativas < self.total_tentativas:
            return False
        return True

    # Verifica se o jogador venceu ou perdeu
    def verficar_jogador_venceu(self):
        if self.esconder_letras() == self.palavra:
            return True
        else:
            return False

    def executar_jogo(self):
        print(board[self.tentativas-1])
        if not self.verificar_fim_jogo():
            print(f"\nNúmero de tentativa = {self.tentativas}")
            print(f"\nPalavra secreta: {self.esconder_letras()}\n")
            print("Letra(s) correta(s): ", end='')
            for letra in self.letras_certas:
                print(f"{letra} ", end="")
            print("\nLetra(s) erradas(s): ", end='')
            for letra in self.letras_erradas:
                print(f"{letra} ", end="")
            print("\n\n")
            return True
        return False


# Carrega palavra do arquivo       
def buscar_palavra(nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            palavras = arquivo.readlines()
            palavra = choice(palavras).strip()
        return palavra



arquivo = 'palavras.txt'
palavra_secreta = buscar_palavra(arquivo)
jogo = JogoDaForca(palavra_secreta)

# Executa o jogo
while jogo.executar_jogo():
    letra = input("Digite uma letra: ").strip()
    jogo.receber_letra(letra)

# Verifica status final
if jogo.verficar_jogador_venceu():
    print("\nParabéns!\nJogador venceu")
else:
    print("\nDeu ruim!\nJogador perdeu")
print(f"Palavra secreta: {jogo.palavra}\n")
