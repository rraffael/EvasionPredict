from flask import Flask
from flask_restplus import Resource, Api
from prediction_controller import PredictionController
app = Flask(__name__)                  #  Create a Flask WSGI application
api = Api(app)                         #  Create a Flask-RESTPlus API

@api.route('/Prediction')                   #  Create a URL route to this resource
class predict:                         #  Create a RESTful resource
    def get(self):                     #  Create GET endpoint
        result = PredictionController().validation()
        return {'Accuracy': 'world'}

if __name__ == '__main__':
    app.run(debug=True)                #  Start a development server