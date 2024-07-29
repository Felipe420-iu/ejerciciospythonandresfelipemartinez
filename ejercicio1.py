mensaje= "hola, estoy aprendiendo python"
nombre= "felipe"
formacion= "adso"
edad= 24
estatura= 1.75
peso=70
#forma de imprimir 1
print(mensaje, "mi nombre es:", nombre, "soy de la formacion:", formacion, "tengo:", edad, "años:", "mido:", estatura, "y peso:",peso, "kg" ) 
#forma de imprimir 2
print(f'{mensaje}. mi nombre es: {nombre}, soy de la formacion: {formacion}, tengo: {edad},años, mido: {estatura}, y peso: {peso} kg')

a=10
b=5
suma= a + b
resta= a - b
multiplicacion= a * b
division_cociente= a // b
division_residuo= a % b
print("suma:", suma, "resta:", resta, "multiplicacion:", multiplicacion, "division cociente", division_cociente, "division residuo", division_residuo)
print(f" suma, {suma}, resta, {resta}, multiplicacion, {multiplicacion}, division cociente, {division_cociente}, division residuo, {division_residuo}")
'''
HOLA EJERCICIO DATOS POR TECLADO
'''
a=int(input("digite un valor: "))
b=int(input("digite otro valor: "))
print(f" el resultado de la suma es: {a+b} el resultado de la resta es: {a-b} el resultado de la multiplicacion es: {a*b} el resultado de la division cociente es: {a//b} el resultado de la division residuo es: {a%b}")
 
