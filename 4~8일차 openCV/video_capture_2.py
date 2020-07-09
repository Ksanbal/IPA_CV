# Show fps on the frames
import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)
count = 0
fps = 0
t0 = cv.getTickCount()  # CPU의 카운트를 측정

while True:
    ret, frame = capture.read() # 이미지가 들어올때까지 자원을 잡고있다.
    cv.putText(frame, str(fps), (10,60), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (255,255,128), 1)   # 영상에 fps 출력
    cv.imshow('frame', frame)
    if cv.waitKey(1) == 27:
        break

    count += 1  # 각 프레임마다 1씩 증가
    if count == 20:
        t = cv.getTickCount()
        time = (t-t0) / cv.getTickFrequency()  # 실제시간으로 변환하기 위해, tick횟수/초당 틱의 수
        fps = int(np.round(count/time)) # 반올림
        count = 0
        t0 = t

capture.release()

# fps = f/s = 1/deltaT = 1/33ms but, 장당으로 계산하면 노이즈가 발생할 수 있다.
# 따라서 여러장을 모아 평균적으로 값을 구한다.
# 10장을 기준으로 잡는 경우 fps = 10/시간
# moving window, 각 프레임미다 전 5프레임까지의 fps를 구해 update 한다.(원형큐를 이용해 시간을 메모리에 저장해둔다)

