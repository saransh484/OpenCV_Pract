import cv2 as cv

img = cv.imread("C:\\Users\\smara\\Downloads\\wall-01_smol.png")

i = 1000

while True:
    canny = cv.Canny(img,i,i*2)
    cv.imshow("Edges", canny)
    i -= 10
    if cv.waitKey(20) & 0XFF == ord('q'):
        break

cv.destroyAllWindows()