#pylint:disable=no-member

import cv2 as cv
import numpy as np

mat = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', mat)

# 1. Paint the image a certain colour
mat[200:300, 300:400] = 0,255,0
cv.imshow('Green', mat)

# 2. Draw a Rectangle
# thickness=cv.FILLED is the same as thickness=-1
cv.rectangle(mat, (0,0), (mat.shape[1]//2, mat.shape[0]//2), (255,0,0), thickness=cv.FILLED)
cv.imshow('Rectangle', mat)

# 3. Draw A circle
cv.circle(mat, (mat.shape[1]//2, mat.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', mat)

# 4. Draw a line
cv.line(mat, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', mat)

# 5. Write text
cv.putText(mat, 'Hello, my name is Jason!!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (128,128,128), 2)
cv.imshow('Text', mat)

cv.waitKey(0)