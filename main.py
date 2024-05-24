import random
from sre_constants import REPEAT, REPEAT_ONE

print("______________________________________________________________________")
print("                   Bem vindo ao jogo da advinhação")
print("______________________________________________________________________")

print("Você quer jogar na dificuldade dificil, mediano ou fácil?")
dificuldade = input("(d,m,f)\n")
tentativas_maximas = 5

if dificuldade == "d":
  tentativas_maximas = 3
elif dificuldade == "m":
  tentativas_maximas = 5
elif dificuldade == "f":
  tentativas_maximas = 10
else:
  print("Você não definiu a dificuldade, sua dificuldade foi alterada para mediano")

numero_secreto = random.randint(1, 50)
tentativas = 1

while tentativas <= tentativas_maximas:
  #print(f"O número é: {numero_secreto}")
  print("Você está na tentativa", tentativas, "de", tentativas_maximas)
  numero_usuario = int(input("\nDigite o número secreto:"))
  if numero_secreto == numero_usuario:
    print("\nParabéns! Você ganhou o jogo!")
    break
  elif numero_secreto > numero_usuario:
    print("\nUm pouco mais")
  else:  #numero_secreto < numero_usuario:
    print("\nUm pouco menos")

  # Tentativas = tentativas + 1
  tentativas += 1

if tentativas > tentativas_maximas:
  print("Você perdeu! Tentativas excedidas! O número secreto era", numero_secreto)