"""This script compares images visually and prints the error between them."""

# import required libraries
import os
import cv2
import numpy as np
import itertools
import matplotlib.pyplot as plt


# define a function to calculate the error between two images
def error(img1, img2):
    h, w = img1.shape
    diff = cv2.subtract(img1, img2)
    err = np.sum(diff**2)
    mse = err/(float(h*w))
    msre = np.sqrt(mse)
    return mse, diff


# load all images from a certain directory
images = []
for file in os.listdir('res/images'):
    img = cv2.imread(os.path.join('res/images', file))
    if img is not None:
        img = cv2.resize(img, (300, 300), interpolation=cv2.INTER_AREA)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        images.append((file, img))


# compare all images with each other and plot them
x = 0
y = 0
fig, axs = plt.subplots(4,4)
for a, b in itertools.combinations(images, 2):
    match_error, diff = error(a[1], b[1])
    print(f"Image matching Error between image {a[0]} and image {b[0]}:", match_error)
    axs[x, y].imshow(diff, 'gray')
    axs[x, y].set_title(f" - ")
    axs[x, y].axis('off')

    y += 1
    if y >= 4:
        x += 1
        y = 0

plt.show()
