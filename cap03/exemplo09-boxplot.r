# Carregamento da Bibilioteca
library(ggplot2)

# Utilizando o dataset nativo Iris
dados = iris

# Plotando um boxplot por espécies da característica Petal.length
ggplot(dados, aes(x=Species, y=Petal.Length, fill=Species)) + geom_boxplot()
