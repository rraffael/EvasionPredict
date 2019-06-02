from collections import Counter

class AuxiliarMethods:
    #Empty constructor
    def __init__(self):
        pass
        
    #Method that return the base hit rate
    @classmethod
    def base_accuracy(self, markings):
        base_hit = max(Counter(markings).values())
        base_hit_rate = 100.0 * base_hit / len(markings)
        return base_hit_rate

    #Method that fit and predict the model hit rate
    @classmethod
    def model_fit_and_predict(self, model, training_data, training_markups, test_data, test_markups):
        model.fit(training_data, training_markups)

        result = model.predict(test_data)

        #Where the results have the same value in the test_markups
        hits = result == test_markups

        total_hits = sum(hits)
        total_elements = len(test_data)
        #Turning into percentage
        hit_rate = 100.0 * total_hits / total_elements

        return hit_rate

    #Method that predict the model answer
    @classmethod
    def model_predict(self, model, validation_data):
        result = model.predict(validation_data)
        return result

    #Method to transform values into binary columns as the model
    @classmethod
    def transform_values(self, origem, prouni, tpo_ingresso, sexo, idade, nota):
        # Atribui valor de origem para binário
        if origem.upper() == "AJU":
            origem_bin = [1, 0, 0]
        elif origem.upper() == "OUTROS":
            origem_bin = [0, 1, 0]
        else:
            origem_bin = [0, 0, 1] 
            
        # Atribui valor de prouni para binário
        if prouni.upper() == "S":
            prouni_bin = [1, 0]
        else:
                prouni_bin = [0, 1]

        # Atribui valor de tipo_ingresso para binário
        if tpo_ingresso.upper() == "PORTADOR_DIPLOMA":
            tpo_ingresso_bin = [1, 0, 0, 0, 0]
        elif tpo_ingresso.upper() == "PROUNI":
            tpo_ingresso_bin = [0, 1, 0, 0, 0]
        elif tpo_ingresso.upper() == "TRANSF_EXTERNA":
            tpo_ingresso_bin = [0, 0, 1, 0, 0]
        elif tpo_ingresso.upper() == "TRANSF_INTERNA":
            tpo_ingresso_bin = [0, 0, 0, 1, 0]
        else:
            tpo_ingresso_bin = [0, 0, 0, 0, 1]

        # Atribui valor de sexo para binário
        if sexo.upper() == "F":
            sexo_bin = [1, 0]
        else:
            sexo_bin = [0, 1]

        # Transforma o valor de idade para inteiro
        idade_bin = [int(idade)]

        # Transforma o valor de nota para inteiro e atribui a nota_bin
        nota = int(nota)
        if nota > 9.6:
            nota_bin = [10]
        elif nota > 8.6:
            nota_bin = [9]
        elif nota > 7.6:
            nota_bin = [8]
        elif nota > 6.6:
            nota_bin = [7]
        elif nota > 5.6:
            nota_bin = [6]
        elif nota > 4.6:
            nota_bin = [5]
        elif nota > 3.6:
            nota_bin = [4]
        elif nota > 2.6:
            nota_bin = [3]
        elif nota > 1.6:
            nota_bin = [2]
        elif nota > 0.6:
            nota_bin = [1]
        else:
            nota_bin = [0]

        # Concatena todos valores binários na ordem desejada e retorna
        result = idade_bin + origem_bin + prouni_bin + tpo_ingresso_bin + sexo_bin + nota_bin
        return result