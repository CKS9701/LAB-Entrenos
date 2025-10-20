import csv

from collections import namedtuple
Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, ' \
    'duracion, calorias, distancia, frecuencia, compartido')

from datetime import datetime

def lee_entrenos(fichero: str) -> list[Entreno]:
    '''
    Recibe la dirección del fichero y devuelve
    una lista con tuplas de tipo Entreno
    '''
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        ret = []
        for tipo, fechahora, ubicacion, duracion, calorias, \
            distancia, frecuencia, compartido in lector:

            tupla = Entreno(tipo, fechahora, ubicacion, duracion, \
                        calorias, distancia, frecuencia, compartido)

            fechahora = datetime.strptime(fechahora, "%d/%m/%Y %H:%M")
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            compartido = True if (compartido == 'S') else False

            ret.append(tupla)
        
        return ret

def tipo_entreno(entrenos: list[Entreno]) -> list[str]:
    '''
    Recibe la lista de tuplas de tipo Entreno
    y devuelve una lista de los tipos de entreno
    ordenada alfabéticamente y sin elementos
    repetidos
    '''
    entrenos.sort() # Ordenamos la lista
    size = len(entrenos) # Tomamos la longitud de la lista
    ret = [entrenos[0].tipo] # Inicializamos una lista con solo el primer elem.
    for i in range(1, size-1):
        if entrenos[i].tipo != entrenos[i-1].tipo:
            ret.append(entrenos[i].tipo)

    return ret

def entrenos_duracion_superior(entrenos: list[Entreno], d: int) -> list[Entreno]:
    '''
    
    '''
    pass