# Este es el arcivo python en el cual mis companeros y yo trabajaremos para
# Crear una calculadora de manera colaborativa

#Suma
def sumar(numero1, numero2):
    resultado=numero1+numero2;
    return resultado;

#Resta
def restar(numero1, numero2):
    resultado=numero1-numero2;
    return resultado;

#Multiplicar
def Mult(num1,num2):
    return num1*num2;

#Dividir
def Div(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return "SYNTAX ERROR"


# Version nueva