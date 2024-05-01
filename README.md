Loodud programm RSA võtmete genereerimiseks ja teksti krüpteerimiseks ja dekrüpteerimiseks.

Käivitamiseks vajalikud pluginad: rsa, argparse.

-Programm genereerib avaliku ja privaatse võtme ja salvestab need failidesse public_key.txt ja private_key.txt.

-Programm krüpteerib sisestatud teksti kasutades privaatset võtit ja salvestab krüpteeritud teksti faili encrypted_text.txt

-Programm dekrüpteerib krüpteeritud teksti ja salvestab faili nimega decrypted_file.txt.

NB! kontrolli, et programmifail on samas kaustas, kuhu võtmed luuakse. Kui pole, kasuta käsku cd (change directory) tühik uusasukoht. N: cd Desktop.


Võtmete genereerimiseks: python key_gen.py --generate-keys

Teksti krüpteerimiseks käsurealt: python key_gen.py --encrypt "Sinu tekst siia."

Teksti krüpteerimiseks failist: python key_gen.py --encrypt-file "failinimi.txt"

Teksti dekrüpteerimiseks: python key_gen.py --decrypt-file "failinimi.txt"

Autorid Eyleen Krikk ja René Vainula.
