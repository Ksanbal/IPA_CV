# 동영상 파일을 원하는 fps로 재생하고, moving windowfh 매 프레임 fps 측정

import cv2 as cv
import numpy as np

capture = cv.VideoCapture('capture.avi')
dt = 1. / capture.get(cv.CAP_PROP_FPS)  # 내가 지정해주고자하는 프레임
tickFrequency = cv.getTickFrequency()

buffer_size = 10    # 원형큐의 사이즈
ticks = [0] * buffer_size
tick_idx = 0    # 원형큐의 현재 가르키고 있는 index

count = 0   # 지금까지 읽은 프레임의 수를 저장
start_time = cv.getTickCount() / tickFrequency

while True:
    ret, frame = capture.read()
    if not ret:
        break
    # fps measurement
    # 현재로부터 10프레임전의 tick은 어디에 저장되어있는가? -> ticks[tick_idx]
    # 10프레임전의 시각과 현재 시각의 차이는? -> tick - ticks[tick_idx] / tickFrequency
    # fps = buffer_size / (tick - ticks[tick_idx] / tickFrequency)
    tick = cv.getTickCount()
    fps_measured = buffer_size * tickFrequency / (tick - ticks[tick_idx])
    ticks[tick_idx] = tick
    tick_idx = (tick_idx+1) % buffer_size   # 다음 프레임에 tick 저장

    cv.putText(frame, str(int(np.round(fps_measured))), (10,60), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (0,255,0), 2)
    cv.imshow('frame', frame)

    # delay for target fps
    count += 1
    curr_time = cv.getTickCount() / tickFrequency
    delay = start_time + dt * count - curr_time # delay는 최소 1이 되어야한다.

    if cv.waitKey(max(int(np.round(delay*1000)), 1)) == 27:    # delay를 밀리세컨드 단위로 변경, delay가 최소 1이 되도록
        break

capture.release()