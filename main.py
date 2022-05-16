while True:
  lado = float(input('Digite um número: ')) 

  print('Nesses casos, o valor dado aparece como cateto: \n')

  #Teste Catetos:
  if lado % 2 == 0:  #A paridade do lado é relevante
    for i2 in range(1, (int((lado/2)**0.5)+1)):
      i=lado/i2/2
      if i % 1 == 0:
        lado2=i*i-i2*i2
        lado3=i*i+i2*i2        
        print(lado, lado2, lado3)
  else:
    for i2 in range(1, (int(lado/2) + 1)):
      i=(lado+i2*i2)**0.5
      if i % 1 == 0:
        lado2=2*i*i2
        lado3=i*i+i2*i2
        print(lado, lado2, lado3)

  print('\nNesses casos, o valor dado aparece como hipotenusa: \n')

  #Teste Hipotenusa:
  for i2 in range(1, (int((lado/2)**0.5)+1)):
    i=(lado-i2*i2)**0.5     
    if i % 1 == 0:
      lado2=2*i*i2
      lado3=i*i-i2*i2
      print(lado2, lado3, lado)