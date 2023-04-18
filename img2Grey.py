import cv2 as cv

img = cv.imread("C:\\Users\\smara\\Downloads\\wall-01.png")

gery = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(img,(45,45),100)
canny = cv.Canny(img, 500,1000)

def resizeER(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


cv.imshow("image", resizeER(blur))
# cv.imshow("image", resizeER(canny))
# cv.imshow("image", resizeER(gery))

cv.waitKey(0)
