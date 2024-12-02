import manipulacaoStrings

palavra = input('Digite um palavra: ')

while True:
  continuar = input("""
  1 - Inverter palavra
  2 - Números de letras na palavra
  3 - Verificar se é um palidromo
  * - Sair
  """)
  
  if continuar == '1':
    palavraInvertida = manipulacaoStrings.inverterString(palavra)
    print(palavraInvertida)
  elif continuar == '2':
    numeroLetras = manipulacaoStrings.numeroLetras(palavra)
    print(numeroLetras)
  elif continuar == '3':
    palavraPalidromo = manipulacaoStrings.palavraPalidromo(palavra)
  elif continuar == '*':
    print("Programa encerrado!")
    break
  else:
    print('Opção inválida. Digite S para sair ou alguma função válida')