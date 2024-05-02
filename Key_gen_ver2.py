import rsa
import argparse

def generate_keys():
    try:
        (pubkey, privkey) = rsa.newkeys(2048)
        with open('public_key.txt', 'w') as pub_file:
            pub_file.write(pubkey.save_pkcs1('PEM').decode())
        with open('private_key.txt', 'w') as priv_file:
            priv_file.write(privkey.save_pkcs1('PEM').decode())
        print("Võtmed edukalt genereeritud!")
    except Exception as e:
        print(f"Viga võtmete genereerimisel: {e}")

def encrypt_file(file_path, pub_key):
    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()
        encrypted_content = rsa.encrypt(file_content, pub_key)
        with open('encrypted_file.txt', 'wb') as enc_file:
            enc_file.write(encrypted_content)
        print("Fail krüpteeritud ja salvestatud faili 'encrypted_file.txt'")
    except Exception as e:
        print(f"Viga teksti krüpteerimisel: {e}")

def decrypt_file(file_path, priv_key):
    try:
        with open(file_path, 'rb') as file:
            encrypted_content = file.read()
        decrypted_content = rsa.decrypt(encrypted_content, priv_key)
        with open('decrypted_file.txt', 'wb') as dec_file:
            dec_file.write(decrypted_content)
        print("Fail dekrüpteeritud ja salvestatud faili 'decrypted_file.txt'")
    except Exception as e:
        print(f"Viga faili dekrüpteerimisel: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='RSA key generation and encryption/decryption.')
    parser.add_argument('--generate-keys', action='store_true')
    parser.add_argument('--encrypt-file', type=str)
    parser.add_argument('--decrypt-file', type=str)
    args = parser.parse_args()

    if args.generate_keys:
        generate_keys()

    if args.encrypt_file:
        try:
            with open('public_key.txt', 'r') as pub_file:
                pub_key = rsa.PublicKey.load_pkcs1(pub_file.read().encode())
            encrypt_file(args.encrypt_file, pub_key)
        except Exception as e:
            print(f"Viga faili krüpteerimisel: {e}")

    if args.decrypt_file:
        try:
            with open('private_key.txt', 'r') as priv_file:
                priv_key = rsa.PrivateKey.load_pkcs1(priv_file.read().encode())
            decrypt_file(args.decrypt_file, priv_key)
        except Exception as e:
            print(f"Viga faili dekrüpteerimisel: {e}")