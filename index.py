#Variaveis que recebe o nome e quantidade de experiencia recebida pelo usuario
print("---------------CLASSIFICADOR DE NIVEL DE HERÓI-----------------")
nome = (input("Digite o nome do herói e tecle ENTER: "))
xp = (int(input("Digite a quantidade de xp possuida e tecle ENTER: ")))

#Estrutura de decisão do rank de acordo com a quantidade de xp
if xp < 1000:
    mensagem = "Ferro"
elif 1000 <= xp <= 2000:
    mensagem = "Bronze"
elif 2001 <= xp <= 5000:
    mensagem = "Prata"
elif 6001 <= xp <= 7000:
    mensagem = "Ouro"
elif 7001 <= xp <= 8000:
    mensagem = "Platina"
elif 8001 <= xp <= 9000:
    mensagem = "Ascendente"
elif 9001 <= xp <= 10000:
    mensagem = "Imortal"
else:
    mensagem = "Radiante"

# Exibir a mensagem correspondente a classificação

print(f"O heroi de nome {nome} com {xp} de XP está no rank {mensagem}.")
