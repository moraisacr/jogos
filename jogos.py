import forca
import adivinhacao

print("**************************")
print("****Escolha o seu jogo****")
print("**************************")

print("(1)Forca (2)Adivinahcao ")
jogo = int(input("Qual jogo: "))

if(jogo ==1):
    print("Jogando Forca")
    forca.jogar_forca()
elif(jogo ==2):
    print("Jogando Advinhacao")
    adivinhacao.jogar_adivinhacao()

