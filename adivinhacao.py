import random

def jogar_adivinhacao():

    print("********************************")
    print("Bem vindo ao jogo de adivinhacao")
    print("********************************")

    numero_secreto = int(random.randrange(0,101))
    total_de_tentativas = 0
    pontos = 1000
    print(numero_secreto)

    print("Qual nivel de dificuldade?")
    print("1 - Facil")
    print("2 - Medio")
    print("3 - Dificil")
    nivel= int(input("Define o nivel: "))

    if(nivel ==1):
        total_de_tentativas =20
    elif(nivel ==2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativas {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Voce digitou ", chute)

        if(chute < 1 or chute > 100):
                print("Voce deve digitar um numero entre 1 e 100!")
                continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Voce acertou e fez {} pontos!".format(pontos ))
            break
        else:
            if(maior):
                print("Voce errou! O seu chute foi maior que o numero secreto.")
            elif(menor):
                print("Voce errou! O seu chute foi menor que o numero secreto.")
            pontos_perdidos = abs(numero_secreto-chute)
            pontos = pontos - pontos_perdidos

    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar_adivinhacao()