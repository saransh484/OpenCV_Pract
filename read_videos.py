import cv2 as cv

# Reading Videos
capture2 = cv.VideoCapture("C:\\Users\\smara\\Downloads\\Video\\demonslayer.mp4")  # 0, 1, 2 == camera devices
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    canny = cv.Canny(frame, 50,100)
    # blur = cv.GaussianBlur(canny, (5,5),0)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("Video", hsv)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()

# # Change resolution of live video
# def change_res(height, width):
#     capture.set(3,width)
#     capture.set(4,height)
