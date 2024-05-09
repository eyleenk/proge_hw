1. ülesande link https://www.codewars.com/kata/514b92a657cdc65150000006
2. ülesande link https://www.codewars.com/kata/551b4501ac0447318f0009cd/python
3. Ülesande link https://www.codewars.com/kata/558fc85d8fd1938afb000014
4. Ülesande link https://www.codewars.com/kata/55f8a9c06c018a0d6e000132
5. Ülesande link: https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d
6. Ülesande link: https://www.codewars.com/kata/52597aa56021e91c93000cb0
____________________________________________________________________________________________________________________________________________________________________________________________
3. Kodutöö
Plussid - kood kergesti arusaadav, piisavalt lühike, töötaks erinevate elementidega. Ei muuda algseid liste, mida võib hilisemas koodis veel vaja minna.

Miinused - kui listid pikemad, võtab kaua aega. Samamoodi suurusega, kui listid pikemad, siis failid mahukamad. Listi printimine vajalik ainult koodi kontrollimiseks, otseselt pole vajalik.

Hoidla on forkitud ja merge'tud.
Koostatud project issue ja pull request.

Analüüsi koostanud: Eyleen Krikk ja René Vainula
____________________________________________________________________________________________________________________________________________________________________________________________
4. Kodutöö
  
Autorid Eyleen Krikk ja René Vainula
____________________________________________________________________________________________________________________________________________________________________________________________
5. Kodutöö
Loodud programm RSA võtmete genereerimiseks ja teksti krüpteerimiseks ja dekrüpteerimiseks.

Käivitamiseks vajalikud pluginad: rsa, argparse.

-Programm genereerib avaliku ja privaatse võtme ja salvestab need failidesse public_key.txt ja private_key.txt.

-Programm krüpteerib sisestatud teksti kasutades privaatset võtit ja salvestab krüpteeritud teksti faili encrypted_text.txt

-Programm dekrüpteerib krüpteeritud teksti ja salvestab faili nimega decrypted_file.txt.

NB! kontrolli, et programmifail on samas kaustas, kuhu võtmed luuakse. Kui pole, kasuta käsku cd (change directory) tühik uusasukoht. N: cd Desktop.


Võtmete genereerimiseks: python key_gen.py --generate-keys

Faili krüpteerimiseks: python key_gen.py --encrypt-file "failinimi.txt"

Faili dekrüpteerimiseks: python key_gen.py --decrypt-file "failinimi.txt"

ver2 genereerib võtmed, krüpteerib kasutades public võtit ja dekrüpteerib kasutades private võtit. ver2 kasuta commande python key_gen_ver2.py

Autorid Eyleen Krikk ja René Vainula
________________________________________________________________________________________________________________________________________________________________________________________________
