import pygame as pg
import numpy as np

pg.init()
pg.mixer.init()

sampling_rate = 44100
frequency = 440
duration = 1.5
frames = int(duration * sampling_rate)
arr = np.cos(2 * np.pi * frequency)

sound = np.asarray([])