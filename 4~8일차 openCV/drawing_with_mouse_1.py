import cv2 as cv
import numpy as np

img0 = np.zeros((480,640,3), np.uint8)
img = np.copy(img0)

x0 = y0 = 0
mode = 1


def on_mouse(event, x, y, flags, param):
    global x0, y0, img0, img, mode
    # 1번 버튼 : 직선
    if mode == 1:
        if event == cv.EVENT_LBUTTONDOWN:
            x0, y0 = x, y
        elif event == cv.EVENT_MOUSEMOVE and flags:
            np.copyto(img, img0)
            cv.line(img, (x0, y0), (x,y), (255,0,0), 2)
        elif event == cv.EVENT_LBUTTONUP:
            np.copyto(img0,img)

    # 2번 버튼 : 사각형
    elif mode == 2:
        if event == cv.EVENT_LBUTTONDOWN:
            x0, y0 = x, y
        elif event == cv.EVENT_MOUSEMOVE and flags:
            np.copyto(img, img0)
            cv.rectangle(img, (x0, y0), (x, y), (0, 255, 0), 2)
        elif event == cv.EVENT_LBUTTONUP:
            np.copyto(img0, img)

    # 3번 버튼 : 원
    elif mode == 3:
        if event == cv.EVENT_LBUTTONDOWN:
            x0, y0 = x, y
        elif event == cv.EVENT_MOUSEMOVE and flags:
            np.copyto(img, img0)
            r = int(np.sqrt((x-x0)**2 + (y-y0)**2))
            cv.circle(img, (x0,y0), r, (0,0,255), 2)
        elif event == cv.EVENT_LBUTTONUP:
            np.copyto(img0, img)

    # 4번 버튼 : 자유 그리기
    elif mode == 4:
        if event == cv.EVENT_LBUTTONDOWN:
            x0, y0 = x, y
        elif event == cv.EVENT_MOUSEMOVE and flags:
            cv.line(img, (x0,y0), (x,y), (255,255,0),2)
            x0, y0 = x, y
        elif event == cv.EVENT_LBUTTONUP:
            np.copyto(img0, img)

    if event == cv.EVENT_LBUTTONDOWN:
        x0, y0 = x, y
    elif event == cv.EVENT_MOUSEMOVE and flags:
        if mode < 4:
            np.copyto(img, img0)

        if mode == 1:   # 직선 그리기
            cv.line(img, (x0, y0), (x, y), (255, 0, 0), 2)
        elif mode == 2: # 사각형 그리기
            cv.rectangle(img, (x0, y0), (x, y), (0, 255, 0), 2)
        elif mode == 3: # 원 그리기
            r = int(np.sqrt((x - x0) ** 2 + (y - y0) ** 2))
            cv.circle(img, (x0, y0), r, (0, 0, 255), 2)
        elif mode == 4: # 자유 그리기
            cv.line(img, (x0, y0), (x, y), (255, 255, 0), 2)
            x0, y0 = x, y

    elif event == cv.EVENT_LBUTTONUP:
        np.copyto(img0, img)

cv.namedWindow('img')
cv.setMouseCallback('img', on_mouse)

while True:
    cv.imshow('img', img)
    key = cv.waitKey(30)
    if 48 < key < 53:
        mode = key - 48
    elif key == 27:
        break

cv.imwrite('Drawimg.png', img0)
