class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        def __is_valid_vin(vin_number):
            if isinstance(vin_number, int):
                if vin_number in range(1000000, 9999999):
                    return True
                else:
                    raise IncorrectVinNumber('Неверный диапазон для vin номера')
            else:
                raise IncorrectVinNumber('Некорректный тип vin номер')
        if __is_valid_vin(__vin):
            self.__vin = __vin
        def __is_valid_numbers(numbers):
            if isinstance(numbers, str):
                if len(numbers) == 6:
                    return True
                else:
                    raise IncorrectCarNumbers('Неверная длина номера')
            else:
                raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if __is_valid_numbers(__numbers):
            self.__numbers = __numbers

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')