import time


class User:
    def __init__(self, nickname , password, age):
        # Инициализируем атрибуты пользователя
        self.nickname = nickname  # Имя пользователя
        self.password = hash(password)  # Хэшируем пароль для безопасности
        self.age = age  # Возраст пользователя

    def __repl__(self):
        return f'User (nickname = {self.nickname}, age = {self.age})'

class Video:
    def __init__(self,title, duration, time_now=0, adult_mode = False ):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        # Возвращаем строковое представление видео
        return f"Video(title={self.title}, duration={self.duration}, adult_mode={self.adult_mode})"

class UrTube:
    def __init__(self ):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                print(f'Ты выполнил вход {nickname}')
                return
            print('Неверный логин или пароль')

    def register(self,nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь с таким {nickname}, уже существует')
                return

        new_user = User(nickname ,password ,age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f'Пользователь с {nickname}, был зарегистрирован успешно')
        return new_user

    def log_out(self):
        self.current_user = None
        print(f'Вы вышли из аккаунта ')

    def add(self, *videos):
        for video in videos:
            if not any(b.title == video.title for b in self.videos):
                self.videos.append(video)
                print(f'Видео с названием {video.title} добавлено')
            else:
                print(f'Видео с название {video.title} уже существует')

    def get_videos(self, search_tit):
        return [
            video.title for video in self.videos
            if search_tit.lower() in video.title.lower()
        ]

    def watch_video(self, title):
        if self.current_user is None:
            print('Для просмотра нужно войти в систему или зарегистрироваться')
            return

        for video in self.videos:
            if video.title == title:
                if self.current_user.age < 18 and video.adult_mode:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return

                print(f'Начинаем смотреть, {title}')
                while video.time_now < video.duration:
                    print(video.time_now + 1)
                    video.time_now += 1  # Увеличиваем текущее время
                    time.sleep(1)  # Пауза в 1 секунду
                print('Конец видео')
                return
        print(f"Видео '{title}' не найдено.")



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












