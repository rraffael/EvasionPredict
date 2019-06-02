from flask import Flask
from flask import jsonify
from prediction_controller import PredictionController
app = Flask(__name__)                  #  Create a Flask application

                       
@app.route('/Prediction/<origem>/<prouni>/<tipo_ingresso>/<sexo>/<idade>')                           #  Create a URL route to this resource         
def accuracy_student(origem, prouni, tipo_ingresso, sexo, idade):                                #  Create GET endpoint
    prediction = PredictionController()
    result = prediction.validation(origem, prouni, tipo_ingresso, sexo, idade)

    answer = str(result[0])
    return jsonify(Evasao = answer)

@app.route('/Prediction/HitRate')                           #  Create a URL route to this resource         
def accuracy_hit_rate():                                     #  Create GET endpoint
    result = PredictionController().hit_rate()
    
    answer = (str(result) + "%")
    return jsonify(Evasion = answer)

if __name__ == '__main__':
    app.run(debug=True)                #  Start a development server