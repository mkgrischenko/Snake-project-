# подключаем библиотеки
import pygame
import random
import sys

#Скорость движения игры
speed = 15

width = 400 # ширина игрового окна 
height = 400 # высота игрового окна

# Задаем цвета
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


#задаем движения
UP  = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

pygame.init() #  запускаем игру
random.seed() # функция для инициализации случайных чисел
#Ввод глобальных переменных
global screen
global clock
clock = pygame.time.Clock()  #Игровой модуль для контроля кодров в секунду
screen = pygame.display.set_mode((width, height)) # задаем окно игры
pygame.display.set_caption("Snake") # задаем название окна игры

#Задаем класс змейки
class snake:
    def __init__(self, x, y, color=(GREEN), pixels=None):
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
        
#Даем команды для клавиш
    def events(self, event):
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
        self.x += self.speedx
        self.y += self.speedy
#Проверяем случай врезания в самого себя
        if (self.x, self.y) in self.pixels:
            self.crash = True

        # Заворачиваем змею по нажатию
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

#Рисуем змейку
    def draw(self):
        for x, y in self.pixels:
            pygame.draw.rect(screen, (GREEN), (x, y+10, 10, 10), 0)

#Задаем класс еды
class food():
    def __init__(self):
        self.x = random.randrange(20, width - 20, 10)
        self.y = random.randrange(20, height - 20, 10)

#Случай попадания змейки на еду
    def hitCheck(self, snakePixels):
        if snakePixels[0][0] == self.x and snakePixels[0][1] == self.y:
            return True

#Смена позиции еды
    def relocate(self):
        self.x = random.randrange(20, width - 20, 10)
        self.y = random.randrange(20, height - 20, 10)

#Рисуем еду
    def draw(self):
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

    if food.hitCheck(snake.pixels): #Увеличиваем змейку если она съедает еду и меняем позицию еды
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
            
    # Обновляет дисплей в конце.
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