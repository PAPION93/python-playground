import cv2
import sys

print('Hello, OpenCV', cv2.__version__)

img = cv2.imread('./05_opencv/ch01/cat.bmp')

if img is None:
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image', img)
cv2.waitKey(10)
cv2.destroyAllWindows()