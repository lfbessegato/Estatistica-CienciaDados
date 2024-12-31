# Imports das Bibiliotecas
from statistics import variance
from statistics import stdev
from statistics import mean

import numpy as np

dados = [3, 4, 5, 6, 12]

# Amplitude 
print(np.max(dados)-np.min(dados))

# Variância
print(variance(dados))

# Desvio-padrão
print(stdev(dados))

# Coeficiente de variação
print(stdev(dados) / mean(dados) * 100)
