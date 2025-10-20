from entrenos import *

def test_lee_entrenos(entrenos):
    print("Probando lee_entrenos()...")
    print(f"Se han leído {len(entrenos)} entrenos.")
    print()
    for i in range(5):
        print(*entrenos[i])

    print()

if __name__ == '__main__':
    entrenos = lee_entrenos('data/entrenos.csv')
    test_lee_entrenos(entrenos)