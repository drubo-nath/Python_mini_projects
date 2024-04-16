import datetime

from PIL import ImageGrab
import numpy as np
import cv2
from win32api import  GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_vid = cv2.VideoWriter(file_name, fourcc, 5.0, (width, height))

webcam = cv2.VideoCapture(0)
while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGRA2RGB)
    _, frame = webcam.read()
    fr_height, fr_width, _ = frame.shape
    img_final[0:fr_height, 0: fr_width, :] = frame
    cv2.imshow('Capture', img_final)
    # cv2.imshow('webcam', frame)

    captured_vid.write(img_final)

    if cv2.waitKey(10) == ord('q'):
        break