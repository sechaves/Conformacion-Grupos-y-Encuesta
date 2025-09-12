#Autor: Sergio Gabriel Chaves Mosquera
#Asignación: Encuesta conformación de grupos
#Objetivo del programa: Recoja información mediante una encuesta a sus compañeros..


# Clase principal Encuesta

class Encuesta:
    def __init__(self):
        self.preguntas = (
            "¿Cómo te llamas?",
            "¿Cuántos años tienes?",
            "¿En qué carrera estás?",
            "¿En qué semestre?",
            "¿Tienes alguna idea para el proyecto?",
            "¿Te sientes comod@ trabajando en equipo?"
        )
        self.respuestas = []

    def agregar_respuesta(self):
        respuestas_estudiante = []
        for pregunta in self.preguntas:
            respuesta = input(pregunta + " ")
            respuestas_estudiante.append(respuesta)

        # Crear objeto Estudiante
        estudiante = Estudiante(
            nombre=respuestas_estudiante[0],
            edad=respuestas_estudiante[1],
            respuesta_proyecto=respuestas_estudiante[4]
        )
        self.respuestas.append((estudiante, respuestas_estudiante))

    def mostrar_resultados(self):
        print("\n--- Resultados de la encuesta ---\n")
        for estudiante, respuestas in self.respuestas:
            print(f"{estudiante.nombre} ({estudiante.edad} años) respondió:")
            for r in respuestas[2:]:
                print("  -", r)
            print()  

#Clase secundaria Estudiante
class Estudiante:
    def __init__(self, nombre, edad, respuesta_proyecto):
        self.nombre = nombre
        self.edad = edad
        self.respuesta_proyecto = respuesta_proyecto

# Ejecución main y métodos
def main():
    encuesta = Encuesta()
    for numero_encuestado in range(10):
        print(f"\nEncuestado #{numero_encuestado+1}")
        encuesta.agregar_respuesta()
    encuesta.mostrar_resultados()
if __name__ == "__main__":
    main()