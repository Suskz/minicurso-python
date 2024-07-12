import random 
def jogo_forca():
    print("*************************")
    print("******JOGO DA FORCA******")
    print("*************************\n")

    with open("palavras.txt", "r") as file: 
        palavra_secreta = random.choice(open("palavras.txt","r").readline().split())

    letras_acertadas = ["_" for letra in palavra_secreta]
 
    enforcou = False
    acertou = False
    erros = 0
    print(letras_acertadas)
 
    while(not enforcou and not acertou):
        chute = input("Qual é seu chute? ")
        chute = chute.upper()
        if(chute in palavra_secreta):
            index=0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index]=letra
                index=index+1
        else:
            erros=erros+1
        
        enforcou = erros==5
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        count = 5 - erros
 
        if(acertou):
            print("Você é muito bom, parabéns!")
            print("\nFIM DE JOGO")
        elif(enforcou):
            print("Você perdeu, tente novamente depois")
            print("\nFIM DE JOGO")
        else:
            print(f"Quantidade de erros {erros}, restam {count}\n")
 
jogo_forca()