import pygame
import win32api
import win32con
import win32gui

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
done = False
fuchsia = (255, 0, 128)  # Transparency color
import pygame #імпортуваєм модуль Pygame за допомогою команди
import random #вбудований модуль, який можна використовувати для створення випадкових чисел, просто імпортувавши випадковий модуль
import win32api # бібліотека розширень Python для Windows, яка дає змогу використовувати функції інтерфейсу прикладного програмування Win32 (API) на Python.
import win32con
import win32gui

pygame.init()
fuchsia = (255, 0, 128)  # Transparency color
WHITE = [255, 255, 255] #колір сніжинок
SIZE = [1920, 1080] #розміри вікна виводу

screen = pygame.display.set_mode((SIZE))
pygame.display.set_caption("Programming World of GFG") #Призначає назву екрану вікна снігопаду(Надану назву можна побачити в лівому кутку вікна виводу)

# Встановлення прозорості вікна
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)

snowFlake = [] #порожній масив для сніжинок
for i in range(550): #Циклування для отримання позицій сніжинок
    x = random.randrange(0, 1920)
    y = random.randrange(0, 1080)
    snowFlake.append([x, y])

clock = pygame.time.Clock()  # об’єкт, який допоможе відстежувати час
done = False  # Сніжинки мають падати, доки користувач не натисне кнопку закриття, і для цього всередині циклу while використовуйте цикл for .
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(fuchsia)  # Прозорість фону
    screen.set_alpha(255)
    for i in range(len(snowFlake)):  # використовуємо цикл for для обробки кожної сніжинки в списку
        pygame.draw.circle(screen, WHITE, snowFlake[i], 4)  # малюєм сніжинки

        snowFlake[i][1] += 1
        if snowFlake[i][1] > 1080:
            y = random.randrange(-50, -10)
            snowFlake[i][1] = y

            x = random.randrange(0, 1920)

            snowFlake[i][0] = x
    pygame.display.update()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()