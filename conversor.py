def convertor(c):
  p= c * 0.39
  file = open('resultado.txt', 'w+')
  file.write(f'o valor {c} em centímetros corresponde a {p} valor em polegadas.')
  file.close
