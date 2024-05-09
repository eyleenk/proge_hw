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
Loodud programm, mis salvestab sisestatud kasutajanime ja parooli koodis olevasse andmebaasi, millesse on võimalik pärast sisse logida
Vajalikud moodulid: mysql-connector-python

- Programm võtab sisendina kasutajanime ja parooli;
- hashib parooli SHA-256 algoritmi abil;
- kontrollib, kas antud kasutajanimi on juba olemas andmebaasis, selle puudumisel, lisab andmed tabelisse.

- Sisselogides võtab sisendid ja hashib parooli sarnaselt;
- kontrollib andmebaasist, kas kasutajanimi ja parool vastavad eelnevalt sisestatud andmetele;
- kui vastavus leitakse, trükib "Sisselogimine õnnestus"; vastasel juhul trükib "Sisselogimine ebaõnnestus".

- Andmebaasiühenduse sulgemiseks tuleb valida lõpuks kolmas valik.

- Andmebaasi muutmine on lihtsasti teostatav, muutes lihtsalt 4.-8. rea teavet.
- NB! Praegu kasutusel oleva tasuta andmebaasiga tuleb looja meili kaudu uuendada oma soovi seda lahti hoida, muidu suletakse see hiljem. (ei peaks olema probleem XAMPP või muude andmebaasidega)

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
