import random
import numpy

class Recommender:

    def __init__(self, difference_vector):
        self.attributes = ['Low Risk Low Reward', 'Low Risk High Reward', 'High Risk Low Reward', 'High Risk High Reward']
        self.dimensions = len(self.attributes)
        self.difference_vector = difference_vector
        self.suggestions = {}
        self.suggestions[self.attributes[0]] = ["Treasury Bonds","Muncipal Bonds","Inflation Protected Bonds","Fixed Deposits"]
        self.suggestions[self.attributes[1]] = ["Treasury Bonds","Muncipal Bonds","Inflation Protected Bonds","Fixed Deposits"]
        self.suggestions[self.attributes[2]] = ["Index Funds","ETFs","Derivatives","Futures"]
        self.suggestions[self.attributes[3]] = ["Stocks","Options","Cryptocurrencies"]

    def get_recommendation_ordinal(self):
        for i in range(self.dimensions):
            self.difference_vector[i] = abs(self.difference_vector[i])
        pair_vectors = list(zip(self.difference_vector, self.attributes))
        pair_vectors.sort(reverse=True)
        self.pair_vectors = pair_vectors

    def get_word_repr(self, words):
        if len(words) == 1:
            return words[0]
        return ", ".join(words[:-1]) + " and " + words[-1]

    def get_recommendation_url(self):
        return "http://personalized_url_portfolio_recommendation.com/bussiness/model/"

    def get_recommendation_string(self):
        resp = "We noticed that you have a very few investments in the " + self.pair_vectors[0][1] + " category. This was found using a learning algorithm based on multiple individuals who have similar financial characteristics as you. We recommend investing in items like " + self.get_word_repr(self.suggestions[self.pair_vectors[0][1]]) + ". We also found that your second weakest investment group is " + self.pair_vectors[1][1] + ", for which we recommend investing in " + self.get_word_repr(self.suggestions[self.pair_vectors[1][1]]) + "."
        return resp


    def get_recommendation(self):
        self.get_recommendation_ordinal()
        response = self.get_recommendation_string()
        url = self.get_recommendation_url()
        return (response, url)
