# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

print("Starting")

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)

print("Camera initialized")

# allow the camera to warmup
time.sleep(0.1)

print("here")

# grab an image from the camera
camera.capture(rawCapture, format="bgr")
print("Captured image")
image = rawCapture.array

print("Got image")

# display the image on screen and wait for keypress
cv2.imshow("Image", image)
cv2.waitKey(0)
