# 도전 1 : 조금 더 정확하게 fps 조절
# 도전 2 : moving window를 활용해서 매 프레임 fps 측정

import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)
fps = capture.get(cv.CAP_PROP_FPS)
dt = int(1000/fps)  # delay 시간은 read에서 걸린 시간에 따라서 평균적으로 33.3프레임이 되도록 해야한다.

count = 0
# fps = 0r
t0 = cv.getTickCount()

while True:
    ret, frame = capture.read()
    if ret:
        cv.putText(frame, str(fps), (10,60), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (0,255,0), 3)
        cv.imshow('frame', frame)
    else:
        break
    if cv.waitKey(dt) == 27:
        break

    count += 1
    if count == 20:
        t = cv.getTickCount()
        time = (t-t0) / cv.getTickFrequency()
        fps = int(np.round(count/time))
        count = 0
        t0 = t

capture.release()