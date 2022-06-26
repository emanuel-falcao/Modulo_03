"""
Desenvolva um código que simule uma eleição com três candidatos.
- candidato_X => 889
- candidato_Y => 847
- candidato_Z => 515
- branco => 0

O código deve perguntar se deseja finalizar a votação depois do voto. Caso o número do voto não
corresponda a nenhum candidato ou seja branco, ele deve ser tratado como nulo. Se for inserido um texto
ao invés de número, o código deve retornar uma mensagem para votar novamente.

Quando a votação for finalizada, o código deverá mostrar o vencedor, aquele com o maior número de votos
e, também, a quantidade de votos de cada candidato, os brancos e nulos """

candidato_x = 0
candidato_y = 0
candidato_z = 0
branco = 0
nulo = 0
final = "n"

while(final=="n"):
    try:
        candidato = int(input("""Digite o Numero do Candidato:
                - candidato_X => 889
                - candidato_Y => 847
                - candidato_Z => 515
                - branco => 0  \n"""))
    except:
        print("Voto Nulo")
        candidato = 666

    if (candidato == 889):
        candidato_x = candidato_x + 1
        print("voto para o Candidato X.")
    elif (candidato == 847):
        candidato_y = candidato_y + 1
        print("voto para o Candidato Y.")
    elif (candidato == 515):
        candidato_z = candidato_z + 1
        print("voto para o Candidato Z.")
    elif (candidato == 0):
        branco = branco + 1
        print("voto em branco.")
    else:
        nulo = nulo + 1

    final = input("""Fim da votação.
         Digite: 
         n - Novo Voto
         r - Resultados \n""")

    if (final == "r"):
        if candidato_x > candidato_y and candidato_x > candidato_z:
            print(f"Vencedor: Candidato X com {candidato_x} votos\n"
                  f"Candidato Y obteve {candidato_y} votos\n"
                  f"Candidato Z obteve {candidato_z} votos\n")
        elif candidato_y > candidato_x and candidato_y > candidato_z:
            print(f"Vencedor: Candidato Y com {candidato_y} votos\n"
                  f"Candidato X obteve {candidato_x} votos\n"
                  f"Candidato Z obteve {candidato_z} votos\n")
        elif candidato_z > candidato_x and candidato_z > candidato_y:
            print(f"Vencedor: Candidato Z com {candidato_z} votos\n"
                  f"Candidato X obteve {candidato_x} votos\n"
                  f"Candidato Y obteve {candidato_y} votos\n")
        else:
            print("Não há vencedor.")
        print(f"Votos nulos: {nulo} \nVotos em branco: {branco}")
