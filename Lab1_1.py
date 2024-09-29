# Домашнее задание по лабораторной №1 по предмету "Информационные технологии"
# БВТ2402 - Голиков Михаил Вячеславович

MAX_LOOP = 10*15


def get_number() -> 'bool, int':
  try:
    number: int = int(input("Введите число: "))

  except Exception as e:
    print(f"Некорректный ввод: {e}")
    return False, 0
  return True, number


def check_number(number: int) -> bool:
  if number < 1:
    return False
  return True


def print_numbers(number: int) -> bool:
  is_endless_loop_breakpoint: int = 0

  number_cashe: int = 1

  while number_cashe <= number:

    is_endless_loop_breakpoint+=1  # Аварийное завершение
    if is_endless_loop_breakpoint > MAX_LOOP:
        print('Превышено максимальное число циклов в функции print_numbers')
        return 0
    
    print(number_cashe)
    number_cashe += 1

  return True



def main() -> bool:
  is_got_number: bool
  number: int

  is_got_number, number = get_number()
  if not is_got_number:
    return False
  
  is_number_correct: bool = check_number(number)
  if not is_number_correct:
    print(f'Чисел между 1 и {number} нет')
    return False
  
  is_print_correct: bool = print_numbers(number)
  if not is_print_correct:
    return False
  return True


if __name__ == '__main__':
  main()


'''
for i in range(1,int(input('Введите число: '))+1): print(i);

'''