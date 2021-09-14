import numpy as np
import cv2

def on_level_changed(pos):
    global img

    level = pos * 16
    if level >= 255:
        level = 255
    # np.clip(level, 0, 255)

    img[:, :] = level
    cv2.imshow('image', img)

img = np.zeros((480, 640), np.uint8)

# cv2.namedWindow('image')
cv2.imshow('image', img)
cv2.createTrackbar('level', 'image', 0, 16, on_level_changed)  # 트랙바는 윈도우창이 반드시 생성된 뒤에 !

cv2.waitKey()

cv2.destroyAllWindows()