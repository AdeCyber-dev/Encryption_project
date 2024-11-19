import tkinter as tk
from tkinter import filedialog
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import os

# Generate a random key for encryption using a password
def generate_key(password):
    salt = os.urandom(16)
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1, backend=default_backend())
    key = kdf.derive(password.encode())
    return key, salt

# Encrypt the image
def encrypt_image(file_path, password):
    key, salt = generate_key(password)

    with open(file_path, 'rb') as f:
        image_data = f.read()

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(image_data) + padder.finalize()

    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    with open(file_path + '.enc', 'wb') as f:
        f.write(salt + iv + encrypted_data)

    print(f"Image {file_path} encrypted successfully!")

# Decrypt the image
def decrypt_image(file_path, password):
    with open(file_path, 'rb') as f:
        file_data = f.read()

    salt = file_data[:16]
    iv = file_data[16:32]
    encrypted_data = file_data[32:]

    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1, backend=default_backend())
    key = kdf.derive(password.encode())

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    decrypted_file_path = file_path.replace('.enc', '_decrypted.png')
    with open(decrypted_file_path, 'wb') as f:
        f.write(unpadded_data)

    print(f"Image {decrypted_file_path} decrypted successfully!")

# Use Tkinter to select a file
def select_image_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title="Select an Image File", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    return file_path

# Example usage
if __name__ == "__main__":
    # Ask the user to select an image file to encrypt
    image_path = select_image_file()
    if image_path:
        password = input("Enter a password for encryption: ")
        encrypt_image(image_path, password)

        # Ask the user to decrypt
        decrypt = input("Would you like to decrypt the image? (yes/no): ")
        if decrypt.lower() == "yes":
            decrypt_image(image_path + '.enc', password)
