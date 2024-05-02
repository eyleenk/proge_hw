# loob argumendi num ja arvutab kõikide arvude summa, mis jagunevad 5 või 3'ga
def solution(num):
    if num < 0:
        return 0
#muutuja väärtus 0, hakkab koguma kriteeriumitele vastavaid väärtusi
    summa2 = 0
    #kontrollib, kas iga ranges olev väärtus jagub 3 või 5'ga
    for i in range(num):
        #kui jäägiks on 0, siis jagub ja arv sobib
        if i % 3 == 0 or i % 5 == 0:
            #kui arv sobib, liidetakse kõik sobivad arvud kokku
            summa2 += i

    return summa2
