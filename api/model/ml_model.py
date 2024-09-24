import pickle


class MLmodel:
    """Load a machine learning model and call the model predict method"""

    def load_model(path):

        if path.endswith(".pkl"):
            with open(path, "rb") as file:
                model = pickle.load(file)
        else:
            raise Exception("Invalid File Format. File must have '.pkl' extension.")

        return model

    def predictor(model, X_input):

        prediction = model.predict(X_input)

        return prediction
