import random

NOMBRES = [
    'Ana',
    'Pedro',
    'Pablo',
    'Ernesto',
    'Ariel',
    'Carlos',
    'Luis',
    'Oscar',
    'Alicia',
    'Maria',
    'Brenda'
]

CIUDADES = [
    'Managua',
    'Masaya',
    'Matagalpa',
    'Chinandega',
    'Somoto',
    'Rivas'
]


def generar_diccionario_estudiantes():
    estudiantes = {}

    for nombre in NOMBRES:
        estudiantes[nombre] = {
            'edad': random.randrange(16, 30),
            'anio': random.randrange(1, 5),
            'ciudad': random.choice(CIUDADES)
        }

    return estudiantes
if __name__ == '__main__':
    diccionario = generar_diccionario_estudiantes()
    for llave,valor in diccionario.iteritems():
        print llave,valor

mensaje = 'El estudiante  {nombre} con la edad de: {edad}, que cursa el {anio} anio y que habita en la ciudad de {ciudad}'

for nombre_estudiante, datos in diccionario.iteritems():
    print mensaje.format(nombre=nombre_estudiante, edad=datos['edad'],anio=datos['anio'], ciudad = datos['ciudad'])
    f = open('peralta.txt', 'a')
    f.write(mensaje.format(nombre=nombre_estudiante, edad=datos['edad'], anio=datos['anio'], ciudad=datos['ciudad']))
    f.close()
mensaje = 'se mencionan los estudiantes {nombre} de la ciudad de {ciudad}'

for nombre_estudiante, datos in diccionario.iteritems():
    if datos['ciudad'] == 'Managua':
        print mensaje.format(nombre=nombre_estudiante,ciudad=datos['ciudad'])
        f = open('alexa.txt', 'a')
        f.write(mensaje.format(nombre=nombre_estudiante, edad=datos['edad'],anio=datos['anio'], ciudad = datos['ciudad']))
        f.close()