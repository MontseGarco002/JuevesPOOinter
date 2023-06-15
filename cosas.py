class Autor:
    def _init_(self, nom, seudo):
        self.__nombre = nom
        self.__seudonimo = seudo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nom):
        self.__nombre = nom

    @property
    def seudonimo(self):
        return self.__seudonimo

    @nombre.setter
    def seudonimo(self, seudo):
        self.__seudonimo = seudo

    def __str__(self):
        return f"Nombre {self._nombre}, pseudonimo: {self._seudonimo}"

    def escribir(self):
        print(f"{self.__seudonimo} esta escribiendo su siguiente obra")


class Libro:
    def _init_(self, tit, aut, an, edi):
        self.__titulo = tit
        self.__autor = aut
        self.__anio = an
        self.__editorial = edi

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, tit):
        self.__titulo = tit

    @property
    def autor(self):
        return self.__autor
    @autor.setter
    def autor(self,aut):
        self.__autor = aut

    @property
    def anio(self):
        return self.__anio
    @anio.setter
    def anio(self, an):
        self.__anio = an

    @property
    def editorial(self):
        return self.__editorial

    @editorial.setter
    def editorial(self, edi):
        self.__editorial = edi

    def __str__(self):
        return f"""
                Titulo: {self.__titulo}
                Autor: {self.__autor}
                Editorial: {self.__editorial}
                Año: {self.__anio}
                """

    @classmethod
    def libro_planeta(cls, titulo, autor, anio):
        return cls(titulo, autor, anio, "planeta")

    def leer(self, minutos):
        print(f"leyendo por {minutos} minutos")


class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nom):
        self.__nombre = nom

class Alumno(Persona):
    def __init__(self,nombre, edad, number_cuenta, carrera, promedio):
        super().__init__(nombre,edad)
        self.__numero_cuenta = number_cuenta
        self.__carrera = carrera
        self.__promedio = promedio
