# EvasionPredict

This project was made as the conclusion course project in University Tiradentes, Sistemas para Internet. While using tons of data to evaluate the IA so it can try to predict if a student will evade or not the course, before it does. While doing this, is expectated that actions can be made to prevent it, as the percentage of evasion in some courses like TI Courses is high and need prevemption.

### Objectives

- Get the predicted answer if a student will evade or not.
- Have a 80% + accuracy.
- Possibilitate to try prevempting some students to evade before they do.

## Getting Started

As instruções abaixo mostra como instalar e fazer o projeto rodar, obtendo os resultados esperados.

### Prerequisites

- Python 3.

### Installing

1 - Download this project.
2 - Unzip it.
3 - Download Python 3.
  Go to the link https://www.python.org/downloads/ and get the most recent version.
4 - Install it into your machine.
### Testing

-- Windows --
1 - Open your CMD.
2 - Go to the api.py file directory downloaded in this project.
3 - Type "python apy.py" in your CMD and press enter.
4 - Fill the data as the route and parameter needs.
5 - Type the route to get some answers.
5.1 - "/Prediction/HitRate" to get the actual hit rate of the application.
5.2 -"/Prediction/{Origem}/{Prouni}/{TipoDeIngresso}/{Sexo}/{Idade}/{Nota1Unidade}" to get the prediction of the result as "Sim/Yes" or "Não/No" in json format.

### Results

Architecture Diagram:

![ArchDiagram](https://user-images.githubusercontent.com/27858619/112488767-c1f9dd80-8d75-11eb-823f-d5c8ff81f9af.png)

Prediction Accuracy API return:

![Predict Accuracy](https://user-images.githubusercontent.com/27858619/112488506-7d6e4200-8d75-11eb-883b-e30faf45a56e.png)

Sample API return

![Sample](https://user-images.githubusercontent.com/27858619/112488525-819a5f80-8d75-11eb-8f8c-903d133f399a.png)

## Built With

* [Pandas] (https://pandas.pydata.org/) - Data data analysis tools library used.
* [Scikit-Learn] (https://scikit-learn.org/) - Machine learning library used.
* [NumPy] (https://numpy.org/) - Scientific package used.
* [Flask] (https://palletsprojects.com/p/flask/) - Mini-framework used to develop as an api.

## Authors

* **Raffael de Castro Rodrigues**

## License
This project is licensed under the BSD License - see the LICENSE file for details
