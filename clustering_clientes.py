
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score

np.random.seed(42)
idade = np.random.normal(40, 12, 200)
renda = np.random.normal(60000, 15000, 200)
pontuacao = np.random.normal(50, 20, 200)

df = pd.DataFrame({
    'Idade': idade,
    'Renda Anual': renda,
    'Pontuação de Gastos': pontuacao
})

scaler = StandardScaler()
dados_padronizados = scaler.fit_transform(df)

pca = PCA(n_components=2)
dados_pca = pca.fit_transform(dados_padronizados)

kmeans = KMeans(n_clusters=4, random_state=42)
kmeans_labels = kmeans.fit_predict(dados_padronizados)
kmeans_score = silhouette_score(dados_padronizados, kmeans_labels)

dbscan = DBSCAN(eps=1.2, min_samples=4)
dbscan_labels = dbscan.fit_predict(dados_padronizados)

if len(set(dbscan_labels)) > 1:
    mask = dbscan_labels != -1
    if np.sum(mask) > 1 and len(set(dbscan_labels[mask])) > 1:
        dbscan_score = silhouette_score(dados_padronizados[mask], dbscan_labels[mask])
    else:
        dbscan_score = None
else:
    dbscan_score = None

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].scatter(dados_pca[:, 0], dados_pca[:, 1], c=kmeans_labels, cmap='viridis')
axs[0].set_title(f'K-Means Clustering\nSilhouette Score: {kmeans_score:.2f}')

axs[1].scatter(dados_pca[:, 0], dados_pca[:, 1], c=dbscan_labels, cmap='plasma')
if dbscan_score is not None:
    axs[1].set_title(f'DBSCAN Clustering\nSilhouette Score: {dbscan_score:.2f}')
else:
    axs[1].set_title('DBSCAN Clustering\n(Sem clusters válidos)')

plt.tight_layout()
plt.savefig("clusters_comparacao.png")
plt.show()
