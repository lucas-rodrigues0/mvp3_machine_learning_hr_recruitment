import pickle


class Pipeline:
    """Load a pipeline with a preprocessor and a ML model"""

    def load_pipeline(path):

        with open(path, "rb") as file:
            pipeline = pickle.load(file)

        return pipeline
