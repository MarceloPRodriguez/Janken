# O objetivo do código é criar um jogo de  'r', papel 'p' e tesoura 't'
#  -> usario escolhe uma opção dentre as tres disponiveis
#  -> a CPU escolhe aleatóriamente uma opção com a função 'random'
#  -> função verifica o vencedor

import random 

user_points = 0
computer_points = 0


options = ["r", "t", "p"]# cria uma lista com as opções

while True:
    user_choice = input("Escolha R(Pedra)/T(Tesoura)/P(Papel) ou Q para sair.").lower() # user escolhe uma das tres opções e converte para caixa baixa

    if user_choice == 'q': # se digitar 'Q' encerra aplicação
        break

    if user_choice not in options: # Se digitar uma opção que não está na lista repete opções até user digitar uma válida.
        continue

# Computador escolhe uma opção da sua lista ('options')
    computer_choice = random.randint(0, 2) 
    # 0 : R, 1 : T, 2 : P
    computer_option = options[computer_choice]

    print("O computador escolheu " + computer_option) # Exibe opção escolhida pelo computador

# Compara resultados 
    if user_choice == computer_option:
        print("Empate!")

    elif user_choice == "r" and computer_option == "t":
        print("Você ganhou!")
        user_points = user_points + 1

    elif user_choice == "p" and computer_option == "r":
        print("Você ganhou!")
        user_points = user_points + 1

    elif user_choice == "t" and computer_option == "p":
        print("Você ganhou!")
        user_points = user_points + 1 # verifica e atribui pontos ao user

    else:
        print("Você perdeu!")
        computer_points = computer_points + 1 # verifica e atribui pontos ao computador

# Exibe pontos do usuario e da CPU
print("Sua pontuação: " + str(user_points))
print("Pontuação do Computador: " + str(computer_points))

if computer_points > user_points:
    print("Derrota!!!!")
elif computer_points == user_points:
    print("Empate")
else:
    print("Vitória!!")