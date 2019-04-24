import pandas as pd
from collections import Counter

class AccuracyPrediction:
    #Empty constructor
    def __init__(self):
        pass
        
    #Method that return the base hit rate
    def base_accuracy(markings):
        base_hit = max(Counter(markings).values())
        base_hit_rate = 100.0 * base_hit / len(markings)
        return base_hit_rate

    #Method that fit and predict the model hit rate
    def model_fit_and_predict(model, training_data, training_markups, test_data, test_markups):
        model.fit(training_data, training_markups)

        result = model.predict(test_data)

        #Where the results have the same value in the test_markups
        hits = result == test_markups

        total_hits = sum(hits)
        total_elements = len(test_data)
        #Turning into percentage
        hit_rate = 100.0 * total_hits / total_elements

        return hit_rate

    #Method that predict the model hit_rate
    def model_predict(model, validation_data, validation_markups):
        result = model.predict(validation_data)
        hits = result == validation_markups

        total_hits = sum(hits)
        total_elements = len(validation_markups)

        hit_rate = 100.0 * total_hits / total_elements

        return hit_rate