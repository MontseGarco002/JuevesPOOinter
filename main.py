from cosas import *
def main():
    l1=Libro.libro_planeta("El perfume", Autor("Patrick","PS"), 1980)
    #Cambiar seudonimo
    l1.autor.seudonimo = l1.autor.seudonimo.lower()
    print(l1)


    print("------------Herencia------------")
    al2 = Alumno("José", 19, 31899672)
    al2.nombre="Pepé"
    print(al2)

main()