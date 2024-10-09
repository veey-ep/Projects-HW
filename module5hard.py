import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.age = age
        self.password = hash(password)

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
    def log_in(self, nickname, password):
        for i in self.users:
            if i.nickname == nickname and i.password == hash(password):
                self.current_user = i
                break
    def register(self, nickname, password, age):
        reg = True
        for i in self.users:
            if i.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                reg = False
        if reg:
            self.users.append(a := User(nickname, password, age))
            self.current_user = a
    def log_out(self):
        self.current_user = None
    def add(self, *args):
        reg = True
        for i in args:
            for j in self.videos:
                if i.title.lower() == j.title.lower():
                    reg = False
            if reg:
                self.videos.append(i)
    def get_videos(self, search):
        serp = []
        for i in self.videos:
            if search.lower() in i.title.lower():
                serp.append(i.title)
        return serp
    def watch_video(self, title):
        if self.current_user:
            for i in self.videos:
                if title.lower() == i.title.lower():
                    if self.current_user.age < 18 and i.adult_mode:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        for j in range(i.time_now, i.duration):
                            print(j)
                            time.sleep(1)
                        print('Конец видео')
                        i.time_now = 0
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

#Проверка выхода и входа в аккаунт
ur.log_out()
print(ur.current_user)
ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
print(ur.current_user.nickname)