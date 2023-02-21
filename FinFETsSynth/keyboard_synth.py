import pygame as pg
import numpy as np
import time
import os

pg.init()
pg.mixer.init()

sampling_rate = 44100
# frequency = 440
# duration = 1.5
def synth(frequency, duration=1.5, sampling_rate=44100):
    frames = int(duration * sampling_rate)
    arr = np.cos(2 * np.pi * frequency * np.linspace(0, duration, frames))
    sound = np.asarray([32767*arr, 32767*arr]).T.astype(np.int16)
    sound = pg.sndarray.make_sound(sound.copy())

    return sound
keylist = '123456789qwertzuioasdfghjklyxcvbnm,.'
notes_file = open(os.path.join(os.getcwd(), 'FinFETsSynth\\noteslist.txt'))
file_contents = notes_file.read()
notes_file.close()
noteslist = file_contents.splitlines()

keymod = '0-='
notes = {} # dict to store samples
freq = 16.3516 # base frequency for calculating all higher frequencies
print("keylist: " + str(len(keylist)) + "\nnoteslist: " + str(len(noteslist)))
for i in range(len(noteslist)):
    mod = int(i/36)
    key = keylist[i-mod*36] + str(mod)
    sample = synth(freq)
    notes[key] = [sample, noteslist[i], freq]
    notes[key][0].set_volume(0.33)
    notes[key][0].play()
    notes[key][0].fadeout(100)
    pg.time.wait(100)
    freq = freq * 2 ** (1/12)

pg.mixer.quit()
# sound.play()
time.sleep(5)
pg.quit()