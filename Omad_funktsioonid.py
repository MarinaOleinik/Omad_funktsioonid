from Modul import *
while True:
    print("Funktsioonid".center(50,"+"))
    print("arithmetic- A,\nis_year_leap-Y")
    v=input()
    if v.upper()=="A":
        arv1=float(input("Arv 1:"))
        arv2=float(input("Arv 2:"))
        sym=input("Tehe:")
        rezult=arithmetic(arv1,arv2,sym)
        print(rezult)
    elif v.upper()=="Y":
        rezult=is_year_leap(int(input("Sisesta aasta: ")))
        print(rezult)
    elif v.upper()=="X":
        print("Kodeerimine".center(60,"*"))
        rezult=xor_cipher(input("Sisesta text: "), input("Sisesta võti: "))
        print(rezult)
        print("Dekodeerimine".center(60,"*"))
        de_rezult=xor_uncipher(rezult, input("Sisesta võti: "))
        print(de_rezult)
