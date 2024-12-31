install.packages("plotly")
library(plotly)

# Categorias, tamanhos dos setores e %. Os setores serão ordenados e plotados
# no sentido anti-horário.

categorias = c("Java", "R", "Python")
setores = c(45, 25, 30)

# Criando o data.frame (Resultado do cruzamento de categorias e setores)
dados=data.frame(categorias, setores)

#  Criação do Gráfico e Exibição
plot_ly(dados, 
        labels = ~categorias, 
        values = ~setores, 
        type = 'pie')

