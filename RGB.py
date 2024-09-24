import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("C:\\Users\\evans\\OneDrive\\Desktop\\Python\\RGB Channels\\sistinechapel.jpg")
assert image is not None, "file could not be read, check with os.path.exists()"

# Stupid method just finds the frequency values :(
hist = cv2.calcHist([image], [2], None, [256], [0, 256])
print(hist)