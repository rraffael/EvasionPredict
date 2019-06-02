import pandas as pd
import numpy as np
from auxiliar_methods import AuxiliarMethods

class PredictionController:
    #Empty constructor
    def __init__(self):
        pass

    def hit_rate(self):
        # File reading
        db = pd.read_csv('Main.csv')
        
        # Variable association with column attribute and results 
        X_db = db[['IDADE','ORIGEM_AJU', 'ORIGEM_OUTROS', 'ORIGEM_SE', 'PROUNI_SIM', 'PROUNI_NAO','PORTADOR_DIPLOMA', 'PROUNI', 'TRANSF_EXTERNA', 'TRANSF_INTERNA', 'VESTIBULAR','SEXO_FEMININO', 'SEXO_MASCULINO', 'NOTA']]
        Y_db = db['SITUACAO']

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
        multinomialAccuracy = AuxiliarMethods().model_fit_and_predict(multinomialModel, training_data, training_markups, test_data, test_markups)

        from sklearn.ensemble import AdaBoostClassifier
        adaBoostModel = AdaBoostClassifier()
        adaBoostAccuracy = AuxiliarMethods().model_fit_and_predict(adaBoostModel, training_data, training_markups, test_data, test_markups)

        #Chosing the model with higher accuracy
        if multinomialAccuracy > adaBoostAccuracy:
            winner =  multinomialModel
        else:
            winner = adaBoostModel

        #Real test with the more accurate model
        result = winner.predict(validation_data)
        hits = result == validation_markups

        total_hits = sum(hits)
        total_elements = len(validation_markups)

        hit_rate = 100.0 * total_hits / total_elements
         
        return hit_rate # To get base hit_rate, change hit_rate with 'AuxiliarMethods().base_accuracy(test_markups)' 

    def validation(self, origem, prouni, tipo_ingresso, sexo, idade, nota):
        # File reading
        db = pd.read_csv('Main.csv')
        
        # Variable association with column attribute and results 
        X_db = db[['IDADE','ORIGEM_AJU', 'ORIGEM_OUTROS', 'ORIGEM_SE', 'PROUNI_SIM', 'PROUNI_NAO','PORTADOR_DIPLOMA', 'PROUNI', 'TRANSF_EXTERNA', 'TRANSF_INTERNA', 'VESTIBULAR','SEXO_FEMININO', 'SEXO_MASCULINO', 'NOTA']]
        Y_db = db['SITUACAO']

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

        #Using the model_accuracy definition in AccuracyPrediction to get accuracy rate
        from sklearn.naive_bayes import MultinomialNB
        multinomialModel = MultinomialNB()
        multinomialAccuracy = AuxiliarMethods().model_fit_and_predict(multinomialModel, training_data, training_markups, test_data, test_markups)

        from sklearn.ensemble import AdaBoostClassifier
        adaBoostModel = AdaBoostClassifier()
        adaBoostAccuracy = AuxiliarMethods().model_fit_and_predict(adaBoostModel, training_data, training_markups, test_data, test_markups)

        #Chosing the model with higher accuracy
        if multinomialAccuracy > adaBoostAccuracy:
            winner =  multinomialModel
        else:
            winner = adaBoostModel
        
        # Method to transform parameters into binary columns as the trained model 
        student =  AuxiliarMethods().transform_values(origem, prouni, tipo_ingresso, sexo, idade, nota)
        modeled_student = np.reshape(student, (1, -1))
        
        #Real test with the more accurate model
        answer = AuxiliarMethods().model_predict(winner, modeled_student)

        #Muda a reposta de 0 para Sim ou 1 para Nao
        if answer == 0:
            answer = "Sim"
        elif answer == 1:
            answer = "Nao"
        
        return answer