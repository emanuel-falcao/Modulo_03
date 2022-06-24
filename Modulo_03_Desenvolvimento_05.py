'''

Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando 
infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de 
operações:
1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar. 

'''

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
    if (op >4)    :
        print ("Essa opção não existe")
sair = True
while(sair):
    print ("Calculadora:")
    num1 = float(input("Digite o primeiro Numero: "))        
    num2 = float(input("Digite o segundo Numero: "))
    op = int(input("""Digite a Opreação:
                1 - Soma
                2 - Subração
                3 - Multiplicação
                4 - Divisão
                0 - Sair
                \n"""))

    if (op == 0):
        print("Programa Finalizado")
        sair = False

    final = Calculadora(num1, num2, op)
    print(f'O Resultado do Cálculo: {final}')