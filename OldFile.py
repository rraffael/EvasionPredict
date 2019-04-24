import pandas as pd
from collections import Counter

# teste inicial: home, busca, logado => comprou
# home, busca
# home, logado
# busca, logado
# busca: 85,71% (7 testes)

#Leitura do arquivo, atribuição das colunas variaveis/resultados em X_df/Y_df
df = pd.read_csv('buscas2.csv')
X_df = df[['home','busca', 'logado']]
Y_df = df['comprou']

#dummies converte variáveis categóricas em colunas do tipo binário
Xdummies_df = (pd.get_dummies(X_df))
Ydummies_df = Y_df

#remove as labels e deixa apenas a data do dataframe
X = Xdummies_df.values
Y = Ydummies_df.values

#Quantos % dos dados serão utilizados para treino/teste/validação
porcentagem_treino = 0.8
porcentagem_de_teste = 0.1

tamanho_de_treino = int(porcentagem_treino * len(Y))
tamanho_de_teste = int(porcentagem_de_teste * len(Y))

# 0 até 799
treino_dados = X[:tamanho_de_treino]
treino_marcacoes = Y[:tamanho_de_treino]

fim_de_teste = tamanho_de_treino + tamanho_de_teste

#800 até 899
teste_dados = X[tamanho_de_treino:fim_de_teste]
teste_marcacoes = Y[tamanho_de_treino:fim_de_teste]

#900 até 999
validacao_dados = X[fim_de_teste:]
validacao_marcacoes = Y[fim_de_teste:]

#Método para retornar a taxa de acerto dado um modelo
def fit_and_predict(nome, modelo, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes):
    modelo.fit(treino_dados, treino_marcacoes)

    resultado = modelo.predict(teste_dados)

    acertos = resultado == teste_marcacoes

    total_de_acertos = sum(acertos)
    total_de_elementos = len(teste_dados)

    taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

    return taxa_de_acerto

#Método para realizar o teste real utilizando o modelo melhor selecionado
def teste_real(modelo, validacao_dados, validacao_marcacoes):
    resultado = modelo.predict(validacao_dados)
    acertos = resultado == validacao_marcacoes

    total_de_acertos = sum(acertos)
    total_de_elementos = len(validacao_marcacoes)

    taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos
    
    msg = "Taxa de acerto do vencedor entre os dois algoritmos no mundo real: {0}".format(taxa_de_acerto)
    print(msg)

#Importação, instanciação do modelo e utilização da função fit_and_predict para dar o resultado do modelo escolhido
from sklearn.naive_bayes import MultinomialNB
modeloMultinomial = MultinomialNB()
resultadoMultinomial = fit_and_predict("MultinomialNB", modeloMultinomial, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)

from sklearn.ensemble import AdaBoostClassifier
modeloAdaBoost = AdaBoostClassifier()
resultadoAdaBoost = fit_and_predict("AdaBoostClassifier", modeloAdaBoost, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)

#Escolha do modelo com maior taxa de sucesso
if resultadoMultinomial > resultadoAdaBoost:
    vencedor =  modeloMultinomial
else:
    vencedor = modeloAdaBoost

#Teste real com modelo melhor escolhido
teste_real(vencedor, validacao_dados, validacao_marcacoes)


# DONE IN BASEACCURACY.PY
# a eficácia do algoritmo que chuta tudo um único valor para criar uma taxa de acerto sucesso base
# acerto_base = max(Counter(validacao_marcacoes).values())
# taxa_de_acerto_base = 100.0 * acerto_base / len(validacao_marcacoes)
# print("Taxa de acerto base: %f" % taxa_de_acerto_base)
# total_de_elementos = len(validacao_dados)
# print("Total de teste: %d" % total_de_elementos)
