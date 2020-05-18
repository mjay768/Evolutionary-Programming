import numpy as np
import matplotlib.pyplot as plt
import random

features = [1, 2, 3, 4, 5, 6, 7, 8]
labels = [0, 1, 0, 1, 0, 1, 1, 1]


class LRegression:
    def __init__(self, weights, passes):
        self.weights = weights
        self.passes = passes

    def initializews(self):
        weights = []
        for i in range(self.weights):
            weights.append(random.randint(0, 2))
        print(weights)
        return weights

    def sigmoid(self, scores):
        return 1 / (1 + np.exp(-scores))

    def log_likelihood(self, features, weights, labels):
        scores = np.dot(features, weights)
        return np.sum(labels * scores - np.log(1 + np.exp(scores)))

    def gradient(self, features, error):
        return np.dot(features, error) / np.size(features)

    def predict(self, predictions, threshold):
        return predictions >= threshold

    def logistic_regression(feature, labels, epochs, step_size, predictions, gradient):
        for i in range(epochs):
            score = np.dot(feature, weights)
            error = labels - predictions

            # print(predictions,score,error)
            # print(predictions)
            # print(score)
            # print(error)
            # gradient_ = np.dot(feature,error)/8
            # print('Gradients',gradient_)
            # print(int(predict(predictions,0.01)))
            weights = weights - (step_size * gradient_)
            # print('Weights',weights)
            # classified_data =  predict(predictions,1)
            # print(classified_data)
        return weights


obj = LRegression(2, 20)

init_weights = obj.initializews()
scores = np.dot(features, init_weights)
predictions = obj.sigmoid(scores)
gradient_ = gradient(feature, error)
weights = obj.logistic_regression(features, labels, 100, 0.001, predictions)
print(weights)
# classified_data = predict(weights,0.5)
# print(classified_data)

plt.scatter(features, labels, color="red")
plt.plot(weights)
plt.show()
