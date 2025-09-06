import hashlib
from functools import lru_cache
import cachetools
pathCache = cachetools.LRUCache(maxsize=10000000)



@lru_cache(maxsize=250000)
def __processImage(self, imgPath):
    imageLoaded = False
    reloads = 0
    while not imageLoaded and reloads < Constants.MAX_RELOADS:
        try:
            image = cv2.imread(imgPath)
            imgShape = image.shape
            imageLoaded = True
        except:
            reloads += 1
            self._logger.warn(f"{imgPath} could not be loaded. Reloads: {reloads}")
    if imageLoaded:
        image = self.resizeImage(image.astype(np.uint8))
        modelOutput = self.__simModel.call(tf.constant(image), training=False)
        return modelOutput
    else:
        return np.zeros((1, 28, 28, 64))


def getFileHash(filePath):
    finalHash = hashlib.sha256()
    with open(filePath, "rb") as f:
        for byteBlock in iter(lambda: f.read(4096), b""):
            finalHash.update(byteBlock)
        finalHash = finalHash.hexdigest()
    return finalHash
