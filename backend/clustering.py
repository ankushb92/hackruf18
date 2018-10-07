from sklearn.cluster import KMeans
from sklearn import svm
from sklearn.preprocessing import StandardScaler
import ast
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

scalar = StandardScaler()
with open('tocluster') as fo:
    data = scalar.fit_transform(np.array([np.array(ast.literal_eval(l)) for l in fo.readlines()]))

kmeans = KMeans(init='k-means++', n_clusters=3, n_init=10)
kmeans.fit(data)

axislabels = ['Age', 'Last Balance', 'Transaction Count', 'Debit Sum', 'Credit Sum', 'LRLR Sum', 'LRHR Sum', 'HRLR Sum', 'HRHR Sum']
x_feature = 0
y_feature = 1
z_feature = 3

x_min, x_max = data[:, x_feature].min() - 0.1, data[:, x_feature].max() + 0.1
y_min, y_max = data[:, y_feature].min() - 0.1, data[:, y_feature].max() + 0.1
z_min, z_max = data[:, z_feature].min() - 0.1, data[:, z_feature].max() + 0.1
points = list(zip(data[:, x_feature], data[:, y_feature], data[:, z_feature]))
labels = kmeans.labels_
groups = [[] for _ in range(max(labels)+1)]
for p,l in zip(points, labels):
    groups[l].append(p)

colors = ['r', 'g', 'b']
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i, group in enumerate(groups):
    xs, ys, zs = list(zip(*group))
    ax.scatter(xs, ys, zs, c=colors[i], marker='o')
ax.set_xlabel(axislabels[x_feature])
ax.set_ylabel(axislabels[y_feature])
ax.set_zlabel(axislabels[z_feature])
plt.show()


# Plot the centroids as a white X
'''
plt.plot(data[:, x_feature], data[:, y_feature], 'k.', markersize=2)
plt.scatter(centroids[:, x_feature], centroids[:, y_feature],
            marker='x', s=169, linewidths=3,
            color='b', zorder=10)

plt.title('K-means')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()'''
