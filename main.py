import numpy as np
import cv2
import matplotlib
from math import *

image = cv2.imread('dog-cat.jpg', cv2.IMREAD_UNCHANGED)
image2 = cv2.imread('cat-dog.jpg', cv2.IMREAD_UNCHANGED)
cv2.putText(
    image,  # numpy array on which text is written
    "cat and dog",  # text
    (10, 50),  # position at which writing has to start
    cv2.FONT_HERSHEY_SIMPLEX,  # font family
    1,  # font size
    (209, 80, 0, 255),  # font color
    5)  # font thickness
cv2.imwrite('dog-cat-text.jpg', image)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(cos(sqrt(8)))
