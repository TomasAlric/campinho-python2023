"""
Listar numeros primos
"""

# listar os numeros primos de 1 a 250
numerosPrimos = [3]


# estrutura de repeticao
for i in range(1, 251):
# verificar se o numero é primo
# numero primo são aqueles que apresentam dois divisores
# um e o proprio numero
    #print(i)
    
    # verificar se é divisivel
    # condicional
    if i > 1:
        for j in range(2, i):
            if(i % j == 0):
                break # finaliza a execucao
        else:
            #print(i)
            numerosPrimos.insert(0, i)

# criar o arquivo    
file = "/Users/viih/Desktop/campinho-python/campinho/day-7/numbers.txt"

# escrever no arquivo
with open(file, "w") as f:
    numerosPrimos.reverse()
    
    # ler numero por numero
    for n in numerosPrimos:
        # inserir numeros no arquivo
        f.write(str(n) + ', ')

# ler o arquivo
with open(file, "r") as arquivo:
    print(arquivo.read())

