import pygame
import time
def getdate():
    import datetime
    return datetime.datetime.now()

initial_wat = time.time()
initial_eyes = time.time()

def musiccontrol(write,stopper):
    if (write == stopper):
        f = open("water_exercise_log.txt", "a")
        f.write("Water was drank at " + str(getdate()) + "\n")
        f.close()
        pygame.mixer.music.stop()

while(True):
    if time.time() - initial_wat >= 10:
        pygame.mixer.init()
        pygame.mixer.music.load('example.mp3')
        pygame.mixer.music.play()
        initial_wat = time.time()
        print("Write drank to stop music")
        drank = input()
        musiccontrol(drank,"drank")
    if time.time() - initial_eyes >= 35:
        pygame.mixer.init()
        pygame.mixer.music.load('example.mp3')
        pygame.mixer.music.play()
        print("Write eye to stop music")
        eye = input()
        initial_eyes = time.time()
        musiccontrol(eye,"eye")



