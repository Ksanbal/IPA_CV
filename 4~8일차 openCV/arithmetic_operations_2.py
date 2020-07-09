# Blend two images with various weights
import cv2 as cv

img0 = cv.imread('add1.jpg', cv.IMREAD_UNCHANGED)
img1 = cv.imread('add2.jpg', cv.IMREAD_UNCHANGED)

num_images = 100

for i in range(99999):
    # 0 <= w0 <= 1
    # i = 0 -> w0 = 0
    # i = num_images-1 -> w0 = 1
    # i = num_images -> w0 = 0
    # i = ...

    w0 = (i % num_images) / (num_images-1)  # 나머지가 0~99이므로, 나머지 / 99
    w1 = 1 - w0
    img = cv.addWeighted(img0, w0, img1, w1, 0)
    cv.imshow('img', img)

    if cv.waitKey(50) == 27:    # waitkey(x) x는 입력 키 번호,
        break