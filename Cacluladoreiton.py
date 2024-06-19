# Este es el arcivo python en el cual mis companeros y yo trabajaremos para
# Crear una calculadora de manera colaborativa


def Mult(num1,num2):
    return num1*num2;

def Div(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return "SYNTAX ERROR"


