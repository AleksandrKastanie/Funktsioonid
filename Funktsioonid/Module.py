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