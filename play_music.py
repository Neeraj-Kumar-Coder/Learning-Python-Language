from pygame import mixer
mixer.init()  # Starting the mixer
song_name = input("Enter the name of the song you want to listen\nphysical.mp3\neyes.mp3\nwater.mp3\n==> ")
mixer.music.load(song_name)  # Loading the song
while(True):
    mixer.music.play()  # Play the song
    to_stop_the_music = input("Enter 's' to stop, 'p' to pause and 'r' to resume the music: ")
    if to_stop_the_music == 's':
        mixer.music.stop()
        break
    elif to_stop_the_music == 'p':
        mixer.music.pause()
    elif to_stop_the_music == 'r':
        mixer.music.unpause()
