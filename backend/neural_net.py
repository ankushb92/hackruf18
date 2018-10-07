from sklearn.neural_network import MLPRegressor
import ast
import numpy as np


def train():
	fos = [open('nn1_training'), open('nn2_training'), open('nn3_training')]

	clfs = []
	for fo in fos:
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
		clfs.append(clf)
	return clfs


def predict(inp, clfs):
	dist1 = np.linalg.norm(np.array(inp) - np.array([1.45519152e-10, 2.91038305e-10, 3.39448958e+04, 5.46197439e+05]))
	dist2 = np.linalg.norm(np.array(inp) - np.array([1.45519152e-10, 5.54463897e+05, 6.12790794e+04, -1.74622983e-10]))
	dist3 = np.linalg.norm(np.array(inp) - np.array([6.76717678e+05, 2.91038305e-10, 2.18278728e-11, -1.74622983e-10]))
	if dist1<=dist2 and dist1<=dist3:
		print(clfs[0].predict([inp]))
	elif dist2<=dist1 and dist2<=dist3:
		print(clfs[1].predict([inp]))
	else:
		print(clfs[2].predict([inp]))


if __name__ == '__main__':
	clfs = train()
	predict([0, 0, 0, 560354.342700227], clfs)
