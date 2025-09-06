from sklearn.cluster import DBSCAN
import numpy as np 
import pandas as pd 
import math 

EPS = 1

sMatrix = sMatrixDf.iloc[0:, 0:].astype(float).values
imagePathsList = sMatrixDf.index.tolist()
eps = EPS / math.sqrt(sMatrix.shape[1])
dbscan = DBSCAN(eps=eps, min_samples=1, metric="precomputed")
clusterLabels = dbscan.fit_predict(sMatrix)
for i in range(clusterLabels.shape[0]):
    shutil.copy2(imagePathsList[i], os.path.join(os.path.join(outDir, "images", str(clusterLabels[i]) + "_" + imagePathsList[i].split("/")[-1])))
    outdata.append([imagePathsList[i], eps, modelLayer, clusterLabels[i]])
return outdata