'''

Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e 
o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0

'''
print ("Calculadora")

def Calculadora(num1,num2, op):
    if (op == 1):
        res = num1 + num2
        return res
    if (op == 2):
        res = num1 - num2
        return res
    if (op == 3):
        res = num1 * num2
        return res
    if (op == 4):
        if (num2 == 0):
            print ("Não é possível dividir por 0")
        else:
            res = num1 / num2
            return res
    if (op == 0 or op >4)    :
        res = 0
        return res

num1 = float(input("Digite o primeiro Numero: "))        
num2 = float(input("Digite o segundo Numero: "))
op = int(input("""Digite a Opreação:
                1 - Soma
                2 - Subração
                3 - Multiplicação
                4 - Divisão\n"""))

final = Calculadora(num1, num2, op)
print(f'O Resultado do Cálculo: {final}')


