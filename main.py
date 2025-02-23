from abc import ABC, abstractmethod
from datetime import datetime

# Clase base abstracta para representar a una persona (cliente de la veterinaria) - Felipe
class Persona(ABC):  
    def __init__(self, nombre, contacto, direccion):
        self.nombre = nombre
        self.contacto = contacto
        self.direccion = direccion

    @abstractmethod
    def mostrar_informacion(self):
        pass

# Clase base abstracta para representar a una mascota registrada en la veterinaria - Edinson
class Mascota(ABC): 
    def __init__(self, nombre, especie, raza, edad):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.historial_citas = [] # Lista para almacenar citas médicas

    @abstractmethod
    def agregar_al_historial(self, detalles_servicio):
        pass

# Clase base abstracta para representar una cita médica para una mascota - Felipe
class Cita(ABC):
    pass

# Clase concreta que representa a un cliente de la veterinaria - Edinson
class Cliente(Persona):
    def __init__(self, nombre, contacto, direccion):
        super().__init__(nombre, contacto, direccion)
        self.mascotas = []

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def mostrar_informacion(self):
        return f"Cliente: {self.nombre}, Contacto: {self.contacto}, Dirección: {self.direccion}"

# Clase concreta para el registro de una mascota en el sistema - Felipe
class RegistroMascota(Mascota):
    pass

# Clase concreta que representa una cita médica de una mascota - Edinson
class CitaMascota(Cita):
    pass

# Clase principal que administra el sistema de la veterinaria - Felipe
class SistemaVeterinaria:

    # Función para registrar clientes - Edinson
    def registrar_cliente(self):
        pass

    # Función para eliminar clientes - Felipe  
    def eliminar_cliente(self):
        pass

    # Función para actualizar información del cliente - Edinson
    def actualizar_cliente(self):
        pass

    # Función para registar mascota asociada al correspondiente cliente - Felipe
    def registrar_mascota(self): 
        pass

    # Función para eliminar el registro de una mascota, ya sea por error en el registro o fallecimiento de la mascota - Edinson
    def eliminar_mascota(self):
        pass

    # Función para actualizar información de las mascotas - Felipe
    def actualizar_mascota(self):
        pass

    # Función para programar una cita - Edinson
    def programar_cita(self):
        pass
    
    # Función para actualizar una cita - Felipe
    def actualizar_cita(self):
        pass

    # Función para cancelar una cita de una mascota - Edinson
    def cancelar_cita(self):
        pass

    # Función para consultar historial según una mascota específica - Felipe
    def consultar_historial(self):
        pass

    # Función para buscar citas según una fecha específica - Edinson
    def buscar_citas_por_fecha(self):
        pass

    # Función para generar un reporte de clientes con sus respectivas mascotas - Felipe
    def generar_reporte_clientes(self):
        pass

    # While para crear opciones - Edinson
    def iniciar(self):
        pass

# Punto de entrada del programa
if __name__ == "__main__":
    sistema = SistemaVeterinaria()
    sistema.iniciar()