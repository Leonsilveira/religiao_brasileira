import matplotlib.pyplot as plt
import seaborn as sns

# Dados
religions = ['Católica', 'Evangélica', 'Sem religião', 'Espírita', 'Umbanda/Candomblé', 'Outra', 'Ateu', 'Judaica']
percentages = [50, 31, 10, 3, 2, 2, 1, 0.3]
ages = {
    "Católica": [13, 17, 18, 26, 25],
    "Evangélica": [19, 21, 22, 23, 16],
}

# Configuração geral
plt.style.use('ggplot')  # Estilo para gráficos

# 1. Gráfico de Linha
plt.figure(figsize=(10, 6))
for religion, age_data in ages.items():
    plt.plot(['16-24', '25-34', '35-44', '45-59', '60+'], age_data, label=religion, marker='o')
plt.title("Distribuição Etária por Religião")
plt.xlabel("Faixa Etária")
plt.ylabel("Porcentagem (%)")
plt.legend()
plt.savefig("line_plot_religion.png")
plt.show()

# 2. Gráfico de Barras
plt.figure(figsize=(10, 6))
plt.bar(religions, percentages, color='skyblue')
plt.title("Distribuição de Religiões no Brasil")
plt.xlabel("Religiões")
plt.ylabel("Porcentagem (%)")
plt.xticks(rotation=45)
plt.savefig("bar_plot_religion.png")
plt.show()

# 3. Gráfico de Pizza
plt.figure(figsize=(10, 8))
explode = [0.1 if p == max(percentages) else 0 for p in percentages]
plt.pie(percentages, labels=religions, autopct='%1.1f%%', startangle=90, explode=explode)
plt.title("Proporção de Religiões no Brasil")
plt.savefig("pie_chart_religion.png")
plt.show()

# 4. Histograma
plt.figure(figsize=(10, 6))
sns.histplot(percentages, bins=8, kde=True, color='purple')
plt.title("Distribuição de Porcentagens das Religiões")
plt.xlabel("Porcentagem (%)")
plt.ylabel("Frequência")
plt.savefig("histogram_religion.png")
plt.show()

# 5. Gráfico de Dispersão
plt.figure(figsize=(10, 6))
categories = list(range(len(religions)))  # Valores numéricos para categorias
plt.scatter(categories, percentages, color='green', s=100)
plt.xticks(categories, religions, rotation=45)
plt.title("Dispersão das Porcentagens das Religiões")
plt.xlabel("Religiões")
plt.ylabel("Porcentagem (%)")
plt.savefig("scatter_plot_religion.png")
plt.show()