import random

class JuegoAdivinanza():
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.conteo_intentos = 0

    def validarNumero(self, numero):
        if numero > self.numero_secreto:
            return "El número ingresado es mayor al número secreto."
        elif numero < self.numero_secreto:
            return "El número ingresado es menor al número secreto."
        else:
            return "El número ingresado es igual al número secreto. Felicidades, has ganado."

    def registrarIntento(self):
        self.conteo_intentos += 1

    def reiniciar(self):
        self.numero_secreto = random.randint(1, 100)
        self.conteo_intentos = 0

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = []

    def registro(self, intentos, resultado):
        self.historial.append((intentos, resultado))

    def mostrar_estadisticas(self):
        try:
            with open(f"estadisticas_{self.nombre}.txt", "r") as archivo:
                historial = archivo.readlines()

            if not historial:
                print("No se ha jugado aún.")
                return

            partidas_totales = len(historial)

            if partidas_totales == 0:
                print("No se ha jugado aún.")
                return

            ganes = sum(1 for linea in historial if "True" in linea)
            porcentaje = (ganes / partidas_totales) * 100

            print(f"Partidas jugadas: {partidas_totales}")
            print(f"Partidas ganadas: {ganes}")
            print(f"Porcentaje de victorias: {porcentaje:.2f}%")

        except FileNotFoundError:
            print(f"No se encontró el archivo de estadísticas para {self.nombre}.")

    def guardar_estadisticas(self):
        with open(f"estadisticas_{self.nombre}.txt", "w") as archivo:
            for intentos, resultado in self.historial:
                archivo.write(f"Intentos: {intentos}, Gano: {resultado}\n")
            partidas_totales = len(self.historial)
            ganes = sum(1 for intentos, resultado in self.historial if resultado)
            porcentaje = (ganes / partidas_totales) * 100 if partidas_totales > 0 else 0
            archivo.write(f"Partidas jugadas: {partidas_totales}\n")
            archivo.write(f"Partidas ganadas: {ganes}\n")
            archivo.write(f"Porcentaje de victorias: {porcentaje:.2f}%\n")

    def cargar_estadisticas(self):
        try:
            with open(f"estadisticas_{self.nombre}.txt", "r") as archivo:
                for linea in archivo:
                    if linea.startswith("Partidas") or linea.startswith("Porcentaje"):
                        continue
                    intentos, resultado = linea.strip().split(", ")
                    self.registro(intentos, resultado == "True")
        except FileNotFoundError:
            print(f"No se encontró el archivo de estadísticas para {self.nombre}.")

def jugar():
    while True:
        print("\nMenu: ")
        print("1. Comenzar una nueva partida.")
        print("2. Ver las estadísticas del jugador.")
        print("3. Salir del juego.")

        opcion = input("Seleccione una opción: ").strip()

        jugador = input("Ingrese su nombre: ")
        jugador_registro = Jugador(jugador)
        jugador_registro.cargar_estadisticas()

        if opcion == '1':
            juego = JuegoAdivinanza()
            print(f"\nBienvenido {jugador_registro.nombre}. Tendrás 10 intentos para adivinar el número secreto. Comenzaremos una nueva partida pronto...")

            while True:
                try:
                    numero = int(input("Adivina un número entre el 1 y 100: "))
                    if numero < 1 or numero > 100:
                        print("Por favor ingrese únicamente un número entre el 1 y el 100.")
                        continue

                    juego.registrarIntento()
                    respuesta = juego.validarNumero(numero)
                    print(respuesta)

                    if respuesta == "El número ingresado es igual al número secreto. Felicidades, has ganado.":
                        jugador_registro.registro(juego.conteo_intentos, True)
                        print(f"Para adivinar el número secreto necesitaste {juego.conteo_intentos} intentos.")
                        jugador_registro.guardar_estadisticas()
                        jugador_registro.cargar_estadisticas()
                        False

                    if juego.conteo_intentos >= 10:
                        print(f"No lograste adivinar el número. El número secreto era {juego.numero_secreto}.")
                        jugador_registro.registro(juego.conteo_intentos, False)
                        jugador_registro.guardar_estadisticas()
                        False

                except ValueError:
                    print("Por favor, ingrese un número válido.")
                    continue

            # Vuelve al menú principal después de que termine una partida
            continue

        elif opcion == '2':
            jugador_registro.mostrar_estadisticas()

        elif opcion == '3':
            jugador_registro.guardar_estadisticas()
            print("Gracias por jugar a adivinar el número secreto. ¡Vuelve pronto!")
            False

        else:
            print("Opción no válida.")

jugar()

