print("Tentativa de {0} de {1}".format(1,3))#printar o numero 1 e 3
print("Tentativa de {1} de {0}".format(1,3))#printar o numero 3 e 1

#//////////////////////////////////////////////////////////////////////
#Formatação de Floats

print("R$ {}".format(1.59))
print("R$ {:f}".format(1.59))#Varias casas decimais
print("R$ {:.2f}".format(1.59))#2 Casas Decimais
print("R$ {:.3f}".format(2.79))#3 Casas Decimais
print("R$ {:.4f}".format(2))#4 Casas Decimais


#Formatação de Inteiros
print("R$ {:07d}".format(4))#Zeros a Esquerda

#Utilização nas Datas

print("Data {:02}/{:02}".format(9,4))#Datas