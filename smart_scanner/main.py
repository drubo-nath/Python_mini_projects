import urllib.request as request
import numpy as np
import cv2
from PIL import Image
import time

url = 'http://192.168.0.***:****/shot.jpg'

while True:
    img = request.urlopen(url)
    img_bytes = bytearray(img.read())
    img_np = np.array(img_bytes, dtype=np.uint8)
    frame = cv2.imdecode(img_np, -1)
    frame_cvt = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_blur = cv2.GaussianBlur(frame_cvt, (5, 5), 0)
    frame_edge = cv2.Canny(frame_blur, 30, 50)
    contours, _ = cv2.findContours(frame_edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(max_contour)
        if cv2.contourArea(max_contour) > 5000:
            object_only = frame[y:y+h, x:x+w]
            cv2.imshow("smart scanner", frame)
            if cv2.waitKey(1) == ord('e'):
                img_pil = Image.fromarray(frame)
                time_str = time.strftime('%Y-%m-%d-%H-%M-%S')
                img_pil.save(f'{time_str}.pdf')

















