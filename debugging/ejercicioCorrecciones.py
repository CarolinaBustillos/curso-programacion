#Codigo del ejercicio de debugging

def calcular_promedio(numeros): 
    total = sum(numeros) / len(numeros) 
    print(f"Promedio: {total}") #Imrime el promedio para poder comparar visualmente
    return total

def comparar_con_promedio(numeros, promedio):
    for num in numeros:
        if num > promedio: #Falta : al final
            print(f"{num} es mayor que el promedio.")
        elif num < promedio: #Falta : al final
            print(f"{num} es menor que el promedio.")
        else: #Falta : al final
            print(f"{num} es igual al promedio.")

# Pedir al usuario tres números
numeros = []
for i in range(3):
    num = float(input("Introduce un número: ")) #Se agrega un float para trabajar con números enteros o decimales
    numeros.append(num)

# Calcular el promedio
promedio = calcular_promedio(numeros)

# Comparar cada número con el promedio
comparar_con_promedio(numeros, promedio)
