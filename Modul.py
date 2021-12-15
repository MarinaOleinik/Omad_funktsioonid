def arithmetic(a: float,b:float,c:str):
    """Lihtne kalkulaator
    + - liitmine, - - lahutamine, * - korrutamine,/ - jagamine
    :param float a: Esimene arv
    :param float b: Teine arv
    :param str c: Aritmeetiline tehing
    :rtype: var Märamata tüüb
    """
    if c in ["+","-","*","/"]:
        if c=="/" and b==0:
            vastus="Div/0"
        else:
            vastus=eval(str(a)+c+str(b))
    else:
        vastus="Tundmatu tehe!"
    return vastus

def is_year_leap(aasta: int):
    """Liigaasta leidmine
    Tagastab True kui aasta on liigaasta ja False kui ei ole
    :param int aasta: Aasta number
    :rtype: bool Funktsioni vastus loogilises formaadis
    """
    if aasta%4==0:
        vastus=True
    else:
        vastus=False
    return vastus
def season(kuu:int)->str:
    """Пишем от 1 до 12 месяцев и программа определяет сезон по месяцам
    :param int kuu: kuu järjekordne number
    :rtype str: hooaja nimetus
    """
    if kuu==12 or 0<kuu<3:
        rez="Talv"
    elif 2<kuu<6:
        rez="Kevad"
    elif 5<kuu<9:
        rez="Suvi"
    elif 8<kuu<12:
        rez="Sügis"
    else:
        rez="Viga!"
    return rez
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