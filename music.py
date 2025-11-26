import pygame
import time

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('matue.mp3')
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
        time.sleep(1)  #evita loop travando a CPU

print('Terminou de tocar')