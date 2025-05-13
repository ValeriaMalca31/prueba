from pyDatalog import pyDatalog

# Inicializar términos
pyDatalog.create_terms('progenitor, hombre, mujer, hermano, abuelo, abuela, tio, tia, Z, P, P1, P2, X, Y')

# Definir Hechos de Progenitor
+ progenitor('Juan', 'Carlos')
+ progenitor('Maria', 'Carlos')
+ progenitor('Juan', 'Luisa')
+ progenitor('Maria', 'Luisa')
+ progenitor('Carlos', 'Pedro')
+ progenitor('Ana', 'Pedro')
+ progenitor('Carlos', 'Miguel')
+ progenitor('Ana', 'Miguel')

# Definir Hechos de Género
+ hombre('Juan')
+ hombre('Carlos')
+ hombre('Pedro')
+ hombre('Miguel')

+ mujer('Maria')
+ mujer('Luisa')
+ mujer('Ana')

# Regla para Identificar Hermanos
hermano(X, Y) <= progenitor(P, X) & progenitor(P, Y) & (X != Y)

# Regla para Identificar Abuelos y Abuelas
abuelo(X, Y) <= progenitor(X, Z) & progenitor(Z, Y) & hombre(X)
abuela(X, Y) <= progenitor(X, Z) & progenitor(Z, Y) & mujer(X)

# Regla para Identificar Tios y Tias
tio(X, Y) <= hermano(X, P) & progenitor(P, Y) & hombre(X)
tia(X, Y) <= hermano(X, P) & progenitor(P, Y) & mujer(X)

def mostrar_relaciones():
    print("---- Hermanos ----")
    print(hermano(X, Y))

    print("\nNietos de Juan")
    print(abuelo('Juan', Y))

    print("\n---- Tía de Pedro ----")
    print(tia(X, 'Pedro'))

if __name__ == "__main__":
    mostrar_relaciones()