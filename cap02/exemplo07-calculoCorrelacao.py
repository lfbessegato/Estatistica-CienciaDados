import numpy as np

# Dados de exemplo (duas variáveis)
var1 = [7, 9, 4, 6, 1]
var2 = [2, 3, 4, 5, 6]

# Calculando a correlação Pearson
correlacao = np.corrcoef(var1, var2)[0, 1]

print("A correlação de Pearson: ", correlacao)