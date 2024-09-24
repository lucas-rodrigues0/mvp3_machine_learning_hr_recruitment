from sklearn.metrics import accuracy_score
from model.ml_model import MLmodel


class Evaluator:
    """Evaluate the model prediction based in accuracy score."""

    def evaluation(model, X_test, Y_test):

        prediction = MLmodel.predictor(model, X_test)

        return accuracy_score(Y_test, prediction)
