# Instalando Bibilioteca
install.packages("e1071")

# Carregando a Bibilioteca
library(e1071)

# Dados
x = c(8.0, 1, 2.5, 4, 28.0)

# Calculando a assimetria manualmente
n = length(x)
mean_ = sum(x) / n
a= sum(((x - mean_)**3) * n / ((n - 1) * (n - 2) * sd(x)**3))

# Calculando a assimetria usando a Biblioteca
skewness(x, type = 2)
# AS > 0 (1.947043) --> distribuição será assimétrica a direita ou positiva, 
# terá concentração dos valores no gráfico a esquerda e a curva se alongará 
# mais a direita do gráfico