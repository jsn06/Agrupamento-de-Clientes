# Projeto de Machine Learning: Agrupamento de Clientes com K-Means e DBSCAN

Este projeto aplica algoritmos de *clustering* (agrupamento não supervisionado) para segmentar clientes com base em características como idade, renda anual e pontuação de gastos. Utilizamos os algoritmos *K-Means* e *DBSCAN, com visualização dos resultados por meio de **PCA (Análise de Componentes Principais)*.

---

## 📌 Descrição do Problema

Empresas de varejo desejam entender melhor seus clientes para oferecer produtos e serviços personalizados. Neste projeto, simulamos dados de clientes de um shopping center e aplicamos técnicas de agrupamento para identificar padrões de comportamento.

---

## 💡 Motivação

A segmentação de clientes permite:
- Criar campanhas de marketing mais eficazes
- Personalizar ofertas e promoções
- Aumentar a fidelização e o valor do cliente

---

## 🔍 Metodologia

1. *Geração de Dados Sintéticos*:
   - Dataset com 200 clientes contendo:
     - Idade
     - Renda Anual
     - Pontuação de Gastos

2. *Pré-processamento*:
   - Padronização com StandardScaler
   - Redução de dimensionalidade com PCA para visualização

3. *Modelos Aplicados*:
   - *K-Means*:
     - Número de clusters: 4
     - Avaliação com Silhouette Score
   - *DBSCAN*:
     - Parâmetros: eps=1.2, min_samples=4
     - Detecção de outliers
     - Avaliação com Silhouette Score

4. *Visualização*:
   - Gráficos comparativos dos clusters gerados por cada algoritmo

---

## ⚙️ Algoritmos Utilizados

### 🎯 PCA (Principal Component Analysis)
- Técnica de redução de dimensionalidade
- Projeta os dados em eixos que maximizam a variância
- Permite visualização em 2D mantendo a estrutura dos dados

### 📊 K-Means
- Algoritmo de clustering baseado em distância
- Agrupa os dados em k clusters com centróides
- Requer definição prévia do número de clusters

### 🧭 DBSCAN
- Algoritmo baseado em densidade
- Agrupa pontos densamente conectados e detecta outliers
- Não requer número de clusters como entrada

---

## 📈 Resultados

- *K-Means*:
  - Formou 4 clusters bem definidos
  - Silhouette Score alto
- *DBSCAN*:
  - Detectou 3 clusters e pontos de ruído
  - Silhouette Score razoável
- *PCA*:
  - Permitiu visualização clara dos agrupamentos em 2D

---

## ✅ Conclusões

- K-Means é eficaz para clusters bem separados e esféricos
- DBSCAN é útil para detectar formas arbitrárias e outliers
- PCA foi essencial para visualização e interpretação dos resultados

---

## 🚀 Próximos Passos

- Aplicar os algoritmos em dados reais
- Testar novos algoritmos como HDBSCAN
- Otimizar hiperparâmetros com validação cruzada
- Explorar mais variáveis e fontes de dados

---

## ▶️ Como Executar

1. Instale as dependências com:

```bash
pip install numpy pandas matplotlib scikit-learn
