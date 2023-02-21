import pygame as pg
import numpy as np
import time

pg.init()
pg.mixer.init()

sampling_rate = 44100
frequency = 440
duration = 1.5
frames = int(duration * sampling_rate)
arr = np.cos(2 * np.pi * frequency * np.linspace(0, duration, frames))
print(arr)
sound = np.asarray([32767*arr, 32767*arr]).T.astype(np.int16)
sound = pg.sndarray.make_sound(sound.copy())

sound.play()
time.sleep(5)