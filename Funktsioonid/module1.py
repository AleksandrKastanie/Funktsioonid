def arithmetic(number1:float, number2:float, argument:str):
    """Saab teha +,-,*,/ ja tagastab kui vastus on arv ja  "Tundmatu tehe",
    kui ei saa vastust leida või sestatud ehe ei ole ["+", "-", "/","*"].
    :param float number1: Esimine arv
    :param float number2: Teine arv
    :param str argument: Aritmeetilise tehe
    :rtype: var
    """
    if c in ["+", "-", "/","*"]:
        if argument == "/":
            if number1==0:
                vastus="Div/0"
            else:
                vastus=number1/number2
        elif argument =="*":
            vastus=number1*number2
        elif argument =="+":
            vastus==number1+number2
        elif argument=="-":
            vastus== number1-number2
    else:
        vastus="Неизвестная операция"
    return vastus