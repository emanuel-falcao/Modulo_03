'''


Faça um código que execute a contagem regressiva de uma bomba, informando o número de segundos para explodir. 
Ele deverá mostrar a mensagem “iniciando contagem regressiva”, os segundos passados e, no final, a mensagem “BUM!”.

Não é necessário, mas, caso deseje tornar o sistema mais realista para que o tempo realmente passe em segundos, 
você pode usar a função time.sleep() que existe na Python (acesse o link em anexo). No entanto, é preciso adicionar 
uma biblioteca antes de executá-la.

'''

import time
cont = int(input("Digite o Numero de Segundos: "))
print ("Iniciando Contagem Regressiva")
for i in range(cont+1):
    print(i)
    time.sleep(1)
print("BUM!")