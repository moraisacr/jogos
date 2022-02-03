def jogar_forca():

    print("**************************")
    print("Bem vindo ao jogo de Forca")
    print("**************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False
    print(letras_acertadas)
    #enquanto nao enforcou e nao acertou
    while(not enforcou and not acertou ):

        chute = input("Qual a letra?")
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra

            index = index + 1
        print(letras_acertadas)

    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar_forca()
