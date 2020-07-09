import cv2 as cv
import numpy as np

img0 = np.zeros((480,640,3), np.uint8)
img = np.copy(img0)

x0 = y0 = 0


def on_mouse(event, x, y, flags, param):
    global x0, y0, img0, img, draw

    if event == cv.EVENT_LBUTTONDOWN:
        x0, y0 = x, y

    elif event == cv.EVENT_MOUSEMOVE and flags:
        np.copyto(img, img0)
        cv.rectangle(img, (x0,y0), (x,y), (255,255,0), 2)

    elif event == cv.EVENT_LBUTTONUP:
        np.copyto(img0, img)


cv.namedWindow('img')
cv.setMouseCallback('img', on_mouse)

while True:
    cv.imshow('img', img)
    if cv.waitKey(30) == 27:
        break