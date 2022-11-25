import numpy as np
from PIL import Image,ImageOps
import math


fileName = "img\\brain.jpeg" 
ogImg = Image.open(fileName)
image = ogImg.copy() 
img = ImageOps.grayscale(image)
P = np.asarray(img)

(r,c) = img.size

# Generate a checkerboard pattern B of size R × C
B = np.indices((r,c)).sum(axis=0) % 2

x,y = 2,2
Q = 1

while(x<=r-1):
    while(y<=c-1):
        if B(x,y) == 1:
            nums = [P[x-1][y],P[x][y-1],P[x][y+1],P[x+1][y]]
            if x==r-1:
                p_ = math.floor(sum(nums[:3])/3)
            elif y==c-1:
                p_ = math.floor((sum(nums)-nums[2])/3)
            elif x==r-1 and y==c-1:
                p_ = math.floor(sum(nums[:2])/2)
            else:
                p_ = predPix(nums,P[x][y])

            Pe = p_ - P[x][y]
            if Pe > 0:
                
                













def binarySearch(nums, target):
    low = 0
    high = len(nums) - 1
 
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid      # key found
 
    return low              # key not found
 
 
# Function to find the `k` closest elements to `target` in a sorted integer array `nums`
def predPix(nums, target):
    k=3
    # find the insertion point using the binary search algorithm
    i = binarySearch(nums, target)
 
    left = i - 1
    right = i
 
    # run `k` times
    while k > 0:
 
        # compare the elements on both sides of the insertion point `i`
        # to get the first `k` closest elements
 
        if left < 0 or (right < len(nums) and abs(nums[left] - target) > abs(nums[right] - target)):
            right = right + 1
        else:
            left = left - 1
 
        k = k - 1
 
    # return `k` closest elements
    return math.floor(sum(nums[left+1: right])/k)