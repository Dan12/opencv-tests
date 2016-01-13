# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import os

# define the path to the face detector
FACE_DETECTOR_PATH = "{base_path}/detectors/haarcascade_frontalface_default.xml".format(
	base_path=os.path.abspath(os.path.dirname(__file__)))
print __file__

print("Starting")

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
resolution = (640,480)
camera.resolution = resolution
camera.framerate = 24
rawCapture = PiRGBArray(camera, size=resolution)

print("Camera initialized")

# allow the camera to warmup
time.sleep(0.1)

detector = cv2.CascadeClassifier(FACE_DETECTOR_PATH)

# capture frame from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, the initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array

	# convert the image to grayscale, load the face cascade detector,
	# and detect faces in the image
	grImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	rects = detector.detectMultiScale(grImage, scaleFactor=1.2, minNeighbors=3,
		minSize=(90, 90), flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
	# print(rects)
	
	# construct a list of bounding boxes from the detection
	rects = [(int(x), int(y), int(x + w), int(y + h)) for (x, y, w, h) in rects]
	print(rects)

	# show the frame
	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF

	# clear the stream in preperation for the next frame
	rawCapture.truncate(0)

	# if the 'q' key was pressed, break from the loop
	if key == ord("q"):
		break