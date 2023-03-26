
def inverteCaracteres(str):
    strInvertida = ""

    for i in range(len(str)-1, -1, -1):
        strInvertida += str[i]

    return strInvertida

str = input("Digite uma palavra: ")
print(inverteCaracteres(str))