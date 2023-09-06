# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 22:05:26 2022

@author: Serpil ÖZGÜVEN
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np


#resmi içe aktar
#siyah beyaz olması için sıfır koyuyoruz
img = cv2.imread("london.jpg", 0)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off")

#Burada herhangi bir threshholdu belirlemediğimiz görülüyor
edges = cv2.Canny(image = img, threshold1 = 0, threshold2 = 255)
plt.figure(), plt.imshow(edges, cmap = "gray"), plt.axis("off")


#threshold değerleri değiştireceğiz.
#mantıklı şeyler seçemek istiyorum.En mantıklı değer medyan değeridir.
#np.med ile resmimizin medyanını öğrenelim 

med_val = np.median(img)
print(med_val)
#140 değerini verdi



low = int(max(0,(1 - 0.33)*med_val))
high = int(min(255,(1 + 0.33)*med_val))


print(low)
print(high)

edges = cv2.Canny(image = img, threshold1 = low, threshold2 = high)
plt.figure(), plt.imshow(edges, cmap = "gray"), plt.axis("off")


#blur
blurred_img = cv2.blur(img, ksize = (5,5))
plt.figure(), plt.imshow(blurred_img, cmap = "gray"), plt.axis("off")

med_val = np.median(blurred_img)
print(med_val)
#139 değerini verdi

low = int(max(0,(1 - 0.33)*med_val))
high = int(min(255,(1 + 0.33)*med_val))


print(low)
print(high)


edges = cv2.Canny(image = blurred_img, threshold1 = low, threshold2 = high)
plt.figure(), plt.imshow(edges, cmap = "gray"), plt.axis("off")
























