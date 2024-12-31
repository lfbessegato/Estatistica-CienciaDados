import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Criando um DataFrame de exemplo com algumas variáveis
dados = { 
    'Idade': [45, 20, 25, 40, 34],
    'Salario': [10000, 70000, 5000, 9000, 8000],
    'Experiencia': [13, 2, 5, 10, 12]
}

df = pd.DataFrame(dados)

# Calculando a matriz de correlação
mt_corr = df.corr()

# Plotando a matriz de correlacao como um gráfico de calor com valores
plt.figure(figsize=(8, 6))
plt.imshow(mt_corr, cmap='coolwarm', interpolation='nearest')
plt.colorbar()

# Adicionando os valores de correlação nas células do gráfico
for i in range(len(df.columns)):
    for j in range(len(df.columns)):
        plt.text(i, j, f'{mt_corr.iloc[i, j]:.2f}', ha='center', va='center', color='black', fontsize=12)

plt.xticks(np.arange(len(df.columns)), df.columns, rotation=45)
plt.xticks(np.arange(len(df.columns)), df.columns)
plt.title('Matriz de Correlação')
plt.show()