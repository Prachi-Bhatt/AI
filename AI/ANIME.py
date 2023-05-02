import cv2

cap = cv2.VideoCapture(0)  # 0 for default camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1020)

while True:
    ret, frame = cap.read()

    # Apply a bilateral filter to smooth the image while preserving edges
    filtered = cv2.bilateralFilter(frame, 9, 75, 75)

    # Convert the image to grayscale
    gray = cv2.cvtColor(filtered, cv2.COLOR_BGR2GRAY)

    # Apply a median blur to further smooth the image
    blurred = cv2.medianBlur(gray, 11)

    # Apply adaptive thresholding to create a black and white image
    thresholded = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    # Add bilateral filtering back to the image to create a "painted" look
    color_filtered = cv2.bilateralFilter(frame, 9, 75, 75)

    # Combine the thresholded image with the color filtered image to create a cartoon effect
    cartoon = cv2.bitwise_and(color_filtered, color_filtered, mask=thresholded)

    cv2.imshow('Cartoonized Video Feed', cartoon)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
