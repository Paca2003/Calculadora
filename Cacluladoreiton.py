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


while True:
    while True: 
        try:
            #solicitud de variable
            print("----------------------------------------------")
            op=int(input("\n¿Qué operación matemática desea realizar?\n\nOpción 1:\tSuma.\nOpción 2:\tResta\nOpción 3:\tMultiplicación\nOpción 4:\tDivisión\nOpción 5:\tSalir\n\nSeleccione el número de la opción escogida:\n/"));
        except ValueError:
            #mensaje de error
            print("----------------------------------------------")
            print("Digíte una opción correcta");
        else:
            if op < 1 or op > 5:
                print("----------------------------------------------")
                print("Digíte una opción correcta");
            else:
                break;

    if op == 1:
        while True:
            try:    
                print("----------------------------------------------")
                num1 = int(input("Ingrese el primer numero que desee sumar\n"))
            except ValueError:
                print("----------------------------------------------")
                print("Numero no valido, vuelva a ingresar")
            else:
                break;

        while True:
            try:    
                print("----------------------------------------------")
                num2 = int(input("Ingrese el segundo numero que desee sumar\n"))
            except ValueError:
                print("----------------------------------------------")
                print("Numero no valido, vuelva a ingresar")
            else:
                break;
        print("----------------------------------------------")
        print(f"El resultado de la suma es: {sumar(num1,num2)}")

    elif op == 2:
        while True:
            try:    
                print("----------------------------------------------")
                num1 = int(input("Ingrese el primer numero que desee restar\n"))
            except ValueError:
                print("----------------------------------------------")
                print("Numero no valido, vuelva a ingresar")
            else:
                break;

        while True:
            try:    
                print("----------------------------------------------")
                num2 = int(input("Ingrese el segundo numero que desee restar\n"))
            except ValueError:
                print("----------------------------------------------")
                print("Numero no valido, vuelva a ingresar")
            else:
                break;
        print("----------------------------------------------")
        print(f"El resultado de la resta es: {restar(num1,num2)}")

    elif op == 3:
        while True:
            try:    
                print("----------------------------------------------")
                num1 = int(input("Ingrese el primer numero que desee multiplicar\n"))
            except ValueError:
                print("----------------------------------------------")
                print("Numero no valido, vuelva a ingresar")
            else:
                break;

        while True:
            try:    
                print("----------------------------------------------")
                num2 = int(input("Ingrese el segundo numero que desee multiplicar\n"))
            except ValueError:
                print("----------------------------------------------")
                print("Numero no valido, vuelva a ingresar")
            else:
                break;
        print("----------------------------------------------")
        print(f"El resultado de la multiplicación es: {Mult(num1,num2)}")
    
    elif op == 4:
        while True:
            try:    
                print("----------------------------------------------")
                num1 = int(input("Ingrese el primer numero que desee dividir\n"))
            except ValueError:
                print("----------------------------------------------")
                print("Numero no valido, vuelva a ingresar")
            else:
                break;

        while True:
            try:    
                print("----------------------------------------------")
                num2 = int(input("Ingrese el segundo numero que desee dividir\n"))
            except ValueError:
                print("----------------------------------------------")
                print("Numero no valido, vuelva a ingresar")
            else:
                break;
        print("----------------------------------------------")
        print(f"El resultado de la divición es: {Div(num1,num2)}")

    if op == 5:
        break;