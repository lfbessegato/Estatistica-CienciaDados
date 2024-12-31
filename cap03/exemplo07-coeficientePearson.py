# Import da função
from scipy.stats import skew

# Dados 
x = [8.0, 1, 2.5, 4, 28.0]

# Calculando a assimetria manualmente
n = len(x)
mean_ = sum(x) / n
var_ = sum((item - mean_)** 2 for item in x) / (n - 1)
std_ = var_ ** 0.5
skew_ = (sum((item - mean_)** 3 for item in x) * n / ((n - 1) * (n - 2) * std_ ** 3))
print('Manual....: ', skew_)

# Calculando a assimetria usando a Biblioteca
print('Automático: ',skew_)

# AS > 0 (1.947043227390592) --> distribuição será assimétrica a direita ou positiva, 
# terá concentração dos valores no gráfico à esquerda e a curva se alongará mais a direita 
# do gráfico.