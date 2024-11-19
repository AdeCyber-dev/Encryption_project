from Crypto.Cipher import AES, DES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

# AES Encryption and Decryption
def aes_encrypt(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + cipher_text).decode()

def aes_decrypt(cipher_text, key):
    cipher_text = base64.b64decode(cipher_text)
    iv = cipher_text[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(cipher_text[AES.block_size:]), AES.block_size)
    return decrypted_text.decode()

# DES Encryption and Decryption
def des_encrypt(plain_text, key):
    cipher = DES.new(key, DES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(plain_text.encode(), DES.block_size))
    return base64.b64encode(cipher.iv + cipher_text).decode()

def des_decrypt(cipher_text, key):
    cipher_text = base64.b64decode(cipher_text)
    iv = cipher_text[:DES.block_size]
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(cipher_text[DES.block_size:]), DES.block_size)
    return decrypted_text.decode()

# RSA Key Generation
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    with open("keys/private_key.pem", "wb") as priv_file:
        priv_file.write(private_key)
    with open("keys/public_key.pem", "wb") as pub_file:
        pub_file.write(public_key)

# RSA Encryption and Decryption
def rsa_encrypt(plain_text, public_key_file):
    with open(public_key_file, 'rb') as pub_file:
        public_key = RSA.import_key(pub_file.read())
    cipher = PKCS1_OAEP.new(public_key)
    cipher_text = cipher.encrypt(plain_text.encode())
    return base64.b64encode(cipher_text).decode()

def rsa_decrypt(cipher_text, private_key_file):
    with open(private_key_file, 'rb') as priv_file:
        private_key = RSA.import_key(priv_file.read())
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_text = cipher.decrypt(base64.b64decode(cipher_text))
    return decrypted_text.decode()

# Example usage
if __name__ == "__main__":
    # AES Example
    aes_key = get_random_bytes(32)  # AES-128 bit key
    aes_encrypted = aes_encrypt("Red team operations are Initial Access, and Reconnaissance weaponization Social Engineering harvesting email addresses and Information In today’s evolving cybersecurity landscape, data protection is paramount and pleased to share my latest project, a multi-faceted cybersecurity suite designed to enhance digital security and promote best practices.", aes_key)
    print(f"AES Encrypted: {aes_encrypted}")
    aes_decrypted = aes_decrypt(aes_encrypted, aes_key)
    print(f"AES Decrypted: {aes_decrypted}")
    
    # DES Example
    des_key = get_random_bytes(16)  # DES key
    des_encrypted = des_encrypt("Red team operations are Initial Access, and Reconnaissance weaponization Social Engineering harvesting email addresses and Information In today evolving cybersecurity landscape, data protection is paramount and pleased to share my latest project, a multi-faceted cybersecurity suite designed to enhance digital security and promote best practices.", des_key)
    print(f"DES Encrypted: {des_encrypted}")
    des_decrypted = des_decrypt(des_encrypted, des_key)
    print(f"DES Decrypted: {des_decrypted}")
    
    # RSA Example
    generate_rsa_keys()
    rsa_encrypted = rsa_encrypt("Red team operations are Initial Access, and Reconnaissance weaponization Social Engineering harvesting email addresses and InformationIn today’s evolving cybersecurity landscape, data protection is paramount and pleased to share my latest project, a multi-faceted cybersecurity suite designed to enhance digital security and promote best practices.", "keys/public_key.pem")
    print(f"RSA Encrypted: {rsa_encrypted}")
    rsa_decrypted = rsa_decrypt(rsa_encrypted,"keys/private_key.pem")
    print(f"RSA Decrypted: {rsa_decrypted}")