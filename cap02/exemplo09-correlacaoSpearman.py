import pandas as pd
import scipy.stats as stats

# Criando o DataFrame de exemplo com variáveis ordinais e contínuas
dados = {
    'Satisfação': ['Baixa', 'Média', 'Alta', 'Média', 'Alta'],
    'Idade': [25, 30, 35, 40, 45],
    'Salário':[50000, 60000, 75000, 90000, 100000]    
}

df = pd.DataFrame(dados)

# Mapeando as categorias para valores ordinais 
mapeamento_ordem = {'Baixa': 1, 'Média':2, 'Alta': 3}
df['Satisfação'] = df['Satisfação'].map(mapeamento_ordem)

# Calculando a matriz de correlação de Spearman
matriz_correlacao_spearman = df.corr(method='spearman')

# Imprimindo a matriz de correlação de Spearman
print("Matriz de Correlação de Spearman: ")
print(matriz_correlacao_spearman)