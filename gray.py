# -*- coding: utf-8 -*-
#author： 彭译锋--DUT
#email 1349194985@qq.com

import matplotlib.pyplot as plt
import cv2
import numpy as np
imgpath = "test.jpg"

img = cv2.imread(imgpath)
cv2.namedWindow("cs1")
cv2.imshow("cs1",img)
#cv2.waitKey(0)
img0 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.namedWindow("cs2")
cv2.imshow("cs2",img0)
sx = np.size(img0,0)
sy = np.size(img0,1)
print(sx,sy)
print(type(img0))
x = np.linspace(0, sx, sx)
y = np.linspace(0, sy, sy)
X, Y = np.meshgrid(y, x)
Z = img0

figure = plt.figure(1, figsize = (12, 4))
subplot3d = plt.subplot(111, projection='3d')
surface = subplot3d.plot_surface(X, Y, Z,rstride = 2, cstride = 2,cmap = plt.get_cmap('rainbow'))
plt.show()
cv2.waitKey(0)