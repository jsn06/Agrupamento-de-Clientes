
# Projeto de Machine Learning: Agrupamento de Clientes com K-Means e DBSCAN

Este projeto tem como objetivo aplicar algoritmos de **clustering** (agrupamento não supervisionado) para segmentar clientes com base em características como idade, renda anual e pontuação de gastos. Utilizamos dois algoritmos populares: **K-Means** e **DBSCAN**.

---

##  Descrição do Problema

Empresas que atuam no varejo frequentemente desejam entender melhor seus clientes para oferecer produtos e serviços personalizados. Neste projeto, simulamos um conjunto de dados de clientes de um shopping center e aplicamos técnicas de agrupamento para identificar padrões de comportamento.

---

##  Metodologia

1. **Geração de Dados Sintéticos**:
   - Criamos um dataset com 200 clientes contendo:
     - Idade
     - Renda Anual
     - Pontuação de Gastos

2. **Pré-processamento**:
   - Padronização dos dados com `StandardScaler`
   - Redução de dimensionalidade com `PCA` para visualização

3. **Modelos Aplicados**:
   - **K-Means**:
     - Número de clusters definido como 4
     - Avaliação com *Silhouette Score*
   - **DBSCAN**:
     - Parâmetros ajustados (`eps=1.2`, `min_samples=4`)
     - Detecção de outliers
     - Avaliação com *Silhouette Score*

4. **Visualização**:
   - Gráficos comparativos dos clusters gerados por cada algoritmo

---

##  Bibliotecas Utilizadas

- `numpy`
- `pandas`
- `matplotlib`
- `scikit-learn`

---

##  Como Executar

1. Copie o arquivo `clustering_clientes.py`
2. Instale as dependências com:

```bash
pip install numpy pandas matplotlib scikit-learn
