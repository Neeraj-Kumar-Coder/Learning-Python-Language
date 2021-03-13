# HEALTHY PROGRAMMER
# Assuming working hours from 9AM to 5PM and water glass size to be 250ml. Average human should drink approx 4ltr water a day
import time
from pygame import mixer


def getTime():
    import datetime
    return datetime.datetime.now()


initial_time = time.time()  # Storing the initial time (in seconds)
print(f"\nThe reminder program has started now...\nCurrent time : {getTime()}")

while(True):
    if time.time()-initial_time > 86400:
        break
    time.sleep(1800)

    mixer.init()
    mixer.music.load("eyes.mp3")
    mixer.music.play()
    response = input("Have you done eyes exercise?(y/n): ")
    if response == 'y':
        print(f"{getTime()}: ==> You have done eyes exercise!!")
        mixer.music.stop()
    else:
        print(f"{getTime()}: ==> You haven't done eyes exercise!!")
        mixer.music.stop()
    mixer.init()
    mixer.music.load("water.mp3")
    mixer.music.play()
    response = input("Have you drank 250ml of water?(y/n): ")
    if response == 'y':
        print(f"{getTime()}: ==> You have drank 250ml of water!!")
        mixer.music.stop()
    else:
        print(f"{getTime()}: ==> You haven't drank 250ml of water!!")
        mixer.music.stop()

    time.sleep(900)

    mixer.init()
    mixer.music.load("physical.mp3")
    mixer.music.play()
    response = input("Have you done physical exercise?(y/n): ")
    if response == 'y':
        print(f"{getTime()}: ==> You have done physical exercise!!")
        mixer.music.stop()
    else:
        print(f"{getTime()}: ==> You haven't done physical exercise!!")
        mixer.music.stop()
