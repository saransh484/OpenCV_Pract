import cv2 as cv

# Reading Videos
capture = cv.VideoCapture("D:\\bihar.mp4")  # 0, 1, 2 == camera devices

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

# # Change resolution of live video
# def change_res(height, width):
#     capture.set(3,width)
#     capture.set(4,height)
