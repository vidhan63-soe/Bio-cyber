from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from PIL import Image

def decrypt_file(file_path, image_path, output_file_path):
    # Load the image and convert it to grayscale
    image = Image.open(image_path).convert('L')
    image_data = image.tobytes()

    # Generate a 256-bit key from the image data
    key = SHA256.new(image_data).digest()

    # Load the encrypted file
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    # Create an AES cipher object using the derived key
    cipher = AES.new(key, AES.MODE_ECB)

    # Decrypt the data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Remove the padding from the decrypted data
    decrypted_data = decrypted_data.rstrip(b'\x00')

    # Write the decrypted data to the output file
    with open(output_file_path, 'wb') as file:
        file.write(decrypted_data)

    print("File decrypted successfully!")

# Example usage
encrypted_file_path = "/home/vidhan/Desktop/Biometric/encrypted_secret.txt"
decryption_key_image_path = "/home/vidhan/Desktop/Biometric/lookalike.png"
decrypted_output_file_path = "/home/vidhan/Desktop/Biometric/decrypted_secret.txt"

decrypt_file(encrypted_file_path, decryption_key_image_path, decrypted_output_file_path)

