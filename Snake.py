#подключаем библиотеки
import pygame
import random
import sys

#Скорость движения игры
speed = 15

#Ширина игрового окна
width = 400
#Высота игрового окна
height = 400

#Задаем цвета
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


#задаем команды для движения
UP  = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

#Запускаем игру
pygame.init()
#Функция для инициализации случайных чисел
random.seed() 
#Ввод глобальных переменных
global screen
global clock
#Игровой модуль для контроля кадров в секунду
clock = pygame.time.Clock()
#Задаем параметры окна игры
screen = pygame.display.set_mode((width, height))
#Задаем название окна игры
pygame.display.set_caption("Snake")

class snake:
    """Класс змейки
    Конструктор принимает цвет, размер, позицию, движения змейки
    x,y: координаты по оси x,y
    color: цвет змейки        
    pixels: массив пар координат клеток змейки
    crash: True - если змейка врезалась в саму себя
    speedx: движение змейки по оси x
    speedy: движение змейки по оси y
    length: длина змейки"""

    def __init__(self, x, y, color=(GREEN), pixels=None):
        """Метод для задачи параметров Змейки
        :param self: стандартное имя первого аргумента для методов объекта
        :param x,y: координаты по оси x,y
        :param color: цвет змейки
        :param pixels: массив пар координат клеток змейки (по умолчанию pixels = [(x,y)])
        """
        self.x = x
        self.y = y
        self.speedx = 0
        self.speedy = -10
        if pixels == None:
            self.pixels = [(x, y)]
        else:
            self.pixels = pixels
        self.color = color
        self.crash = False
        self.length = 5
        
    def events(self, event):
        """Метод для обрабоки событий нажатия клавиш
        :param self: стандартное имя первого аргумента для методов объекта
        :param event: событие pygame"""
        if event.key == pygame.K_UP:
            self.speedx = 0
            self.speedy = -10
        elif event.key == pygame.K_DOWN:
            self.speedx = 0
            self.speedy = 10
        elif event.key == pygame.K_LEFT:
            self.speedx = -10
            self.speedy = 0
        elif event.key == pygame.K_RIGHT:
            self.speedx = 10
            self.speedy = 0

    def move(self):
        """Метод перемещения объектов
        :param self: стандартное имя первого аргумента для методов объекта"""
        self.x += self.speedx
        self.y += self.speedy

        #Проверяем случай врезания в самого себя
        if (self.x, self.y) in self.pixels:
            self.crash = True

        #Заворачиваем змею по нажатию
        if self.x < 0:
            self.x = width-10
        elif self.x >= width:
            self.x = 0
        elif self.y <= 0:
            self.y = height-20
        elif self.y >= height-10:
            self.y = 10
            
        self.pixels.insert(0, (self.x, self.y))

        #Увеличиваем длинну змейки после попадания на еду
        if len(self.pixels) > self.length:
            del self.pixels[self.length]

    def draw(self):
        """Метод для того чтобы нарисовать примитивные объекты
        :param self:стандартное имя первого аргумента для методов объекта """
        for x, y in self.pixels:
            pygame.draw.rect(screen, (GREEN), (x, y+10, 10, 10), 0)

class food():
    """Класс еды
    Конструктор принимает цвет, размер, локазцию еды
    x,y: координаты по оси x,y
    """
    def __init__(self):
        """Метод для задачи параметров Еды
        :param self: стандартное имя первого аргумента для методов объекта """
        self.x = random.randrange(20, width - 20, 10)
        self.y = random.randrange(20, height - 20, 10)

    def hitCheck(self, snakePixels):
        """Случай попадания змейки на еду"""
        if snakePixels[0][0] == self.x and snakePixels[0][1] == self.y:
            return True

    def relocate(self):
        """Метод для Смена позиции еды
        :param self: стандартное имя первого аргумента для методов объекта"""
        self.x = random.randrange(20, width - 20, 10)
        self.y = random.randrange(20, height - 20, 10)

    def draw(self):
        """Метод для того чтобы нарисовать примитивные обЪекты
        :param self: стандартное имя первого аргумента для методов объекта"""
        pygame.draw.rect(screen, (RED), (self.x, self.y+10, 10, 10), 0)

#Команда запускающая игру
running = True 
arrowKeys = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
food = food()
#Начальная позиция змейки
snake = snake(width/2, height/2)

#Цикл игры
while running:
    screen.fill((BLACK))
    snake.move()
    snake.draw()
    food.draw()
    #Увеличиваем змейку если она съедает еду и меняем позицию еды
    if food.hitCheck(snake.pixels):
        food.relocate()
        snake.length = snake.length + 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if  event.key in arrowKeys:
                snake.events(event)
            elif event.key == pygame.K_ESCAPE:
                running = False
            clock.tick(speed)
            
    #Обновляе дисплей в конце
    pygame.display.flip()
    clock.tick(speed)

    #Обнавляем игру если у нас проигрыш
    while snake.crash:
        pygame.display.flip()
        clock.tick(speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                snake.crash = False
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                food.__init__()
                snake.__init__(height/2,width/2)
            elif event.key == pygame.K_ESCAPE:
                screen.fill((BLACK))
                food.__init__()
                snake = snake(width/2, width/2)