import random
import json

class TransactionParser:

    def __init__(self, json_transactions, age, is_string=False):
        if is_string:
            self.transactions = json.loads(json_transaciton)
        else:
            self.transactions = json_transaction
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

            pass
        transaction_length = len(self.transactions['transaction'])
        attr_list = [age, self.transactions['transaction'][-1]['runningBalance']['amount'], transaction_length, debit_sum, credit_sum, lrlr_sum, lrhr_sum, hrlr_sum, hrhr_sum]

    def get_neural_net_attrs(self):
        pass
