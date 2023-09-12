from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from PIL import Image

def encrypt_file(file_path, image_path, output_file_path):
    # Load the image and convert it to grayscale
    image = Image.open(image_path).convert('L')
    image_data = image.tobytes()

    # Generate a 256-bit key from the image data
    key = SHA256.new(image_data).digest()

    # Load the file to encrypt
    with open(file_path, 'rb') as file:
        data = file.read()

    # Pad the data to be a multiple of 16 bytes (AES block size)
    data += b'\x00' * (16 - len(data) % 16)

    # Create an AES cipher object using the derived key
    cipher = AES.new(key, AES.MODE_ECB)

    # Encrypt the data
    encrypted_data = cipher.encrypt(data)

    # Write the encrypted data to the output file
    with open(output_file_path, 'wb') as file:
        file.write(encrypted_data)

    print("File encrypted successfully!")

# Example usage
file_path = "/home/vidhan/Desktop/Biometric/secret.txt"
image_path = "/home/vidhan/Desktop/Biometric/gg1.jpeg"
output_file_path = "/home/vidhan/Desktop/Biometric/encrypted_secret.txt"

encrypt_file(file_path, image_path, output_file_path)

