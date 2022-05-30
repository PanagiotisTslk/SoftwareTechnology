#!/usr/bin/python
# -*- coding:utf-8 -*-

''' Script for Class Camera '''

# Libraries
import cv2

# Class for Cameras
class Camera:

  # Constructor
  def __init__(self, trigger):
    self.trigger = trigger

  def EnableCamera(self):

    cap = cv2.VideoCapture(0)
    frame = None
    # Check if the webcam is opened correctly
    self.CheckCamera(cap)

    if self.trigger is True:

      while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        cv2.imshow('Input', frame)

        c = cv2.waitKey(1)

        if c == 27:
          break

    else:
      print("Camera can not be opened!")

    cap.release()
    cv2.destroyAllWindows()

    return frame

  # Cheking camera
  def CheckCamera(self, camera):

    if not camera.isOpened():
      raise IOError("Cannot open webcam!")

    else:
      self.trigger = True



# aCamera = Camera(False)
# aCamera.EnableCamera()
