# Este es el arcivo python en el cual mis companeros y yo trabajaremos para
# Crear una calculadora de manera colaborativa

#Definir funciones

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


# Version nuev
while True:
    try:
        #solicitud de variable
        op=int(input("\n¿Qué operación matemática desea realizar?\n\nOpción 1:\tSuma.\nOpción 2:\tResta\nOpción 3:\tMultiplicación\nOpción 4:\tDivisión\nOpción 5:\tSalir\n\nSeleccione el número de la opción escogida:\n/"));
    except ValueError:
        #mensaje de error
        print("*Digíte una opción correcta*");
    else:
        #Opciones menú
        print("hola");
    