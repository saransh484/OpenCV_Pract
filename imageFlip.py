import cv2 as cv

img = cv.imread("C:\\Users\\smara\\Downloads\\wall-01.png")

img = img[0:500, 0:700] #crop

flip = cv.flip(img, -1)

cv.imshow("Flip",flip)

cv.waitKey(0)
