import random
caveira = '''
███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████
'''
winner = '''
'''🏆🏅🥇🎖🏁
def criar_quadro(tamanho, minas):
quadro = [[" " for _ in range(tamanho)] for _ in range(tamanho)]
contar = 0
while contar < minas:
linha = random.randint(0, tamanho - 1)
coluna = random.randint(0, tamanho - 1)
if quadro[linha][coluna] != "*":
quadro[linha][coluna] = "*"
contar += 1
return quadro
def contar_minas(quadro, linha, coluna):
contar = 0
tamanho = len(quadro)
for i in range(max(0, linha - 1), min(linha + 2, tamanho)):
if quadro[i][coluna] == "*":
contar += 1
for j in range(max(0, coluna - 1), min(coluna + 2, tamanho)):
if quadro[linha][j] == "*":
contar += 1
return contar
def imp_quadro(quadro):
tamanho = len(quadro)
print(" " + " ".join([chr(65 + i) for i in range(tamanho)]))
for i in range(tamanho):
print(f"{i + 1} | " + " ".join(quadro[i]) + " |")
def jogar():
print("----x----x---- CAMPO MINADO ----x----x----")
celulas_abertas = 0
tamanho = input("Informe o tamanho do campo (2 a 26): ")
while not tamanho.isdigit() or int(tamanho) < 2 or int(tamanho) > 26:
print("Valor inválido! Digite um número entre 2 e 26.")
tamanho = input("Informe o tamanho do campo: ")
tamanho = int(tamanho)
tamanho1 = tamanho * tamanho
minas = input("Informe a quantidade de minas: ")
while not minas.isdigit() or int(minas) <= 0:
print("Valor inválido! Informe a quantidade de minas: ")
minas = input("Informe a quantidade de minas: ")
minas = int(minas)
if tamanho < 8:
while minas >= tamanho1:
print(f"Quantidade inválida! O máximo de minas possíveis é {tamanho1 //
2}.")
minas = int(input("Informe a quantidade de minas: "))
else:
while minas > 50:
print("Valor inválido! O máximo permitido é 50.")
minas = int(input("Informe a quantidade de minas: "))
quadro = criar_quadro(tamanho, minas)
quadro_visivel = [[" " for _ in range(tamanho)] for _ in range(tamanho)]
fim_jogo = False
while not fim_jogo:
imp_quadro(quadro_visivel)
acao = input("Informe a letra M para marcar/desmarcar ou qualquer tecla
para abrir: ")
posicao_linha = None
while posicao_linha is None:
posicao_linha = input(f"Informe o número da linha: ")
if not posicao_linha.isdigit() or int(posicao_linha) < 1 or
int(posicao_linha) > tamanho:
print(f"Valor inválido! Digite um número entre 1 e {tamanho}.")
posicao_linha = None
else:
linha = int(posicao_linha) - 1
posicao_coluna = None
while posicao_coluna is None:
posicao_coluna = input("Informe a letra da coluna: ")
if len(posicao_coluna) != 1 or not posicao_coluna.isalpha():
print("Valor inválido! Digite uma única letra para a coluna.")
posicao_coluna = None
else:
coluna = ord(posicao_coluna.upper()) - 65
if coluna < 0 or coluna >= tamanho:
print(f"Coluna fora dos limites! Digite uma letra entre A e
{chr(65 + tamanho - 1)}.")
posicao_coluna = None
if quadro_visivel[linha][coluna] != " ":
print("Essa célula já está aberta! Escolha outra.")
elif acao.lower() == "m":
if quadro_visivel[linha][coluna] == " ":
quadro_visivel[linha][coluna] = "X"
else:
quadro_visivel[linha][coluna] = " "
else:
if quadro[linha][coluna] == "*":
print("BOOM! Você perdeu!")
print(caveira)
fim_jogo = True
else:
quadro_visivel[linha][coluna] = str(contar_minas(quadro, linha,
coluna))
celulas_abertas += 1
if celulas_abertas == tamanho1 - minas:
print(f"Parabéns! Você venceu! {winner}")
imp_quadro(quadro)
fim_jogo = True
jogar()