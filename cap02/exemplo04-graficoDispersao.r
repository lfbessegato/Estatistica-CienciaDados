# install.packages("plotly")
library(plotly)

# Valores de x
x = c(46, 9, 25, 42, 95)

# Valores y
y = c(12, 23, 4, 9, 15)

# Criando o data.frame (Resultado do cruazamento de categorias e valores)
dados = data.frame(x, y)

# Criação do Gráfico e Exibição
ggplot(dados, aes(x, y)) + geom_point(size=3, col="blue")
