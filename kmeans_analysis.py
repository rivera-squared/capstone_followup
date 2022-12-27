import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer

#pip install yellowbrick

df = pd.read_csv('https://raw.githubusercontent.com/rivera-squared/capstone_followup/main/primarias_19_21.csv')

list(df.columns)

# Exploratory Analysis
df.groupby('region')['codigo'].count()
df[['matricula_21','ausentismo_cronico_21','ciencias_meta_21','espanol_meta_21','ingles_meta_21','mate_meta_21']].describe()

df.dtypes

# KMeans clustering analysis
X = df[['matricula_21','ausentismo_cronico_21','ciencias_meta_21','espanol_meta_21','ingles_meta_21','mate_meta_21','escuela_receptora']]
X = X.dropna()

# Evaluating clusters
model = KMeans(random_state = 0, n_init = 20)
visualizer = KElbowVisualizer(model, k = (2,13))
visualizer.fit(X)
visualizer.show()


kmeans = KMeans(n_clusters = 4, random_state = 0, n_init=20).fit(X)
kmeans.labels_
kmeans.inertia_
kmeans.score(X)

df = df.dropna()
df['cluster'] = kmeans.labels_
                                                                                                               receptora[1], matricula[1], espanol[1], ingles[1], mate[1], ciencias[1]))

for cluster in clusters:
    x = df[df['cluster'] == cluster]    
    receptora = x.groupby('escuela_receptora')['codigo'].count()
    
cluster_stats = df.groupby(['cluster'])[['matricula_21','ciencias_meta_21',
                                             'espanol_meta_19','mate_meta_19','ingles_meta_19']].mean().reset_index()    

