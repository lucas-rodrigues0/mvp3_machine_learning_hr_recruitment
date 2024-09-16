from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from model.ml_model import MLmodel


class Evaluator:

    def evaluation(self, model, X_test, Y_test):

        prediction = MLmodel.predictor(model, X_test)

        return accuracy_score(Y_test, prediction)
