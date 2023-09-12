import cv2
import os

# Path to the test fingerprint image
test_fingerprint_path = "finger1.jpeg"

# Load the test fingerprint image
test_fingerprint = cv2.imread(test_fingerprint_path)

# Display the test fingerprint image
cv2.imshow("Test Fingerprint", test_fingerprint)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Path to the database folder
database_folder = "./database"

# Constants for matching threshold and minutiae count
matching_threshold = 10  # Adjust this value based on your algorithm
minutiae_count = 20  # Adjust this value based on your algorithm

# Iterate over the fingerprint images in the database folder
for filename in os.listdir(database_folder):
    # Construct the full path to the fingerprint image
    fingerprint_path = os.path.join(database_folder, filename)

    # Load the fingerprint image from the database
    database_fingerprint = cv2.imread(fingerprint_path)

    # Perform fingerprint matching (use your desired matching algorithm here)
    # Your code for fingerprint matching goes here
    # Calculate the number of matching minutiae points
    matching_minutiae_count = 0  # Replace this with the actual result

    # Calculate the accuracy percentage
    #accuracy_percentage = (matching_minutiae_count / minutiae_count) * 100

    # Display the matched fingerprint and print the result
    cv2.imshow("Matched Fingerprint", database_fingerprint)
    print("Fingerprint matched: " + filename)
    #print("Accuracy: {:.2f}%".format(accuracy_percentage))

    cv2.waitKey(0)
    cv2.destroyAllWindows()

