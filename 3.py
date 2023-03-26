import json

def ehFeriadoOuFinalDeSemana(faturamento):
    return faturamento == 0

def exercicioTarget():
    with open("dados.json") as f:
        jsonData = json.load(f)

    diaDoMenorValor = 0
    menorValor = float("inf")

    diaDoMaiorValor = 0
    maiorvalor = float("-inf")

    somaMensal = 0
    nroDiasMes = 0

    for item in jsonData:
        dia, valor = item.items()
        
        if (not ehFeriadoOuFinalDeSemana(valor[1])):
            nroDiasMes += 1
            somaMensal += valor[1]

            if valor[1] < menorValor:
                menorValor = valor[1]
                diaDoMenorvalor = dia[1]
            if valor[1] > maiorvalor:
                maiorvalor = valor[1]
                diaDoMaiorValor = dia[1]

    mediaMensal = somaMensal / nroDiasMes

    diasQueMediaFoiSuperior = 0

    for item in jsonData:
        dia, valor = item.items()
        if valor[1] > mediaMensal:
            diasQueMediaFoiSuperior += 1

    print(f"A quantidade de dias que o faturamento foi maior que a média mensal foi de {diasQueMediaFoiSuperior} dias")
    print(f"O Menor faturamento ocorreu no dia {diaDoMenorvalor} e o valor foi {menorValor}")
    print(f"O Maior faturamento ocorreu no dia {diaDoMaiorValor} e o valor foi {maiorvalor}")

exercicioTarget()
