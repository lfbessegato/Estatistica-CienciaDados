# Import da função
from statistics import median
import numpy as np

# Dados
dados = [3, 1, 5, 2, 3, 1, 7]

# Mediana
print(median(dados))
print(np.quantile(dados, 0.25))
print(np.quantile(dados, 0.75))