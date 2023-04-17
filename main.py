import cv2 as cv


# # Reading Images
# img = cv.imread("D:\81g4h40e2c471.jpg")
# cv.imshow("Image", img)
# cv.waitKey(0)

# # Reading Videos
# capture = cv.VideoCapture("D:\\bihar.mp4")  # 0, 1, 2 == camera devices
#
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow("Video", frame)
#
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break
#
# capture.release()
# cv.destroyAllWindows()

# # Change resolution of live video
# def change_res(height, width):
#     capture.set(3,width)
#     capture.set(4,height)

# # Rescaling a frame
# # works with video, image, live video
# def rescale(frame, scale=0.75):
#     height = int(frame.shape[0] * scale)
#     width = int(frame.shape[1] * scale)
#     dimensions = (width, height)
#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
#
#
# img = cv.imread("D:\\81g4h40e2c471.jpg")
#
# resized = rescale(img, 0.2)
#
# cv.imshow("image", resized)
# cv.imshow('image big', img)
# cv.waitKey(0)
