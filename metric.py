# from skimage.metrics import structural_similarity
from PIL import Image,ImageOps
import numpy as np
from itertools import chain
from collections import Counter, deque
from math import log10,sqrt
import cv2
from skimage.metrics import structural_similarity as ssim

def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr

img = cv2.imread("img\inputMRI.jpg")
enc = cv2.imread("img\dec.png")

gray1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(enc, cv2.COLOR_BGR2GRAY)

val = PSNR(img,img)
s = ssim(gray1,gray2)
print(f"PSNR value is {val} ")

img1 = Image.open("img\inputMRI.jpg")
# img1 = ImageOps.grayscale(i)
(r,c) = img1.size
Pic = np.asarray(img1)

I = np.transpose(Pic,(1, 0, 2))
P = I[:,:,0]

SimpleList = chain.from_iterable(Pic)
# print(Counter(SimpleList).most_common(1)[0][0])
x=np.count_nonzero(P == 12)
print(x)
# print("Embedding Rate = ",x/(r*c),r,c)



# img2 = Image.open("img\enc.png")

