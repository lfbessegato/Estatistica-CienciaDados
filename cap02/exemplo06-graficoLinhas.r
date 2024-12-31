# install.packages("plotly")
library(plotly)

# Valores de x
x = c(3, 10, 11, 13, 18, 20, 22, 24, 32, 43, 45, 51, 56, 63, 64, 67, 69, 77, 78, 81, 83, 88, 90, 96)

# Valores de y
y = c(2, 2, 9, 1, 6, 6, 0, 6, 9, 1, 8, 4, 1, 9, 7, 3, 5, 4, 1, 0, 2, 5, 7, 3)

# Criando o data.frame (Resultado do cruazamento de categorias e valores)
dados = data.frame(x, y)

# Criação do Gráfico e Exibição
ggplot(dados, aes(x, y)) + geom_line(col="blue")
