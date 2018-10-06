import json
import random
import copy

class Faker:

    def __init__(self, transaction_count=100, holding_count=100):
        self.transaction_count = transaction_count
        self.holding_count = holding_count

    def fake_transaction_history(self):
        transaction_json_string = '{"transaction":[{"CONTAINER":"bank","id":2829798,"amount":{"amount":1000,"currency":"USD"},"runningBalance":{"amount":1000,"currency":"USD"},"baseType":"DEBIT","categoryType":"INCOME","categoryId":17,"category":"Loans","categorySource":"SYSTEM","highLevelCategoryId":10000004,"date":"2014-07-01","createdDate":"2014-07-01T13:42:35Z","lastUpdated":"2014-07-01T13:42:35Z","postDate":"2014-07-01","description":{"original":"ACH Withdrawal-Debit XXXXXXXX00 - PPD US BANK - LOAN A BILL PAYMT","consumer":"My Loan Payment","simple":"U.S. Bank Loan"},"isManual":false,"status":"POSTED","accountId":836726,"type":"PAYMENT","subType":"LOAN","merchant":{"id":"u.s.bank","source":"FACTUAL","name":"U.S. Bank","categoryLabel":["Loans"],"address":{"address1":"4160 Mission St","city":"San Francisco","state":"CA","country":"USA","zip":94112}}}]}'
        transaction_json_dict = json.loads(transaction_json_string)
        for _ in range(self.transaction_count):
            new_transaction = copy.deepcopy(transaction_json_dict['transaction'][-1])
            previous_transaction = transaction_json_dict['transaction'][-1]
            new_transaction['amount']['amount'] = random.randint(100,10000)
            category_type = random.choice(['EXPENSE', 'INCOME'])
            new_transaction['categoryType'] = category_type
            if category_type == 'EXPENSE':
                running_balance = previous_transaction['runningBalance']['amount'] - new_transaction['amount']['amount']
            else:
                running_balance = previous_transaction['runningBalance']['amount'] + new_transaction['amount']['amount']
            if running_balance < 0:
                category_type = 'INCOME'
                new_transaction['categoryType'] = category_type
                running_balance = previous_transaction['runningBalance']['amount'] + new_transaction['amount']['amount']
            new_transaction['runningBalance']['amount'] = running_balance
            transaction_json_dict['transaction'].append(new_transaction)
        return json.dumps(transaction_json_dict)



    def fake_holdings(self):
        holding_json_string = '{"holding":[{"id":1347615,"accountId":1111496500,"providerAccountId":12345,"costBasis":{"amount":2500,"currency":"USD"},"cusipNumber":999999999,"securityType":"MUTUAL_FUND","matchStatus":"PUBLIC","description":"IBM stocks","holdingType":"stock","price":{"amount":2500,"currency":"USD"},"quantity":200,"symbol":"IBM","value":{"amount":500000,"currency":"USD"},"assetClassification":[{"classificationType":"Style","classificationValue":"Low Risk Low Reward","allocation":100},{"classificationType":"Country","classificationValue":"US","allocation":100}]}]}'
        holding_json_dict = json.loads(holding_json_string)
        for _ in range(self.holding_count):
            new_holding = copy.deepcopy(holding_json_dict['holding'][-1])
            holding_amount = random.randint(10,150)
            holding_quantity = random.randint(10, 100)
            new_holding['costBasis']['amount'] = holding_amount
            new_holding['price']['amount'] = holding_amount
            new_holding['quantity'] = holding_quantity
            new_holding['value']['amount'] = holding_quantity * holding_amount
            holding_json_dict['holding'].append(new_holding)
        return json.dumps(holding_json_dict)


f = Faker()
print(f.fake_holdings())

