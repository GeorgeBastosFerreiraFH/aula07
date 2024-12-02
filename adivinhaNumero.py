import random


numeroAleatorio = random.randint(1, 10)
tentativas = 3

while True:
  chute = int(input('Digite um número de 1 a 10: '))
  tentativas -= 1
  if chute == numeroAleatorio:
    print(f'Você acertou o número aleatorio é {numeroAleatorio}')
  elif chute != numeroAleatorio:
    print(f'Você errou restam {tentativas} tentativas')
  elif tentativas == 3:
    print('Acabaram suas tentativas')
    break
  try:
    if chute < 1 or chute > 10:
      print('Digite um número entre 1 e 10')      
  except ValueError:
    print('Você digitou algo invalido!')
  

  if chute > numeroAleatorio:
    print('O número aleatorio é maior')
  else:
    print('O número aleatorio é menor')