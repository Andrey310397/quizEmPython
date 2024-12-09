# Informando o usuário sobre o início do programa
print('Seja bem-vindo ao quiz do Andrey\n')

# Questionando o usuário
answer_user = input('Quer começar? (S/N) ').upper()

print('\n')

# Condição se falso
if answer_user != 'S':
    quit()
    
score = 0

print('Começando...\n')

# Quiz
# Pergunta 1
print('Quem desenvolveu o jogo Grand Thef Auto (GTA)?\n\n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA\n')
answer_1 = input('Resposta: ').upper()

if answer_1 == 'A':
    print('\nAcertou Miserávi!')
    score += 1
else:
    print('\nAííí que burro!')
    
print('\n')
    
# Pergunta 2
print('Qual o nome do protagonista do GTA San Andress?\n\n (A) Carlos Jhon \n (B) Carl Jonhson \n (C) Carl Jaqueline \n (D) Carlos Jonhson\n')
answer_2 = input('Resposta: ').upper()

if answer_2 == 'B':
    print('\nAcertou Miserávi!')
    score += 1
else:
    print('\nAííí que burro!')

# Encerramento
print(f'\nQuiz acabou... Pontuação é {score}')
    