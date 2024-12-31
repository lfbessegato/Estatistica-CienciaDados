# Imports de Bibliotecas
from matplotlib import pyplot

# Categorias e tamanhos dos setores. Os setores serão ordenados e plotados no sentido anti-horário

categorias = 'Java', 'R', 'Python'
setores = [45, 25, 30]

# Criação do gráfico
pyplot.pie(x=setores, labels=categorias)
pyplot.show()