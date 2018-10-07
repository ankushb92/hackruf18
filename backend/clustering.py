from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import ast
import numpy as np
import matplotlib.pyplot as plt

fo = open('tocluster')

data = []
for line in fo:
	data.append(np.array(ast.literal_eval(line)))
data = np.array(data)

scaler = StandardScaler()
data = scaler.fit_transform(data)

kmeans = KMeans(init='k-means++', n_clusters=3, n_init=10)
kmeans.fit(data)

x_feature = 1
y_feature = 2

x_min, x_max = data[:, x_feature].min() - 0.1, data[:, x_feature].max() + 0.1
y_min, y_max = data[:, y_feature].min() - 0.1, data[:, y_feature].max() + 0.1


plt.plot(data[:, x_feature], data[:, y_feature], 'k.', markersize=2)

# Plot the centroids as a white X
centroids = kmeans.cluster_centers_
print(centroids)
plt.scatter(centroids[:, x_feature], centroids[:, y_feature],
            marker='x', s=169, linewidths=3,
            color='b', zorder=10)

plt.title('K-means')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()