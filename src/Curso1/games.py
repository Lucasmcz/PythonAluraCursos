import forca
import advinhacao
def escolher_jogo():
    print(" (1) para forca (2) para advinhacao")
    jogo = int(input("Qual o jogo?"))
    if(jogo == 1):
        print("jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Advinhação")
        advinhacao.jogar()


if(__name__ == "__main__"):
    escolher_jogo()