# 카메라에서 정보 가져오기
import cv2 as cv

capture = cv.VideoCapture(0)

width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = int(capture.get(cv.CAP_PROP_FPS))
print('w, h, fps = ', width, height, fps)

fourcc = cv.VideoWriter_fourcc(*'XVID')   #코덱 (python_언팩킹으로 문자열을 분리해서 인자로 넘겨준다)
# fourcc = cv.VideoWriter_fourcc(*'DX50')
writer = cv.VideoWriter('capture.avi', fourcc, 60, (width, height)) # fps의 값이 영상의 fps보다 커지면 빠르게 재생되고, 낮아지면 느리게 재생된다.

while True:
    ret, frame = capture.read()     # ret = 이미지 불러오기 성공여부, frame = 이미지 내용
    writer.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == 27:    # FPS보다 waitKey의 값이 더 낮아야한다. -> 가장 작은 1로
        break

capture.release()   # 카메라 자원 반환
writer.release()