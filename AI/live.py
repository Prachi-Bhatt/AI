import cv2

# Function to apply the cartoon effect to an image
def apply_cartoon_effect(img):
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply median blur to smooth the image
    blur = cv2.medianBlur(gray, 5)

    # Detect edges in the image using adaptive thresholding
    edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # Apply bilateral filter to smooth the image while keeping the edges sharp
    color = cv2.bilateralFilter(img, 9, 250, 250)

    # Combine the color image with the edges to create the cartoon effect
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon

# Initialize video capture object
cap = cv2.VideoCapture(0)

# Loop over frames of the live video feed
while True:
    # Read frame from video capture
    ret, frame = cap.read()

    # Apply cartoon effect to the frame
    cartoon = apply_cartoon_effect(frame)

    # Display the cartoonified frame
    cv2.imshow("Cartoonified Video", cartoon)

    # Wait for key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
