# install.packages("plotly")
library(plotly)

# Valores
x = c(64, 77, 45, 64, 88, 11, 22, 67, 81, 88, 43, 51, 18, 32, 3, 10, 90, 20, 24, 63, 51, 96, 11, 78)

# Números de intervalos (bins)
num_bins = 6

# Criando o data.frame (Resultado do cruazamento de categorias e valores)
dados = data.frame(x)

# Criação do Gráfico e Exibição
ggplot(dados, aes(x)) + geom_histogram(bins = num_bins, fill="light blue")

