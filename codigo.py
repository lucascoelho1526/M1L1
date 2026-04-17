import random
senha = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

comprimento = int(input("digite sua senha: "))
armazenador = ""


for i in range(comprimento):
    armazenador += random.choice(senha)

print(armazenador)