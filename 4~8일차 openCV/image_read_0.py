import cv2 as cv

# img = cv.imread('cat.jpg', cv.IMREAD_UNCHANGED)     # 이미지를 흑백으로 바꾸거나 하는 변형없이 불러옴
img = cv.imread('cat.jpg', cv.IMREAD_GRAYSCALE)     # Grayscale로 하면 채널개수가 사라진다.

print('type(img) = ', type(img))
print('img.shape, img.dtype = ', img.shape, img.dtype)  # 불러온 이미지 형태를 출력(세로, 가로, 채널개수)
