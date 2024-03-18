# Exercício 1: apresentação do tipo de dado lista

# Criar nossa lista de dados
myFruitList = ["apple", "banana", "cherry"]

# Exibir dados da lista
print(f'LISTA: {myFruitList}')

# Exibir tipo do dados
print(type(myFruitList))

# Exibir apenas o dado na posição desejada
print(myFruitList[0])

# Alterar dado na posicao desejada, dados mutáveis // permite alterações

myFruitList[2] = "Laranja"

print(f'ALTERADO: {myFruitList}')

# Exercício 2: apresentação do tipo de dado tupla

# Criar nossa tupla
myFinalAnswerTuple = ("apple", "banana", "pineapple")

# Exibir dados da tupla
print(myFinalAnswerTuple)

# Acessar posicao na tupla
print(myFinalAnswerTuple[1])

# TUPLA NÃO PERMITE ALTERACAO DAS INFORMACOES DECLARADAS

# Alterar valor da tupla
# myFinalAnswerTuple[2] = "Abacaxi"

# Exibir alteracao
print(myFinalAnswerTuple)

# Exercício 3: apresentação do tipo de dado dicionário

# Criar dicionário
myFavoriteFruitDictionary = {
    "Akua": "apple",
    "Saanvi": "banana",
    "Paulo": "pineapple"
}

# Exibir dados do dicionario
print(myFavoriteFruitDictionary)

# Acessar valores atraves das chaves
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Paulo"])
print(myFavoriteFruitDictionary["Saanvi"])
