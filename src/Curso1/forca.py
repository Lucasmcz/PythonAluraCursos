def jogar():
    print("***************************")
    print("Bem vindo ao jogo da Forca")
    print("**************************")
    palavra_secreta = "banana".upper()
    letras_acertadas= ["_" for caractere in palavra_secreta]
    acertou = False
    enforcou = False
    erros = 0

    while(not acertou and not enforcou):#not acertou == True
                                        #not enforcou == True
        letra = input("Digite uma Letra")
        letra = letra.strip().upper()
        i = 0
        if(letra in palavra_secreta):
            for letra1 in palavra_secreta:
                if(letra.upper() == letra1.upper()):
                    print("Encontrei a letra {} na posição {}".format(letra,i))
                    letras_acertadas[i] = letra

                i = i + 1;
        else:
            erros = erros + 1
        print("Voce tem {} tentativas".format(6-erros))
        enforcou = erros == 6#enforocu == True , not enforcou == False
        acertou = "_" not in letras_acertadas#acertou == True, not acertou == False
        print(letras_acertadas)
        if(acertou):
            print("You win :)")
        elif(enforcou):
            print("You lose :(")
        else:
            print("Running!")






if(__name__ == "__main__"):
    jogar()