import cv2
import numpy as np

def negative(image):
    shape = len(image.shape)
    if shape==3:
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    y, x = image.shape
    negative = np.zeros( (y,x), dtype="uint8" )
    for i in range(y):
        for j in range(x):
            negative[i,j] = 255 - image[i,j]
    negative=negative.astype("uint8")
    return negative

def brightening(image, customRange):
    shape = len(image.shape)
    if shape==3:
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    y, x = image.shape
    bright = np.zeros( (y,x), dtype="uint8" )
    for i in range(y):
        for j in range(x):
            temp = image[i,j] + int(customRange)
            if (temp<0):
                bright[i,j] = 0
            elif (temp>255):
                bright[i,j] = 255
            else:
                bright[i,j] = temp
    bright=bright.astype("uint8")
    return bright

def boolean(image):
    shape = len(image.shape)
    if shape==3:
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    thresh, biner = cv2.threshold(image, 125, 255, cv2.THRESH_BINARY)
    notBooleanImage = cv2.bitwise_not(biner)
    return notBooleanImage
    
def rotation(image):
    shape = len(image.shape)
    if shape==3:
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    y, x = image.shape
    rotate = np.zeros( (x,y), dtype="uint8" )
    for i in range(y):
        k = x-1
        for j in range(x):
            rotate[k,i]=image[i,j]
            k-=1
    rotate=rotate.astype("uint8")
    return rotate

def arithmetic(image,image2):
    x = 350
    y = 350
    shape = len(image.shape)
    shape2 = len(image2.shape)
    if shape==3:
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    if shape2==3:
        image2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
    down_points = (x, y)
    image = cv2.resize(image, down_points, interpolation= cv2.INTER_LINEAR)
    image2 = cv2.resize(image2, down_points, interpolation= cv2.INTER_LINEAR)
    resultImage = np.zeros( (y,x), dtype="uint8" )
    for i in range(y):
        for j in range(x):
            temp = image[i,j] + image2[i,j]
            if (temp>255):
                resultImage[i,j] = 255
            else:
                resultImage[i,j] = temp
    resultImage=resultImage.astype("uint8")
    return resultImage

def get_filtered_image(image, image2, action, customRange):
    # img = cv2.cvtColor(image, cv2.COLOR)
    if action == 'NO_FILTER':
        filtered = image
    elif action == 'GREYSCALE':
        filtered = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        # filtered = cv2.imread("irene.jpg",cv2.IMREAD_GRAYSCALE)
    elif action == 'NEGATIVE':
        filtered = negative(image)
    elif action == 'BRIGHTENING':
        filtered = brightening(image, customRange)
    elif action == 'BOOLEAN':
        filtered = boolean(image)
    elif action == 'GEOMETRI':
        filtered = rotation(image)
    elif action == 'ARITMETIKA':
        filtered = arithmetic(image, image2)
    else:
        filtered = image

    return filtered