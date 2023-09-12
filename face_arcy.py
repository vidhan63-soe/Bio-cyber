import cv2
import face_recognition
import os

# Load the test image
test_image = face_recognition.load_image_file('gg1.jpeg')

# Encode the faces in the test image
test_face_encodings = face_recognition.face_encodings(test_image)

# List to store match percentages
match_percentages = []

# Iterate over the images in the test_set directory
for filename in os.listdir('target_set'):
    # Load each image from the test_set directory
    target_image = face_recognition.load_image_file(os.path.join('target_set', filename))

    # Encode the faces in the target image
    target_face_encodings = face_recognition.face_encodings(target_image)

    # Iterate over the face encodings in the target image
    for target_encoding in target_face_encodings:
        # Compare the face encoding of the test image with the target encoding
        match = face_recognition.compare_faces([target_encoding], test_face_encodings[0])
        
        # Calculate the percentage match
        match_percentage = sum(match) / len(match) * 100
        
        # Append the match percentage to the list
        match_percentages.append(match_percentage)

# Calculate the average match percentage
average_match_percentage = sum(match_percentages) / len(match_percentages)

# Display the average match percentage
print(f"Average match percentage: {average_match_percentage}%")

