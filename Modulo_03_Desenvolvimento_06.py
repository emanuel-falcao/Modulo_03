'''
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará,
no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e
continuará perguntando até que um valor correto seja preenchido.

Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto
no campo ao lado para que outros desenvolvedores possam analisá-lo.

'''
print('Calcula Idade')
nome = input("Digito seu nome: ")
invalido = True
while (invalido):
    try:
        ano = int(input("Digite o seu ano de nascimento, entre 1922 e 2021: "))
        if (ano < 1921 or ano > 2021):
            raise Exception("Ano fora da faixa")
        else:
            invalido = False

    except Exception as err:
        print("Ano invalido, digite novamente.")
        print(err)

idade = (2022 - ano)
print(f'{nome} sua idade é: {idade}')
print("Fim do programa")