import cv2
import os

# Directory paths
face_db_dir = "face_db"
target_set_dir = "target_set"

# Load Haar cascade xml classifier
haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Process each image in the face_database directory
for filename in os.listdir(face_db_dir):
    img_path = os.path.join(face_db_dir, filename)

    # Read the image
    img = cv2.imread(img_path)

    # Convert image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply face detection
    faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=9)

    # Check if any faces are detected
    if len(faces_rect) > 0:
        print(f"Detected face in {filename}")
        # Move the image to the target_set directory
        target_path = os.path.join(target_set_dir, filename)
        os.rename(img_path, target_path)

# Display the filtered images in the target_set directory
for filename in os.listdir(target_set_dir):
    img_path = os.path.join(target_set_dir, filename)
    img = cv2.imread(img_path)
    cv2.imshow('Detected faces', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

