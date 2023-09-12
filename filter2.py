import os
import face_recognition
import shutil

# Directory containing the images
image_directory = "target_set"

# Reference face image
reference_image = "gg1.jpeg"

# Load the reference face image
reference_face = face_recognition.load_image_file(reference_image)
reference_face_encoding = face_recognition.face_encodings(reference_face)[0]

# Create a directory for the reference face
reference_face_directory = os.path.join(image_directory, "Most_probable_face")
os.makedirs(reference_face_directory, exist_ok=True)

# Iterate over all the images in the directory
for filename in os.listdir(image_directory):
    if filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".png"):
        # Load the current image
        image_path = os.path.join(image_directory, filename)
        current_image = face_recognition.load_image_file(image_path)

        # Find the face(s) in the current image
        face_locations = face_recognition.face_locations(current_image)
        face_encodings = face_recognition.face_encodings(current_image, face_locations)

        # Compare the face(s) with the reference face
        for face_encoding in face_encodings:
            face_distance = face_recognition.face_distance([reference_face_encoding], face_encoding)

            # Check if the face is similar to the reference face
            if face_distance < 0.6:
                # Move the image to the reference face directory
                shutil.move(image_path, os.path.join(reference_face_directory, filename))
                break

