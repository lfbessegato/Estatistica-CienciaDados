# install.packages("plotly")
library(plotly)

# Categorias
x = c("Java", "R", "Python")

# Valores de cada categoria
y = c(27, 42, 89)

# Criando o data.frame (Resultado do cruazamento de categorias e valores)
dados = data.frame(x, y)

# Criação do Gráfico e Exibição
barplot(dados$y, names.arg=dados$x, col="light blue", horiz = T)

