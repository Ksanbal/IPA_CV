import cv2 as cv

img = cv.imread('cat.jpg', cv.IMREAD_UNCHANGED)

cv.namedWindow('img')


def on_mouse(event, x, y, flags, param):
    # event : 발생한 이벤트
    # x, y = 발생한 좌표
    # falgs = 추가정보

    print(event, x, y, flags, param)


cv.setMouseCallback('img', on_mouse)   # 마우스 이벤트가 발생했을때 지정해준 함수를 실행

cv.imshow('img', img)
cv.waitKey()

