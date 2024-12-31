# Imports de bibliotecas
from matplotlib import pyplot

# Valores  
x = [64, 77, 45, 64, 88, 11, 22, 67, 81, 88, 43, 51, 18, 32, 3, 10, 90, 20, 24, 63, 51, 96, 11, 78] 

# Número de intervalos (bins)
num_bins = 6

# Criação do gráfico
pyplot.hist(x, num_bins)

# Exibição do Gráfico
pyplot.show()