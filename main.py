dict = {
            "farmar aura": "quando voce manda bem",
            "sabour": "é quase algo"
            }

palavra = input("Digite uma palavra moderna que você não entende: ")
if palavra in dict.keys():
    print(dict [palavra])
else:
    print("palvra nao encontrada")
