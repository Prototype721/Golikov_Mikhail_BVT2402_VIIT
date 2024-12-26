# Задание 2
def describe_person(name, age=30): print(f'Имя - {name} \nВозраст - {age}')

# Задание 3

import math
def is_prime(number):
  if number%2 == 0 and number > 2: return False
  for i in range(3, math.ceil(number**(0.5))+1, 2):
    if number % i == 0:
      return False
  return True