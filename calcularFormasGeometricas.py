import math

def calcularQuadradoArea(lado):
  return f'A área do quadrado é {lado * 2}'
  
def calcularQuadradoPerimetro(lado):
  return f'O perímetro do quadrado é {lado * 4}'

def calcularRetanguloArea(base, altura):
  return f'A área do retangulo é {base * altura}'

def calcularRetanguloPerimetro(base, altura):
  return f'O perímetro do retangulo é {(2 * base) + (2 * altura)}'

def calcularCirculoArea(raio):
  resultado = math.floor(math.pi * (raio * raio))
  return f'A área do círculo é {resultado}'

def calcularCirculoPerimetro(raio):
  return f'O perímetro do círculo é {2 * math.pi * raio}'

def calcularTrianguloArea(base, altura):
  return f'A área do triangulo é {(base * altura) / 2}'

def calcularTrianguloPerimetro(lado1, lado2, lado3):
  return f'O perímetro do triângulo é {lado1 + lado2 + lado3}'

while True:
  print('Digite a Função desejada')
  continuar = input("""
  1 - Calcular área do quadrado
  2 - Calcular perímetro do quadrado
  3 - Calcular área do retângulo
  4 - Calcular perímetro do retângulo
  5 - Calcular área do círculo
  6 - Calcular perímetro do círculo
  7 - Calcular área do triângulo
  8 - Calcular perímetro do triângulo
  * - Sair
""")
  
  if continuar == '1':
    ladoQuadrado = input('Digite o tamanho do lado: ')
    resultado = calcularQuadradoArea(float(ladoQuadrado))
    print(resultado)
  elif continuar == '2':
    ladoQuadrado = input('Digite o tamanho do lado: ')
    resultado = calcularQuadradoPerimetro(float(ladoQuadrado))
    print(resultado)
  elif continuar == '3':
    baseRetangulo = input('Digite a base do retângulo: ')
    alturaRetangulo = input('Digite a altura do retângulo: ')
    resultado = calcularRetanguloArea(float(baseRetangulo), float(alturaRetangulo))
    print(resultado)
  elif continuar == '4':
    baseRetangulo = input('Digite a base do retângulo: ')
    alturaRetangulo = input('Digite a altura do retângulo: ')
    resultado = calcularRetanguloArea(float(baseRetangulo), float(alturaRetangulo))
    print(resultado)
  elif continuar == '5':
    raioCirculo = input('Digite o raio do círculo: ')
    resultado = calcularCirculoArea(float(raioCirculo))
    print(resultado)
  elif continuar == '6':
    raioCirculo = input('Digite o raio do círculo: ')
    resultado = calcularCirculoPerimetro(float(raioCirculo))
    print(resultado)
  elif continuar == '7':
    baseTriangulo = input('Digite a base do triângulo: ')
    alturaTriangulo = input('Digite a altura do triângulo: ')
    resultado = calcularTrianguloArea(float(baseTriangulo), float(alturaTriangulo))
    print(resultado)
  elif continuar == '8':
    lado1 = input('Digite o primeiro lado do triangulo: ')
    lado2 = input('Digite o segundo lado do triangulo: ')
    lado3= input('Digite o terceiro lado do triangulo: ')
    resultado = calcularTrianguloArea(float(lado1), float(lado2), float(lado3))
    print(resultado)
  elif continuar == '*':
    print('Programa encerrado!')
    break
  else:
    print('Você digitou alguma funçaõ invalida!')