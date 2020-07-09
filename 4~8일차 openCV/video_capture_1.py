# Play video file

import cv2 as cv

capture = cv.VideoCapture('capture.avi')
fps = capture.get(cv.CAP_PROP_FPS)
dt = int(1000/fps)   # 프레임간의 시간

while True:
    ret, frame = capture.read()
    if ret:
        cv.imshow('frame', frame)
    else:
        break
    if cv.waitKey(dt) == 27:    # 사실 read에서 디코딩 시간을 거치기 때문에 정확한 영상의 프레임으로 재생할 수 없다.
        break                   # 따라서 정확한 프레임으로 재생하기 위해서는 디코딩 시간을 제외하고 재생해야한다

capture.release()