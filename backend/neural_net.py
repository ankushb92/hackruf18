from sklearn.neural_network import MLPRegressor
import ast
import numpy as np

fo = open('nn_training')

X = []
Y = []
for line in fo:
	x = ast.literal_eval(line)
	y = x[-1]
	x = np.array(x[:-1])
	X.append(x)
	Y.append(y)
X = np.array(X)
Y = np.array(Y)

clf = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(X, Y)

print(clf.predict([[0, 0, 0, 560354.342700227]]))