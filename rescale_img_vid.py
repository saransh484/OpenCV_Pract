import cv2 as cv


# Rescaling a frame
# works with video, image, live video
def rescale(frame, scale=0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread("C:\\Users\\smara\\Downloads\\wall-01.png")

resized = rescale(img, 0.2)

cv.imshow("image", resized)
cv.imshow('image big', img)
cv.waitKey(0)
