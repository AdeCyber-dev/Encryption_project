from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives import hashes
import os

# Generate a random key for encryption using a password
def generate_key(password):
    salt = os.urandom(16)
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1, backend=default_backend())
    key = kdf.derive(password.encode())
    return key, salt

# Encrypt the image
def encrypt_image(file_path, password):
    # Generate encryption key and salt
    key, salt = generate_key(password)

    # Read the image file as binary
    with open(file_path, 'rb') as f:
        image_data = f.read()

    # Create AES cipher
    iv = os.urandom(16)  # Initialization Vector
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Add padding to the image data
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(image_data) + padder.finalize()

    # Encrypt the image data
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Save the encrypted data along with the IV and salt
    with open(file_path + '.enc', 'wb') as f:
        f.write(salt + iv + encrypted_data)

    print(f"Image {file_path} encrypted successfully!")

# Decrypt the image
def decrypt_image(file_path, password):
    # Read the encrypted file
    with open(file_path, 'rb') as f:
        file_data = f.read()

    # Extract the salt, IV, and encrypted data
    salt = file_data[:16]
    iv = file_data[16:32]
    encrypted_data = file_data[32:]

    # Derive the key from the password and salt
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1, backend=default_backend())
    key = kdf.derive(password.encode())

    # Create AES cipher for decryption
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the data
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Remove padding
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    # Save the decrypted image
    decrypted_file_path = file_path.replace('.enc', '_decrypted.png')
    with open(decrypted_file_path, 'wb') as f:
        f.write(unpadded_data)

    print(f"Image {decrypted_file_path} decrypted successfully!")

# Example usage:
# Encrypt the image
encrypt_image('example_image.png', 'my_secure_password')

# Decrypt the image
decrypt_image('example_image.png.enc', 'my_secure_password')
