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
        next(lector) # Saltar la cabecera
        ret = []
        for tipo, fechahora, ubicacion, duracion, calorias, \
            distancia, frecuencia, compartido in lector:

            fechahora = datetime.strptime(fechahora, "%d/%m/%Y %H:%M")
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            compartido = (compartido == 'S')

            tupla = Entreno(tipo, fechahora, ubicacion, duracion, \
                        calorias, distancia, frecuencia, compartido)

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
    Recibe la lista de entrenos y un entero d, y devuelve una nueva
    lista de entrenos con todos los que tengan duración superior a d
    '''
    ret = []
    for u in entrenos:
        if u.duracion > d:
            ret.append(u)

    return ret

def suma_calorias(entrenos: list[Entreno], f_inicio: str, f_fin: str) -> int:
    '''
    Recibe la lista de entrenos y un intervalo de dos fechas,
    y devuelve la suma de calorías quemadas en los entrenos
    comprendidos en dicho intervalo, inclusive los extremos
    '''

    f_inicio = datetime.strptime(f_inicio, "%d/%m/%Y %H:%M")
    f_fin = datetime.strptime(f_fin, "%d/%m/%Y %H:%M")
    suma = 0
    for u in entrenos:
        if f_inicio <= u.fechahora <= f_fin:
            suma += u.calorias

    return suma

def entrenamiento_mas_kms(entrenos: list[Entreno]) -> Entreno:
    '''
    Recibe la lista de entrenos y devuelve el entreno
    con mayor distancia recorrida
    '''
    max = entrenos[0]
    for u in entrenos:
        if u.distancia > max.distancia:
            max = u
    
    return max

def duracion_media_entrenos(entrenos: list[Entreno], año: int, mes: int) -> int:
    '''
    Recibe la lista de entrenos, un año y un mes, y
    devuelve la duración media de los entrenos en ese
    mes y año.
    Si la media no se puede calcular, devuelve None.
    '''
    suma = 0
    num = 0
    for u in entrenos:
        año_entreno = u.fechahora.year
        mes_entreno = u.fechahora.month
        if año == año_entreno and mes == mes_entreno:
            suma += u.duracion
            num += 1

    if num == 0:
        return None
    else:
        return suma / num