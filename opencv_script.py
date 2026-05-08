# Extract data from an image
import cv2
import numpy as np

img = cv2.imread('sample.jpg')
# print(img)


h, w, c = img.shape

red_channel = np.mean(img[:, :, 2])
print("Red channel mean:", red_channel)

green_channel = np.mean(img[:, :, 1])
print("Green channel mean:", green_channel)

blue_channel = np.mean(img[:, :, 0])
print("Blue channel mean:", blue_channel)


bw_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

brightness = np.mean(bw_img)
print("Brightness:", brightness)

contrast = np.std(bw_img)
print("Contrast:", contrast)

# Extract data from a video
cap = cv2.VideoCapture('sample.mp4')

frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print("Frame count:", frame_count)

fps = cap.get(cv2.CAP_PROP_FPS)
print("Frames per second:", fps)

duration = frame_count / fps
print("Duration (seconds):", duration)

