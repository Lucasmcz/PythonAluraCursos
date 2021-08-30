import  random

def jogar():
    imprime_msg_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializar_letras(palavra_secreta)
    print(palavra_secreta)
    print(letras_acertadas)
    acertou = False
    enforcou = False
    erros = 0


    while(not acertou and not enforcou):

            '''letra = input("Digite uma Letra")
            letra = letra.strip().upper()
            print(palavra_secreta)'''
            letra = pede_chute()
            if (letra  in palavra_secreta):
                marcar_chute_correto(letra,letras_acertadas,palavra_secreta)
                print(letras_acertadas)
                '''i = 0
                for letra1 in palavra_secreta:
                    if(letra == letra1):
                        letras_acertadas[i] = letra1
                    i = i + 1'''
            else:
                erros = erros + 1
                desenha_forca(erros)
            print("Voce tem {} tentativas".format(7-erros))
            enforcou = erros == 7#enforocu == True , not enforcou == False
            acertou = "_" not in letras_acertadas#acertou == True, not acertou == False


            if(acertou):
                print("You win :)")
            elif(enforcou):
                print("You lose :(")
            else:
                print("Running!")

def imprime_msg_abertura():
    print("**************************")
    print("Bem vindo ao jogo da Forca")
    print("**************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt","r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    #print(palavra_secreta)
    return palavra_secreta

def inicializar_letras(palavra):
    return ["_" for  caractere in palavra]

def pede_chute():
    letra = input("Digite uma Letra")
    letra = letra.strip().upper()

    return letra

def marcar_chute_correto(letra,letras_acertadas, palavra_secreta):
    i = 0
    for letra1 in palavra_secreta:
        if (letra == letra1):
            letras_acertadas[i] = letra1
        i = i + 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")
    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    elif(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")
    elif (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")
    elif (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    elif(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    elif (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    elif (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()
