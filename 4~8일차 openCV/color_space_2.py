# Decrease the color saturation
# Increase the color saturation
# Change the color

import cv2 as cv

bgr = cv.imread('cat.jpg')
cv.imshow('before', bgr)

# 채도를 낮추기 위해 HSV로 변형 후 S에 *0.5
# 다시 merge하여 BGR로 출력
HSV = cv.cvtColor(bgr, cv.COLOR_BGR2HSV)
H, S, V = cv.split(HSV)

# 채도 낮추기
S1 = cv.addWeighted(S, 0.5, S, 0, 0)
HS1V = cv.merge((H,S1,V))

# 채도 높히기
S2 = cv.addWeighted(S, 2, S, 0, 0)
HS2V = cv.merge((H,S2,V))

H1 = cv.addWeighted(H, 1, H, 0, 180//2)
H1SV = cv.merge((H1,S,V))

cv.imshow('HS1V', cv.cvtColor(HS1V, cv.COLOR_HSV2BGR))
cv.imshow('HS2V', cv.cvtColor(HS2V, cv.COLOR_HSV2BGR))
cv.imshow('H1SV', cv.cvtColor(H1SV, cv.COLOR_HSV2BGR))

cv.waitKey()