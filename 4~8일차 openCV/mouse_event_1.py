# detect mouse clicks and wheel scroll up and down
import cv2 as cv


def on_mouse(event, x, y, flags, param):
    # event : 발생한 이벤트
    # x, y = 발생한 좌표
    # falgs = 추가정보

    if event == cv.EVENT_LBUTTONDOWN: # 왼쪽버튼 클릭이 발생했을 때
        print('left mouse btn down at', x, y)
    elif event == cv.EVENT_LBUTTONUP:
        print('left mouse btn up at', x, y)
    elif event == cv.EVENT_RBUTTONUP:
        print('right mouse btn')
    elif event == cv.EVENT_LBUTTONDBLCLK:
        print('left mouse btn double click')
    elif event == cv.EVENT_RBUTTONDBLCLK:
        print('right mouse btn double click')
    elif event == cv.EVENT_MOUSEWHEEL:
        if flags > 0:
            print('Up Wheel')
        else:
            print('Down Wheel')
    # elif event == cv.EVENT_MOUSEHWHEEL: # 휠 수평 움직임 감지
    #     print('H')


img = cv.imread('cat.jpg', cv.IMREAD_UNCHANGED)

cv.namedWindow('img')

cv.setMouseCallback('img', on_mouse)   # 마우스 이벤트가 발생했을때 지정해준 함수를 실행

cv.imshow('img', img)
cv.waitKey()


