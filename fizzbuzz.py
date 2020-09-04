max_number = int(input('Por favor digite um número que você deseja fazer o fizzbuzz: '))
position = 0

while max_number > position:
  position += 1
  if position % 3 == 0 and position % 5 == 0:
    print('Fizzbuzz')
  elif position % 3 == 0:
    print('Fizz')
  elif position % 5 == 0:
    print('Buzz')
  else:
    print(position)