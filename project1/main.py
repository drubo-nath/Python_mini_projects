import cv2
import cvzone
cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
overlay = cv2.imread('beard.png', cv2.IMREAD_UNCHANGED)
while True:
    _, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
    #cv2.imshow('snap dude', gray_scale)
    faces = cascade.detectMultiScale(gray_scale)
    for (x, y, w, h) in faces:
        #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        overlay_resize = cv2.resize(overlay, (int(w*1.5), int(h*1.5)))
        frame = cvzone.overlayPNG(frame, overlay_resize, [x-45, y-90])
    cv2.imshow('Snapchat dead', frame)
    if cv2.waitKey(10) == ord('q'):
        break
# bg = cv2.imread('mypic.png')
# sunglass = cv2.imread("star.png", cv2.IMREAD_UNCHANGED)
# final_img = cvzone.overlayPNG(bg, sunglass, [90, 40])
# cv2.imshow('Snapchat dead', final_img)
# cv2.waitKey(0)
