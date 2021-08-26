print("**************************")
print("Welcome to Advinhação game")
print("**************************")

total_tentativas = 3
i = 0
num_aletorio = 42
while(i < total_tentativas):
    chute = input("Qual seu Chute")
    print("Vc digitou:",chute)
    int_chute = int(chute )

    if(int_chute == num_aletorio):

        print("Igual")

    else:
       if(int_chute >= num_aletorio):
           print("Maior ou igual")
       elif(int_chute < num_aletorio):
           print("Menor")

    print("Tentativa de numero: ",i+1)
    i = i + 1



print("Endgame")
