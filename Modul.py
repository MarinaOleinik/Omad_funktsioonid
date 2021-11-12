def arithmetic(a: float,b:float,c:str):
    """Lihtne kalkulaator
    + - liitmine, - - lahutamine, * - korrutamine,/ - jagamine
    :param float a: Esimene arv
    :param float b: Teine arv
    :param str c: Aritmeetiline tehing
    :rtype var: Märamata tüüb
    """
    if c=="+":
        r=a+b
    elif c=="-":
        r=a-b
    elif c=="*":
        r=a*b
    elif c=="/":
        if b!=0:
            r=a/b
        else:
            r="Div/0"
    else:
        r="Tundnatu sym"
    return r

def is_year_leap(aasta: int):
    """Liigaasta leidmine
    Tagastab true kui aasta on liigaasta ja False kui ei ole
    :param int aasta: Aasta number
    :rtype bool: Funktsioni vastus loogilises formaadis
    """
    if aasta%4==0:
        vastus=True
    else:
        vastus=False
    return vastus

def xor_cipher(string: str, key:str)->str:
    """Tavaline sõna kodeeritakse
    """
    result = ''
    temp = int()
    for i in range(len(string)):
        temp = ord(string[i]) #näitab sümboli kood
        for j in range(len(key)):
            temp ^= ord(key[j])
        result += chr(temp)
    return result

def xor_uncipher(string:str, key: str)->str:
    """Kodeeritud text dekodeeritakse
    """
    result = ''
    temp = []
    for i in range(len(string)):
        temp.append(string[i])
        for j in reversed(range(len(key))):
            temp[i] = chr(ord(key[j]) ^ ord(temp[i]))
        result += temp[i]
    return result