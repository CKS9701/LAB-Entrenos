from entrenos import *

def test_lee_entrenos(entrenos):
    print("Probando lee_entrenos()...")
    print(f"Se han leído {len(entrenos)} entrenos.")
    print(f"Los tres primeros entrenos son: {entrenos[:3]}")
    print(f"Los tres primeros entrenos son: {entrenos[-3:]}")

    print()

def test_tipo_entreno(entrenos):
    print("Probando tipo_entreno()...")
    tipos = tipo_entreno(entrenos)
    print(f"Los tipos de entreno que hay son: {tipos}")

    print()

def test_entrenos_duracion_superior(entrenos, d):
    print("Probando entrenos_duracion_superior()...")
    lista = entrenos_duracion_superior(entrenos, d)
    print(f"Los entrenos con duración mayor a {d} son: {lista}")

    print()

def test_suma_calorias(entrenos, f_inicio, f_fin):
    print("Probando suma_calorias()...")
    suma = suma_calorias(entrenos, f_inicio, f_fin)
    f_inicio = datetime.strptime(f_inicio, "%d/%m/%Y %H:%M")
    f_fin = datetime.strptime(f_fin, "%d/%m/%Y %H:%M")
    print(f"La suma de calorías quemadas entre {f_inicio} y {f_fin} es de {suma} calorías.")

    print()

def test_entrenamiento_mas_kms(entrenos):
    print("Probando entrenamiento_mas_kms()...")
    entreno_mas_kms = entrenamiento_mas_kms(entrenos)
    print(f"El entreno con más kilómetros es {entreno_mas_kms}")

    print()

def test_duracion_media_entrenos(entrenos, año, mes):
    print("Probando duracion_media_entrenos()...")
    media = duracion_media_entrenos(entrenos, año, mes)
    print(f"La duración media de los entrenos en el mes {mes} del año {año} es {media}")

    print()

if __name__ == '__main__':
    entrenos = lee_entrenos('../data/entrenos.csv')
    # test_lee_entrenos(entrenos)

    # test_tipo_entreno(entrenos)

    # test_entrenos_duracion_superior(entrenos, 120)

    # test_suma_calorias(entrenos, "28/09/2018 0:00", "25/12/2019 0:00")

    # test_entrenamiento_mas_kms(entrenos)

    test_duracion_media_entrenos(entrenos, 2021, 2)