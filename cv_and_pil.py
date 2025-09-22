import cv2
import numpy as np

image_path=""
image = cv2.imread(image_path)
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
img_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

cv2.imwrite(image_path, image)


coordsPts = np.array(self.__highlightConfig[imgSource][roiId]["coords"])

pts = (coordsPts * np.array([image.shape[1], image.shape[0]])).astype(np.int32)
self.__roiMasks[imgSource] = cv2.fillConvexPoly(roiMask, pts, color=(1, 1, 1))
self.__highlightMasks[imgSource] = np.multiply(self.__roiMasks[imgSource], np.array(self.__highlightColor, dtype=np.uint8))

video = cv2.VideoCapture(videofile)
frameId = 0
while video.isOpened():
    success, frame = video.read()
    if success:
        frameId += 1
    else:
        video.release()
        break

colorspace = "rgb"
image = cv2.cvtColor(image, getattr(cv2, "COLOR_BGR2" + colorspace.upper()))
_, encodedImage = cv2.imencode(".jpg", image)
imageBytes = encodedImage.tobytes()