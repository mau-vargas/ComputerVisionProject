import cv2
from playsound import playsound
ComputerVisionProject
capture = cv2.VideoCapture(0)


def readCircle():
    for i in circles[0, :]:
        center = (int(i[0]), int(i[1]))
        radius = int(i[2])
        playsound('sound.mp3')
        cv2.circle(image, center, 1, (255, 0, 0), 3)
        cv2.circle(image, center, radius, (255, 0, 255), 3)


def cubeRead():
    print("cube")


def adaptiveThreshold(gray):
    return cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 3.5)


while True:
    ret, image = capture.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    gray = cv2.medianBlur(gray, 5)
    #gray = adaptiveThreshold(gray)

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 10)

    if circles is not None:
        readCircle()

    cv2.imshow('video', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
