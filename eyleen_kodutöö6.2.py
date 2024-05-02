def move_zeros(lst):#defineerib fn(move_zeros) võttes lst argumendiks
    non_zeros= [] #loob tühja listi, kus mitte nullid
    zeros= [] #loob teise tühja listi, kus nullid
    for i in lst: #iga liikme kohta lst'is
        if i != 0: #kui element listis pole 0, lisab selle non zeros listi
            non_zeros.append(i)
        else: #kui on 0, lisab nullide(zeros) listi
            zeros.append(i)       
    return non_zeros + zeros #tagastab tulemuse, kus nullid lõpus
