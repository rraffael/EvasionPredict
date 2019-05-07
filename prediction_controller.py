import pandas as pd

class PredictionController:
    #Empty constructor
    def __init__(self):
        pass

    def validation(self):
        # File reading
        db = pd.read_csv('test.csv')

        # Variable association with column attribute and results home,busca,logado,comprou
        X_db = db[['attribute_column_1','atribute_column_2', 'attribute_column_3']]
        Y_db = db['result_column']

        # Converting categorical columns into binary columns and excluding labels
        X = (pd.get_dummies(X_db)).values
        Y = (Y_db).values

        # Percentage utilizated in treining/test
        training_percentage = 0.8
        test_percentage = 0.1 # The missing 10% will be attributed in validation later
        # Sizes
        training_size = int(training_percentage * len(Y))
        test_size = int(test_percentage * len(Y))
        total_size = training_size + test_size

        # Training data and markups
        training_data = X[:training_size]
        training_markups = Y[:training_size]
        # Test data and markups
        test_data = X[training_size:(total_size)]
        test_markups = Y[training_size:(total_size)]
        # Validation data and markups
        validation_data = X[total_size:]
        validation_markups = Y[total_size:]

        #Using the model_accuracy definition in AccuracyPrediction to get accuracy rate
        from sklearn.naive_bayes import MultinomialNB
        multinomialModel = MultinomialNB()
        multinomialAccuracy = auxiliar_methods().model_fit_and_predict(multinomialModel, training_data, training_markups, test_data, test_markups)

        from sklearn.ensemble import AdaBoostClassifier
        adaBoostModel = AdaBoostClassifier()
        adaBoostAccuracy = auxiliar_methods().model_fit_and_predict(adaBoostModel, training_data, training_markups, test_data, test_markups)

        #Chosing the model with higher accuracy
        if multinomialAccuracy > adaBoostAccuracy:
            winner =  multinomialModel
        else:
            winner = adaBoostModel

        #Real test with the more accurate model
        test = auxiliar_methods().model_predict(winner, validation_data, validation_markups)
        return test