from math import*
def Kolmnurga_pindala(külg:float, kõrgus:float):
    """leiab kolmnurga pindala. On antud kõrgus ja külje pikkus. Tagastab Sfloat formaadis
    :param float külg: Kolmnurga külje pikkus
    :param float kõrgus: Kõrgus vastav küljele
    :rtype: var
    """
    if külg<0 or kõrgus<0:
        s="valed andmed!"
    else:
        s=0.5*külg*kõrgus

    return s
def arithmetic(num1:float, num2:float, argument:str):
    """Saab teha +,-,*,/ ja tagastab kui vastus on arv ja  "Tundmatu tehe",
    kui ei saa vastust leida või sestatud ehe ei ole ["+", "-", "/","*"].
    :param float number1: Esimine arv
    :param float number2: Teine arv
    :param str argument: Aritmeetilise tehe
    :rtype: var
    """
    if argument in ["+", "-", "/","*"]:
        if argument == "/" and num1==0:
             vastus="Div/0"
        elif argument == "/":
             vastus = num1 / num2
        elif argument =="*":
            vastus=num1 * num2
        elif argument =="+":
            vastus= num1 + num2
        elif argument=="-":
            vastus=num1 - num2
    else:
        vastus="Неизвестная операция"
    return vastus
def ruud (a:float):
    """
    :rtype:  float, float, float
    :param float a: ruudu külg
    """
    while 1: 
        d=a*sqrt(2)
        P=a*4
        S=a*a
    return P,S,d
def season (kuu:int)->str:
    """
    Võtame kuu umber ja tagastame tekst: Talv, Kevad, Suvi või Sügis.
    """
    while 1:
        if kuu>=1 and kuu<=12:
           if kuu in [1,2,12]:
              s="Talv"
           elif kuu in [3,4,5]:
              s="Kevad"
           elif kuu in [6,7,8]:
              s="Suvi"
           else:
              s="Sügis"
           break
        else:
           kuu=int(input("vale kuu, sissestage usesti: "))
    return s
def bank(a:float, years:int)->float:
    """
    Рассчитываем сумму с годовыми от нашего вклада 
    :param float a: вклад
    :param int years: срок в годах  
    :rtype: a float 
    """
    if a >=0:
        for i in range (years):
            a*=1.1
    else:
        a="Сумма не может быть отрицательной!"
    return a
def is_prime(a:int)->bool:
    """
    peate leidma algarvud vahemikus 0 kuni 1000
    :param a int: arv 
    :rtype:  a int 
    """
    t=0 
    for i in range (1, arv+1):
        if arv%i==0: t+=1
    if t==2:
        t=True
    else:
        t=False
    return t 


