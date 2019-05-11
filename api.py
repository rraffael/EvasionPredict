from flask import Flask
from flask import jsonify
from prediction_controller import PredictionController
app = Flask(__name__)                  #  Create a Flask WSGI application

                       
@app.route('/Prediction')                           #  Create a URL route to this resource         
def accuracy():                                     #  Create GET endpoint
    result = PredictionController().validation()
    answer = (str(result) + "%")
    return jsonify(Evasion = answer)

if __name__ == '__main__':
    app.run(debug=True)                #  Start a development server