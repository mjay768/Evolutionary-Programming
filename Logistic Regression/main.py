import numpy as np
import random
import matplotlib.pyplot as plt

#input array/data
data = np.array([[1,1,-1],[1,2,1],[1,3,-1],[1,4,1],[1,5,-1],[1,6,1],[1,7,1],[1,8,1]])
x = data[:,[0,1]]
y = data[:,[-1]]

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array()
test_x = np.array([[1,1.5], [1,2.5], [1,3.5], [1,4.5], [1,5.5], [1,6.5],[1,7.5]])

class LogisticRegression:

    lr = 0.0001
    input = []
    def __init__(self, weights, passes):
        self.weights = weights
        self.passes = passes

    def init_weight(self):
        w = []
        for i in range(self.weights):
            w.append(random.randint(0,1))
        print("initial weights : " + str(w))
        return w

    def summation(self,x,w):
        sum = 0
        for j in range(0, len(x)):
             for i in range(0, len(x[0])):
                 sum += w[i] * x[j][i]

        return sum

    def logit(self, x, w):
        sum = self.summation(x,w)
        return 1 / (1 + np.exp(-sum))

    def update_weights(self, x, y, w):
        print("learning rate : " + str(self.lr))
        self.plot_data(x[:,[1]], y, w, in_color = "green")
        for _ in range(0, self.passes):
            for j in range(0, len(x)):
                for i in range(0, len(x[0])):
                    sum = self.summation(x,w)
                    num = -y[j] * x[j][i]
                    den = 1 + np.exp(y[j]*sum)
                    dw = num/den
                    w[i] = w[i] - self.lr * dw

        print("updated weights : " + str(w))
        return w

    def update_weights_sgd(self, x, y, w):
        print("learning rate : " + str(self.lr))
        sum = 0
        for _ in range(0, self.passes):
            for j in range(0, len(x)):
                random_data_point = random.choice(data)
                rand_x = random_data_point[0:2]
                rand_y = random_data_point[-1]
                sum = w[0] * rand_x[0] + w[1] * rand_x[1]
                error_den = 1 + (np.exp(rand_y * (sum)))
                temp = []
                for i in range(0, len(rand_x)):
                    error_num = -rand_y * rand_x[i]
                    temp.append(error_num)
                delta_error_num = temp[0]-temp[1]
                delta_error = delta_error_num / error_den
                # print("delta_error : " + str(delta_error))
                for l in range(0, len(w)):
                    w[l] = w[l] - self.lr * delta_error

        print("updated weights sgd : " + str(w))
        return w


    def predict(self, x, w):
        y_pred = []
        for i in x:
            sum = w[0] * i[0] + w[1] * i[1]
            res = 1 / (1 + np.exp(-sum))
            y_pred.append(res)
        print("test_x : " + str(x[:,[1]]))
        print("y_pred : " + str(y_pred))
        self.plot_data(x[:,[1]], y_pred, w, in_color = "red")
        plt.show()

    def plot_data(self, x, y, w, in_color = "green"):
        plt.scatter(x, y, color= in_color)
        # plt.show()




regressor = LogisticRegression(2, 200)
w = regressor.init_weight()
regressor.summation(x,w)
# updated_weights = regressor.update_weights(x, y, w)
# regressor.predict(test_x, updated_weights)
# w = regressor.init_weight()
updated_weights_sgd = regressor.update_weights_sgd(x, y, w)
# regressor.predict(test_x, updated_weights_sgd)
