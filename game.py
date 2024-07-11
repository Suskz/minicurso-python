import random
 
def cabecalho():
    print("*************************")
    print("***JOGO DA ADVINHAÇÃO****")
    print("*************************")
    
cabecalho()
numero_secreto = random.randrange(1,101)
total_tentativas = 0
pontos = 1000
 
print("Qual o nível de dificuldade desejado?")
print("(1) Facil  (2) Médio  (3) Difícil")
nivel = int(input("Defina o nível: "))
while(nivel>3 or nivel<1):
    print("O nível deve ser entre 1 e 3")
    nivel = int(input("Defina o nível: "))
if(nivel==1):
    total_tentativas=20
elif(nivel==2):
    total_tentativas=10
else:
    total_tentativas=5
 
for rodada in range(1,total_tentativas+1):
    print(f"Tentativa {rodada} de {total_tentativas}")
    chute = int(input("Digite um numero de 1 a 100\n"))
    
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
 
    if(acertou):
        print(f"Parabéns!! Você acertou. Você fez {pontos} pontos")
        print(f"Pontuação final: {pontos} pontos")
        break
    else:
        if(maior):
            print("Você errou! Seu chute foi maior")
        elif(menor):
            print("Você errou! Seu chute foi menor")
            print("")
        pontos = pontos - 50