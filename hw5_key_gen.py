import rsa
import argparse

#genereerib võtmed ja salvestab need kahte erinevasse faili
def generate_keys():
    try:
        (public_key, private_key) = rsa.newkeys(512)
        with open("public_key.txt", "w") as pub_file:
            pub_file.write(public_key.save_pkcs1("PEM").decode()) 
        with open("private_key.txt", "w") as priv_file:
            priv_file.write(private_key.save_pkcs1("PEM").decode())
        print("Võtmed edukalt genereeritud!")
    except Exception as e:
        print(f"Viga võtmete genereerimisel: {e}")

#võtab sisendiks faili ja privaatvõtme, krüpteerib faili sisu ja salvestab selle uude faili, vea puhul edastab veateate
def encrypt_file(file_path, private_key):
    try:
        with open(file_path, "r") as file:
            text = file.read()
        encrypted_text = rsa.encrypt(text.encode(), private_key)
        with open("encrypted_text.txt", "wb") as enc_file:
            enc_file.write(encrypted_text)
        print("Tekst krüpteeritud ja salvestatud faili 'encrypted_text.txt'")
    except Exception as e:
        print(f"Viga teksti krüpteerimisel {e}")

#võtab sisendiks faili ja privaatvõtme, dekrüpteerib faili sisu ja salvestab selle uude faili, vea puhul edastab veateate
def decrypt_file(file_path, private_key):
    try:
        with open(file_path, "rb") as file:
            enc_text = file.read()
        decrypted_text = rsa.decrypt(enc_text, private_key)
        with open("decrypted_text.txt", "w") as dec_file:
            dec_file.write(decrypted_text.decode())
        print("Tekst dekrüpteeritud ja salvestatud faili 'decrypted_text.txt'")
    except Exception as e:
        print(f"Viga teksti dekrüpteerimisel: {e}")

#käivitab programmi, võtab kasutajalt sisendi ja käivitab vastava funktsiooni
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RSA key generation and encryption/decryption.")
    parser.add_argument("--generate-keys", action="store_true")
    parser.add_argument("--encrypt-file", type=str)
    parser.add_argument("--decrypt-file", type=str)
    args = parser.parse_args()

#kui kasutaja sisestab käsureale --generate-keys, siis käivitatakse võtmete genereerimise funktsioon
    if args.generate_keys:
        generate_keys()
#kui kasutaja sisestab käsureale --encrypt-file ja faili nime, siis käivitatakse faili krüpteerimise funktsioon
    if args.encrypt_file:
        try:
            with open("private_key.txt", "r") as priv_file:
                #laetakse privaatvõti
                private_key = rsa.PrivateKey.load_pkcs1(priv_file.read().encode())
            encrypt_file(args.encrypt_file, private_key)
        except Exception as e: #kui tekib viga, siis väljastatakse veateade
            print(f"Viga faili dekrüpteerimisel: {e}")
#kui kasutaja sisestab käsureale --decrypt-file ja faili nime, siis käivitatakse faili dekrüpteerimise funktsioon
    if args.decrypt_file:
        try:
            with open("private_key.txt", "r") as priv_file:
                private_key = rsa.PrivateKey.load_pkcs1(priv_file.read().encode()) #laetakse privaatvõti
            decrypt_file(args.decrypt_file, private_key) #dekrüpteeritakse fail
        except Exception as e: #kui tekib viga, siis väljastatakse veateade
            print(f"Viga faili dekrüpteerimisel: {e}")
