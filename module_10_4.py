import threading
from queue import Queue
from random import randint
from time import sleep

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))

class Cafe:
    def __init__(self, *args):
        self.queue = Queue()
        self.tables = args

    def guest_arrival(self, *guests):
        for j in guests:
            for i in self.tables:
                if i.guest is None:
                    i.guest = j
                    i.guest.start()
                    print(f'{j.name} сел(-а) за стол номер {i.number}')
                    break
                elif i.guest and i == self.tables[-1]:
                    self.queue.put(j)
                    print(f'{j.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or self.check_tables():
            for i in self.tables:
                if i.guest and not i.guest.is_alive():
                    print(f'{i.guest.name} покушал(-а) и ушёл(ушла)')
                    i.guest = None
                    print(f'Стол номер {i.number} свободен')
                    if not self.queue.empty():
                        i.guest = self.queue.get()
                        print(f'{i.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {i.number}')
                        i.guest.start()

    def check_tables(self):
        for i in self.tables:
            if i.guest:
                return True
        return False

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()