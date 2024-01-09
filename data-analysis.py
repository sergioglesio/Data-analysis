import pandas as pd                         #pip install pandas matplotlib (windows)
import matplotlib.pyplot as plt             #pip3 install pandas matplotlib (macOS)

# Criar um conjunto de dados fictício
dados = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Idade': [25, 30, 22, 35, 28],
    'Salario': [50000, 60000, 45000, 70000, 55000],
    'Pontuacao': [80, 75, 90, 60, 85]
}

df = pd.DataFrame(dados)

print("Informações sobre o DataFrame:")
print(df.info())

# Estatísticas descritivas do DataFrame
print("\nEstatísticas Descritivas:")
print(df.describe())

# Aqui crio o gráfico de barras para Idade
plt.figure(figsize=(10, 5))
plt.bar(df['Nome'], df['Idade'], color='skyblue')
plt.title('Idade dos Indivíduos')
plt.xlabel('Nome')
plt.ylabel('Idade')
plt.show()

# Aqui crio a dispersão para Salário e Pontuação
plt.figure(figsize=(10, 5))
plt.scatter(df['Salario'], df['Pontuacao'], color='orange')
plt.title('Relação entre Salário e Pontuação')
plt.xlabel('Salário')
plt.ylabel('Pontuação')
plt.show()
