# Dados
dados = c(3, 1, 5, 2, 3, 1, 7)

# Mediana
print(median(dados))

# Primeiro Quartil
print(quantile(dados, .25))

# Terceiro Quartil
print(quantile(dados, .75))

# Achando o Primeiro Quartil (Q1), Segundo Quartil (Q2) e o 
# Terceiro Quartil (Q3)
print(summary(dados))
