import pickle


class Pipeline:

    def load_pipeline(path):

        with open(path, 'rb') as file:
            pipeline = pickle.load(file)
        
        return pipeline
