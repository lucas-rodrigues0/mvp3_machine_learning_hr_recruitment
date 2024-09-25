from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from model.ml_model import MLmodel


class Evaluator:
    """Evaluate the model prediction based in metric score.
    Default metric use the accuracy score. Also can get 'recall', 'precision' and 'fscore'.
    """

    def evaluation(model, X_test, Y_test, metric="accuracy"):
        prediction = MLmodel.predictor(model, X_test)

        if metric == "fscore":
            return f1_score(Y_test, prediction)
        elif metric == "recall":
            return recall_score(Y_test, prediction)
        elif metric == "precision":
            return precision_score(Y_test, prediction)
        else:
            return accuracy_score(Y_test, prediction)
