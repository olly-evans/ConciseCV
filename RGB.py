import cv2

# Read the image
image = cv2.imread("C:\\Users\\evans\\OneDrive\\Desktop\\Python\\RGB Channels\\sistinechapel.jpg")

# Display the image in a window, iamge is 800x348
#cv2.imshow("Image", image)

# Wait until a key is pressed, then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

blue, red, green = cv2.split(image)

# One list in the list is 800 elements, there are 348 lists.
rows = len(blue)
print(rows)
col = len(blue[0])
print(col)