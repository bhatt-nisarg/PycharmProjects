"""excersice 7
    Healthy Programmer"""


"""
        9 to 5 pm
        concept
        water -water.mp3  (3.5 litres) - Drank - log- Every 40min
        
        Eyes - eyes.mp3     (30 minutes) - ex-done-log- Every 30 min
        physical activity - physical.mp3  every 45 minutes - ex-don - log 
        rules
        pygame module to play audio"""


from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt", "a") as f:
      f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
      init_water = time()
      init_eyes = time()
      init_exercise = time()
      watersecs = 40*60
      exsecs = 45*60
      eyesecs = 30*60

      while True:
         if time() - init_water > watersecs:
                print("water Drinking time, Enter 'drank' to stop the alarm.")
                musiconloop('water.mp3', 'drank')
                init_water = time()
                log_now("Drank water at")
         if time() - init_eyes > eyesecs:
                print("eye exercise time, Enter 'doneeyes' to stop the alarm.")
                musiconloop('eye.mp3', 'doneeyes')
                init_eyes = time()
                log_now("Eyes Relaxed at")
         if time() - init_exercise > exsecs:
                print("Physical Activity time, Enter 'donephy' to stop the alarm.")
                musiconloop('physical.mp3', 'donephy')
                init_exercise = time()
                log_now("physical activity done at")
"""
# time - init > exercise"""

""" it means time is time now means live time
    intin time means when last he do activity that time 
    means last when you water drink that is your init time
    is greater then the time limit then its run these is main operation in these"""



