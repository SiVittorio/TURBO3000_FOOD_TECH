# Import OpenCV module
import cv2
# Import pyplot from matplotlib as pltd
from matplotlib import pyplot as pltd
import matplotlib.pyplot as plt
from xml.dom import minidom
import numpy as np

def dots():
    doc = minidom.parse('test.xml')
    items = doc.getElementsByTagName('points')

    xy = []

    for elem in items:
        xy.append(list(map(lambda x: list(map(float, x.split(','))), elem.attributes['points'].value.split(';'))))

    xy = xy[0]

    return xy

def table(xy):
    # Opening the image from files
    imaging = cv2.imread("images1/1.jpg")
    # Altering properties of image with cv2
    img_gray = cv2.cvtColor(imaging, cv2.COLOR_BGR2GRAY)
    imaging_rgb = cv2.cvtColor(imaging, cv2.COLOR_BGR2RGB)
    # Plotting image with subplot() from plt
    plt.subplot(1, 1, 1)
    for x in range(0, len(xy)):
        plt.scatter(xy[x][0], xy[x][1] , s=50)
    # Displaying image in the output

    plt.imshow(imaging_rgb)
    plt.show()




table(dots())
