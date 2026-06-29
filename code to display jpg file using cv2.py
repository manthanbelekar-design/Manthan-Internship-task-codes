import cv2

# Read JPG image
img = cv2.imread("image.jpg")

# Display image
cv2.imshow("JPG Image", img)

# Wait until a key is pressed
cv2.waitKey(0)

# Close window
cv2.destroyAllWindows()