valorSP = 67836.43
valorRJ = 36678.66
valorMG = 29229.88
valorES = 27165.48
valorOutrosEstados = 19849.53

valorTotal = valorSP + valorRJ + valorMG + valorES + valorOutrosEstados

percentualSP = valorSP/valorTotal * 100
percentualRJ = valorRJ/valorTotal * 100
percentualMG = valorMG/valorTotal * 100
percentualES = valorES/valorTotal * 100
percentualOutrosEstados = valorOutrosEstados/valorTotal * 100

print(f"O percentual de São Paulo quanto ao valor total é de {round(percentualSP,2)}%")
print(f"O percentual de Rio de Janeiro quanto ao valor total é de {round(percentualRJ,2)}%")
print(f"O percentual de Minas Gerais quanto ao valor total é de {round(percentualMG,2)}%")
print(f"O percentual de Espirito santo quanto ao valor total é de {round(percentualES,2)}%")
print(f"O percentual de Outros Estados quanto ao valor total é de {round(percentualOutrosEstados,2)}%")
