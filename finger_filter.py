import cv2

def match_fingerprints(image1_path, image2_path):
    # Read the fingerprint images
    image1 = cv2.imread(image1_path, 0)  # Read the first image in grayscale
    image2 = cv2.imread(image2_path, 0)  # Read the second image in grayscale

    # Initialize the ORB (Oriented FAST and Rotated BRIEF) detector
    orb = cv2.ORB_create()

    # Find the keypoints and descriptors for the fingerprint images
    keypoints1, descriptors1 = orb.detectAndCompute(image1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(image2, None)

    # Initialize the brute-force matcher
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match the descriptors of the keypoints
    matches = bf.match(descriptors1, descriptors2)

    # Sort the matches by their distance
    matches = sorted(matches, key=lambda x: x.distance)

    # Calculate the percentage of matched keypoints
    total_keypoints = min(len(keypoints1), len(keypoints2))
    matched_keypoints = len(matches)
    match_percentage = (matched_keypoints / total_keypoints) * 100

    return match_percentage

# Example usage
image1_path = 'finger1.jpeg'
image2_path = '5.jpeg'

percentage = match_fingerprints(image1_path, image2_path);
print('Fingerprint match percentage:', percentage)

