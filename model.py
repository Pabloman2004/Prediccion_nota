# here we gonna train de model

from sklearn.linear_model import LinearRegression

class LinearRegressionModel:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X,y):
        self.model.fit(X, y)

    def predict(self, X):
        predictions = self.model.predict(X)
        return predictions
