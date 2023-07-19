import torch
import torchvision
import cv2
from deep_sort_realtime.deepsort_tracker import DeepSort

# Initialize the object detection model
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)

# Initialize the object tracking library
tracker = DeepSort()

# Load the video and extract the frames
video = cv2.VideoCapture("./data/videos/layHangTrackingTest.mp4")

count = 0

while video.isOpened():
  # Read the next frame
  success, frame = video.read()
  
  if not success:
    break
  
  # Preprocess the frame
  frame = preprocess_frame(frame)
  
  # Detect people in the frame
  people = detect_people(frame, model)
  
  # Track the people using the object tracking library
  tracked_people = tracker.track(people, frame)
  
  # Increment the count by the number of tracked people
  count += len(tracked_people)
  
  # Display the count on the screen
  display_count(count)

# Release the video capture
video.release()
