print ("Hola ¡bienvenido!")
nombre = input("¿cual es tu nombre? ")
print ("hola", nombre, "un gusto en saludarte")
edad = input("que edad tienes? ")
print ("¡genial!")
hobby = input("¿Cuál es tu hobby favorito? ")
if hobby.lower() == "leer":
    print("¡Qué interesante! Leer es una gran forma de aprender.")
else:
    print("¡Genial! Es bueno tener pasatiempos que disfrutes.")
    resiclo = input(" ¿que residuo reciclas mas en tu hogar? ")
if resiclo.lower() == "plastico":
    print("Que excelente el plastico es uno de los mas reciclados por la comunidad. ")
else:

    print("Que buena manera de reciclar te felicito. ")
def menu():
    print("Selecciona lo que deseas reciclar:")
    print("1. PLASTICO")
    print("2. CARTON")
    print("3. VIDRIO")
    print("4. METAL")
    choice = input("Ingresa el número de tu elección: ")
    if choice == '1':
        print("Tu seleccion es PLASTICO, exelente")
    elif choice == '2':
        print("Tu seleccion es CARTON, exelente")
    elif choice == '3':
        print("Tu seleccion es VIDRIO, exelente")
    elif choice == '4':
        print("Tu seleccion es METAL, exelente")
    else:
        print("Opción no válida, por favor intenta de nuevo.")
menu()
choice = input("Estas seguro de tu elección: ")
def menu():
    print("1. Sí")
    print("2. NO")
if choice == '1':    
    print("estupenda eleccion.")
elif choice == '2':
    print("estas seguro de tu decision?.")
else:
    print("Opción no válida, por favor intenta de nuevo.")

paises = ["Colombia", "Argentina", "Venezuela", "Chile", "Perú"]

print("Conozcamonos mas ¿de donde eres?:")
for i, pais in enumerate(paises, 1):
    print(f"{i}. {pais}")
choice = input("Ingresa el Pais: ")
try:
    choice = int(choice)
    
    if 1 <= choice <= len(paises):
        print("Exelente")
    else:
        print("Opción fuera de rango, por favor intenta de nuevo.")
except ValueError:
    print("Entrada no válida. Por favor ingresa un número.")

print("selecciona el departamento: ")

departamento = ["Tolima", "Valle", "Antioquia", "Cundinamarca"]
for i, pais in enumerate(departamento, 1):
    print(f"{i}. {pais}")
choice = input("Departamento: ")
try:
    choice = int(choice)
    
    if 1 <= choice <= len(paises):
        print(f"Tu seleccion es: {departamento[choice - 1]}")
    else:
        print("Opción fuera de rango, por favor intenta de nuevo.")
except ValueError:
    print("Entrada no válida. Por favor ingresa un número.")

print("Selecciona la Ciudad: ")

Ciudad = ["Ibague", "Espinal", "Venadillo", "Lerida", "Chaparral"]
for i, pais in enumerate(Ciudad, 1):
    print(f"{i}. {pais}")
choice = input("Ciudad: ")
try:
    choice = int(choice)
    
    if 1 <= choice <= len(paises):
        print(f"Tu seleccion es: {Ciudad[choice - 1]}")
    else:
        print("Opción fuera de rango, por favor intenta de nuevo.")
except ValueError:
    print("Entrada no válida. Por favor ingresa un número.")

print("que Bueno conocerte ")

def registrar_usuario():
    print("Registro de Usuario")
    
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    correo_electronico = input("Ingresa tu correo electrónico: ")
    contraseña = input("Ingresa tu contraseña: ")
    confirmar_contraseña = input("Confirma tu contraseña: ")
    if contraseña == confirmar_contraseña:
        usuario = {
            "Nombre de usuario": nombre_usuario,
            "Correo electrónico": correo_electronico,
            "Contraseña": contraseña
        }
        print("Usuario registrado con éxito!")
        print(f"Información del usuario: {usuario}")
    else:
        print("Las contraseñas no coinciden. Por favor, intenta de nuevo.")
registrar_usuario()
