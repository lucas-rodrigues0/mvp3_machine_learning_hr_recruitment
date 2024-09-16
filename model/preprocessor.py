from sklearn.model_selection import train_test_split
import pickle
import numpy as np


class PreProcessor:

    def split_test_train(self, dataset, test_percentage, seed=7):

        X_train, X_test, Y_train, Y_test = self.__set_holdout(dataset, test_percentage, seed)

        return (X_train, X_test, Y_train, Y_test)
    
    def __set_holdout(self, dataset, test_percentage, seed):

        data = dataset.values

        X = data[:, 0:-1]
        Y = data[:, -1]
        return train_test_split(X, Y, test_size=test_percentage, randon_state=seed)
    
    def set_form(form):

        X_input = np.array([form.age,
                            form.gender,
                            form.education_level,
                            form.xp_years,
                            form.prev_cia_worked,
                            form.dist_cia,
                            form.interview_score,
                            form.skill_score,
                            form.personality_score,
                            form.recruitment_strategy
                        ])
        
        X_input = X_input.reshape(1, -1)
        return X_input
    
    def scaler(X_train):

        scaler = pickle.load('machine_learning\scalers\standard_scaler_recruitment.pkl', 'rb')
        rescaled_X_train = scaler.transform(X_train)
        return rescaled_X_train