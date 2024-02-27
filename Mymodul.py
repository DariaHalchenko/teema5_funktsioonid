from typing import Type

def arifmetic(arv1:int, arv2:int, argument):
    if argument == "-":
        s = arv1 - arv2
    elif argument == "+":
        s = arv1 + arv2
    elif argument == "/":
        if arv2 == 0:
            print("vale andmed(null)")
        else:
             s = arv1 / arv2  
    elif argument == "*":
        s = arv1 * arv2       
        return s







