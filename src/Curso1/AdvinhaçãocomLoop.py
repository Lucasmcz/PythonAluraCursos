print("**************************")
print("Welcome to Advinhação game")
print("**************************")

total_tentativas = 3
i = 0
num_aletorio = 42
for i in range(0,total_tentativas):
    chute = input("Qual seu Chute")
    print("digite um numero entre 1 e 100:",chute)
    int_chute = int(chute)
    if(int_chute > 100 or int_chute < 0):
        print("Vc deve digitar um Numero entre 1 e 100")
        continue
    if(int_chute == num_aletorio):

        print("Igual")
        break
    else:
       if(int_chute >= num_aletorio):
           print("Maior ou igual")
       elif(int_chute < num_aletorio):
           print("Menor")

    print("Tentativa de Nª{}: ".format(i+1))




print("ENDGAME")

