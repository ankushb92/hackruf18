import json
import random
import copy
import numpy as np
import datetime

banks = [
    'Bank of China',
    'Toronto-Dominion Bank',
    'Credit Suisse',
    'Deutsch Bank',
    'Royal Bank of Canada',
    'JP Morgan & Chase',
    'BNY Mellon',
]

instruments = [
    'AMGGF',
    'QTT',
    'GE',
    'TREE',
    'GOLD',
    'NAT. GAS',
    'QSDBI US DIV IDX',
    'MSCI USA IDX',
    'RUSSEL 3000 IDX',
    'S&P 1500 IDX',
    'SOYBEAN',
    'COAL'
]
    

class Faker:

    def __init__(self, user_type=1):
        self.user_type = user_type #1 is low age, high risk guy, 2 is mid age mid risk guy, 3 is high age low risk guy
        if self.user_type == 1:
            self.age_mean = 27
            self.age_var = 5
            self.debit_mean = 400
            self.debit_var = 80
            self.credit_mean = 400
            self.credit_var = 80
            self.balance_mean = 50000
            self.balance_var = 20000
            self.is_LRLR = False
            self.is_LRHR = False
            self.is_HRLR = False
            self.is_HRHR = True
            self.transaction_count_mean = 200
            self.transaction_count_var = 20
            self.holding_count_mean = 20
            self.holding_count_var = 5
        elif self.user_type == 2:
            self.age_mean = 40
            self.age_var = 7
            self.debit_mean = 200
            self.debit_var = 50
            self.credit_mean = 500
            self.credit_var = 100
            self.balance_mean = 500000
            self.balance_var = 100000
            self.is_LRLR = False
            self.is_LRHR = True
            self.is_HRLR = False
            self.is_HRHR = False
            self.transaction_count_mean = 100
            self.transaction_count_var = 10
            self.holding_count_mean = 30
            self.holding_count_var = 5
        elif self.user_type == 3:
            self.age_mean = 55
            self.age_var = 7
            self.debit_mean = 50
            self.debit_var = 20
            self.credit_mean = 200
            self.credit_var = 50
            self.balance_mean = 500000
            self.balance_var = 200000
            self.is_LRLR = True
            self.is_LRHR = False
            self.is_HRLR = False
            self.is_HRHR = False
            self.transaction_count_mean = 50
            self.transaction_count_var = 5
            self.holding_count_mean = 50
            self.holding_count_var = 5
    def fake_transaction_history(self):
        transaction_json_string = '{"transaction":[{"CONTAINER":"bank","id":2829798,"amount":{"amount":0,"currency":"USD"},"runningBalance":{"amount":' +  str(np.random.normal(loc=self.balance_mean, scale=self.balance_var)) + ',"currency":"USD"},"baseType":"DEBIT","categoryType":"INCOME","categoryId":17,"category":"Loans","categorySource":"SYSTEM","highLevelCategoryId":10000004,"date":"2014-07-01","createdDate":"2014-07-01T13:42:35Z","lastUpdated":"2014-07-01T13:42:35Z","postDate":"2014-07-01","description":{"original":"ACH Withdrawal-Debit XXXXXXXX00 - PPD US BANK - LOAN A BILL PAYMT","consumer":"My Loan Payment","simple":"U.S. Bank Loan"},"isManual":false,"status":"POSTED","accountId":836726,"type":"PAYMENT","subType":"LOAN","merchant":{"id":"u.s.bank","source":"FACTUAL","name":"U.S. Bank","categoryLabel":["Loans"],"address":{"address1":"4160 Mission St","city":"San Francisco","state":"CA","country":"USA","zip":94112}}}]}'
        transaction_json_dict = json.loads(transaction_json_string)
        transaction_count = int(np.random.normal(loc=self.transaction_count_mean, scale=self.transaction_count_var))
        date = None
        def new_date(date):
            return date + datetime.timedelta(random.randint(5, 20), random.randint(6000, 12000)) if date else datetime.datetime(2012, 1, 1)
        for _ in range(transaction_count):
            new_transaction = copy.deepcopy(transaction_json_dict['transaction'][-1])
            previous_transaction = transaction_json_dict['transaction'][-1]
            category_type = random.choice(['EXPENSE', 'INCOME'])
            new_transaction['categoryType'] = category_type
            new_transaction['description']['simple'] = random.choice(banks)
            date = new_date(date)
            new_transaction['date'] = new_transaction['createdDate'] = new_transaction['lastUpdated'] = new_transaction['postDate'] = date
            if category_type == 'EXPENSE':
                new_transaction['amount']['amount'] = np.random.normal(loc=self.debit_mean, scale=self.debit_var)
                running_balance = previous_transaction['runningBalance']['amount'] - new_transaction['amount']['amount']
            else:
                new_transaction['amount']['amount'] = np.random.normal(loc=self.credit_mean, scale=self.credit_var)
                running_balance = previous_transaction['runningBalance']['amount'] + new_transaction['amount']['amount']
            if running_balance < 0:
                category_type = 'INCOME'
                new_transaction['amount']['amount'] = np.random.normal(loc=self.credit_mean, scale=self.credit_var)
                new_transaction['categoryType'] = category_type
                running_balance = previous_transaction['runningBalance']['amount'] + new_transaction['amount']['amount']
            new_transaction['runningBalance']['amount'] = running_balance
            transaction_json_dict['transaction'].append(new_transaction)
        return transaction_json_dict



    def fake_holdings(self):
        holding_type = "Low Risk Low Reward" if self.is_LRLR else ("Low Risk High Reward" if self.is_LRHR else ("High Risk Low Reward" if self.is_HRLR else "High Risk High Reward"))
        if random.random() < 0.2:
          holding_type = random.choice(["Low Risk Low Reward", "Low Risk High Reward", "High Risk Low Reward", "High Risk High Reward"])
        holding_json_string = '{"holding":[{"id":1347615,"accountId":1111496500,"providerAccountId":12345,"costBasis":{"amount":2500,"currency":"USD"},"cusipNumber":999999999,"securityType":"MUTUAL_FUND","matchStatus":"PUBLIC","description":"IBM stocks","holdingType":"stock","price":{"amount":2500,"currency":"USD"},"quantity":200,"symbol":"IBM","value":{"amount":500000,"currency":"USD"},"assetClassification":[{"classificationType":"Style","classificationValue":"' + holding_type + '","allocation":100},{"classificationType":"Country","classificationValue":"US","allocation":100}]}]}'
        holding_json_dict = json.loads(holding_json_string)
        holding_count = int(np.random.normal(loc = self.holding_count_mean, scale = self.holding_count_var)) 
        for _ in range(holding_count):
            new_holding = copy.deepcopy(holding_json_dict['holding'][-1])
            holding_amount = np.random.normal(loc=75, scale=30)
            holding_quantity = np.random.normal(loc=50, scale=20)
            new_holding['costBasis']['amount'] = holding_amount
            new_holding['price']['amount'] = holding_amount
            new_holding['description'] = random.choice(instruments)
            new_holding['quantity'] = holding_quantity
            new_holding['value']['amount'] = holding_quantity * holding_amount
            new_holding['assetClassification'][0]['classificationValue'] = holding_type
            holding_json_dict['holding'].append(new_holding)
        return holding_json_dict


if __name__ == '__main__':
    num = 100
    fw = [open('1.json', 'w'), open('2.json', 'w'), open('3.json', 'w')]
    for i in range(3*num):
        user = i%3 + 1
        faker = Faker(user)
        fw[user-1].write(json.dumps(faker.fake_transaction_history())+'\n')
        fw[user-1].write(json.dumps(faker.fake_holdings())+'\n')
    fw[0].close()
    fw[1].close()
    fw[2].close()
