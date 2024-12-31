# Imports das Bibiliotecas
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando o dataset
dados = sns.load_dataset('iris')

# Plotando um boxplot por especies da característica petal length 
sns.boxplot(x=dados["species"], y=dados["petal_length"])

plt.show()