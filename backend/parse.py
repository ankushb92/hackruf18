
import random
import json
import numpy as np

class Parser:
    def __init__(self, transactions, holdings, age):
        self.transactions = transactions
        self.holdings = holdings
        self.age = age

    def get_k_means_attrs(self):
        """ returns [age, last_balance, transaction_count, debit_sum, credit_sum, lrlr_sum, lrhr_sum, hrlr_sum, hrhr_sum]."""

        debit_sum = 0
        credit_sum = 0
        lrlr_sum = 0
        lrhr_sum = 0
        hrlr_sum = 0
        hrhr_sum = 0
        for transaction in self.transactions['transaction']:
            if transaction['baseType'] == 'DEBIT':
                debit_sum += transaction['amount']['amount']
            elif transaction['baseType'] == 'CREDIT':
                credit_sum += transaction['amount']['amount']
        
        transaction_length = len(self.transactions['transaction'])

        for holding in self.holdings['holding']:
            if holding['assetClassification'][0]['classificationValue'] == 'Low Risk Low Reward':
                lrlr_sum += holding['value']['amount']
            elif holding['assetClassification'][0]['classificationValue'] == 'Low Risk High Reward':
                lrhr_sum += holding['value']['amount']
            elif holding['assetClassification'][0]['classificationValue'] == 'High Risk Low Reward':
                hrlr_sum += holding['value']['amount']
            elif holding['assetClassification'][0]['classificationValue'] == 'High Risk High Reward':
                hrhr_sum += holding['value']['amount']

        return [self.age, self.transactions['transaction'][-1]['runningBalance']['amount'], transaction_length, debit_sum, credit_sum, lrlr_sum, lrhr_sum, hrlr_sum, hrhr_sum]

    def get_neural_net_attrs(self):
        """returns [lrlr_sum, lrhr_sum, hrlr_sum, hrhr_sum]"""
        lrlr_sum = 0
        lrhr_sum = 0
        hrlr_sum = 0
        hrhr_sum = 0

        for holding in self.holdings['holding']:
            if holding['assetClassification'][0]['classificationValue'] == 'Low Risk Low Reward':
                lrlr_sum += holding['value']['amount']
            elif holding['assetClassification'][0]['classificationValue'] == 'Low Risk High Reward':
                lrhr_sum += holding['value']['amount']
            elif holding['assetClassification'][0]['classificationValue'] == 'High Risk Low Reward':
                hrlr_sum += holding['value']['amount']
            elif holding['assetClassification'][0]['classificationValue'] == 'High Risk High Reward':
                hrhr_sum += holding['value']['amount']

        return [lrlr_sum, lrhr_sum, hrlr_sum, hrhr_sum]


def nn_train_prob(x):
    return 1/(np.e**(x/100000)**2)

if __name__ == '__main__':
    fo = open('1.json')
    i = 0
    transactions = None
    holdings = None
    age = None

    f_cluster = open('tocluster', 'w')
    f_nn1 = open('nn1_training', 'w')
    f_nn2 = open('nn2_training', 'w')
    f_nn3 = open('nn3_training', 'w')

    for line in fo:
        i += 1
        if i%2==1:
            transactions = json.loads(line)
        else:
            holdings = json.loads(line)
            age = int(np.random.normal(loc=27, scale=5))
            parser = Parser(transactions, holdings, age)
            f_cluster.write(json.dumps(parser.get_k_means_attrs())+'\n')
            nn_attrs = parser.get_neural_net_attrs()
            prob = nn_train_prob(np.linalg.norm(np.array(nn_attrs) - np.array([1.45519152e-10, 2.91038305e-10, 3.39448958e+04, 5.46197439e+05])))
            f_nn1.write(str(nn_attrs+[prob])+'\n')

    fo = open('2.json')
    i = 0
    transactions = None
    holdings = None
    age = None
    for line in fo:
        i += 1
        if i%2==1:
            transactions = json.loads(line)
        else:
            holdings = json.loads(line)
            age = int(np.random.normal(loc=40, scale=7))
            parser = Parser(transactions, holdings, age)
            f_cluster.write(json.dumps(parser.get_k_means_attrs())+'\n')
            nn_attrs = parser.get_neural_net_attrs()
            prob = nn_train_prob(np.linalg.norm(np.array(nn_attrs) - np.array([1.45519152e-10, 5.54463897e+05, 6.12790794e+04, -1.74622983e-10])))
            f_nn2.write(str(nn_attrs+[prob])+'\n')


    fo = open('3.json')
    i = 0
    transactions = None
    holdings = None
    age = None
    for line in fo:
        i += 1
        if i%2==1:
            transactions = json.loads(line)
        else:
            holdings = json.loads(line)
            age = int(np.random.normal(loc=55, scale=7))
            parser = Parser(transactions, holdings, age)
            f_cluster.write(json.dumps(parser.get_k_means_attrs())+'\n')
            nn_attrs = parser.get_neural_net_attrs()
            prob = nn_train_prob(np.linalg.norm(np.array(nn_attrs) - np.array([6.76717678e+05, 2.91038305e-10, 2.18278728e-11, -1.74622983e-10])))
            f_nn3.write(str(nn_attrs+[prob])+'\n')

    f_cluster.close()
    f_nn1.close()
    f_nn2.close()
    f_nn3.close()

