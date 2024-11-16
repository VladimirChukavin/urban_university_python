# Дополнительное практическое задание по модулю
from time import sleep


class User:
    """
    Класс, содержащий необходимые атрибуты и методы для создания объекта пользователя
    """

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    """
    Класс, содержащий необходимые атрибуты и методы для создания объекта видео
    """

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


class UrTube:
    """
    Класс, содержащий необходимые атрибуты и методы для создания объекта видеосервиса
    """

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user

    def register(self, nickname, password, age):
        nickname_list = [user.nickname for user in self.users]
        new_user = User(nickname, password, age)
        if len(nickname_list) == 0:
            self.users.append(new_user)
            self.log_in(nickname, password)
        else:
            if nickname not in nickname_list:
                self.users.append(new_user)
                self.log_in(nickname, password)
            else:
                print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for arg in args:
            title_list = [video.title for video in self.videos]
            if len(title_list) == 0:
                self.videos.append(arg)
            else:
                if arg.title not in title_list:
                    self.videos.append(arg)

    def get_videos(self, search_word):
        res = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                res.append(video.title)
        return res

    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
        elif self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            for video in self.videos:
                if title == video.title:
                    start = video.time_now if video.time_now > 0 else 1
                    for i in range(start, video.duration + 1):
                        print(i, end=' ')
                        sleep(1)
                    else:
                        print('Конец видео')


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
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
