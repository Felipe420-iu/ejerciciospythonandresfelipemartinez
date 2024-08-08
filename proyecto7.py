# Ejercicio 5
#Desarrolle un algoritmo que Programa que calcule el precio final de una compra, dado el valor de la compra y un descuento. Para esto es necesario declarar dos variables, una que guarde el valor de la compra y otra que almacene el valor del descuento. El algoritmo debe mostrar en pantalla, el valor de la compra el valor del descuento y el valor final a pagar.
# Declarar las variables del valor de la compra y el descuento
valor_compra = input("ingresa el valor de la compra") # Puedes cambiar este valor de compra
descuento = input("ingresa el descuento")  # Puedes cambiar el descuento
# Calcular el precio final
precio_final = valor_compra - descuento
# Imprimir los resultados
print(f"La compra fue {valor_compra}, con un descuento de {descuento}, y el valor final a pagar es {precio_final}.")
