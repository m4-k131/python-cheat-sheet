import cv2
import numpy as np

image_path=""
image = cv2.imread(image_path)
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
img_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

cv2.imwrite(image_path, image)



coords_pts = np.array([[0.4, 0.4], [0.6, 0.4], [0.6, 0.6], [0.4, 0.6]])

pts = (coords_pts * np.array([image.shape[1], image.shape[0]])).astype(np.int32)
roiMasks[imgSource] = cv2.fillConvexPoly(roiMask, pts, color=(1, 1, 1))
highlightMasks[imgSource] = np.multiply(self.__roiMasks[imgSource], np.array(self.__highlightColor, dtype=np.uint8))

video = cv2.VideoCapture(videoFile)
frameId = 0
while video.isOpened():
    success, _ = video.read()
    if success:
        frameId += 1
    else:
        video.release()
        break
return frameId