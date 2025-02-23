from abc import ABC, abstractmethod
from datetime import datetime

# Clase base abstracta para representar a una persona (cliente de la veterinaria)
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

# Clase base abstracta para representar una cita médica para una mascota
class Cita(ABC):
    def __init__(self, fecha, hora, servicio, veterinario):
        self.fecha = fecha
        self.hora = hora
        self.servicio = servicio
        self.veterinario = veterinario

    @abstractmethod
    def actualizar(self, **kwargs):
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

# Clase concreta para el registro de una mascota en el sistema
class RegistroMascota(Mascota):  
    def agregar_al_historial(self, detalles_servicio):
        self.historial_citas.append(detalles_servicio)

    def obtener_historial(self):
        return self.historial_citas

# Clase concreta que representa una cita médica de una mascota - Edinson
class CitaMascota(Cita):
    pass

# Clase principal que administra el sistema de la veterinaria
class SistemaVeterinaria:
    def __init__(self):
        self.clientes = [] # Lista de clientes registrados en la veterinaria

    # Función para registrar clientes - Edinson
    def registrar_cliente(self):
        pass

    # Función para eliminar clientes
        try:
            nombre_cliente = input("Ingrese el nombre del cliente a eliminar: ").strip()
            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente), None)

            if not cliente:
                raise ValueError("Cliente no encontrado.")

            self.clientes.remove(cliente)
            print(f"Cliente '{nombre_cliente}' eliminado con éxito.")
        except ValueError as e:
            print(f"Error: {e}")

    # Función para actualizar información del cliente - Edinson
    def actualizar_cliente(self):
        pass

    # Función para registar mascota asociada al correspondiente cliente
    def registrar_mascota(self): 
        try:
            nombre_cliente = input("Ingrese el nombre del cliente al que asociar la mascota: ").strip()
            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente), None)

            if not cliente:
                raise ValueError("Cliente no encontrado.")

            nombre_mascota = input("Ingrese el nombre de la mascota: ").strip()
            especie = input("Ingrese la especie: ").strip()
            raza = input("Ingrese la raza: ").strip()
            edad = int(input("Ingrese la edad: ").strip())

            if not nombre_mascota or not especie or not raza or edad <= 0:
                raise ValueError("Detalles de la mascota inválidos.")

            mascota = RegistroMascota(nombre_mascota, especie, raza, edad) 
            cliente.agregar_mascota(mascota)
            print("¡Mascota registrada con éxito!")
        except ValueError as e:
            print(f"Error: {e}")

    # Función para eliminar el registro de una mascota, ya sea por error en el registro o fallecimiento de la mascota - Edinson
    def eliminar_mascota(self):
        pass

    # Función para actualizar información de las mascotas
    def actualizar_mascota(self):
        try:
            nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
            nombre_mascota = input("Ingrese el nombre de la mascota a actualizar: ").strip()

            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente), None)
            if not cliente:
                raise ValueError("Cliente no encontrado.")

            mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)
            if not mascota:
                raise ValueError("Mascota no encontrada.")

            print("Deje en blanco los campos que no desea actualizar.")
            nueva_especie = input("Nueva especie: ").strip()
            nueva_raza = input("Nueva raza: ").strip()
            nueva_edad = input("Nueva edad: ").strip()

            if nueva_especie:
                mascota.especie = nueva_especie
            if nueva_raza:
                mascota.raza = nueva_raza
            if nueva_edad.isdigit():
                mascota.edad = int(nueva_edad)

            print("¡Información de la mascota actualizada con éxito!")
        except ValueError as e:
            print(f"Error: {e}")

    # Función para programar una cita - Edinson
    def programar_cita(self):
        pass
    
    # Función para actualizar una cita
    def actualizar_cita(self):
        try:
            nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
            nombre_mascota = input("Ingrese el nombre de la mascota: ").strip()
            
            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente), None)
            if not cliente:
                raise ValueError("Cliente no encontrado.")

            mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)
            if not mascota:
                raise ValueError("Mascota no encontrada.")
            
            if not mascota.historial_citas:
                raise ValueError("No hay citas registradas para esta mascota")
            
            print("Citas disponibles para actualizar:")
            for i, cita in enumerate(mascota.historial_citas):
                print(f"{i + 1}: Fecha: {cita.fecha}. Hora: {cita.hora}. Servicio: {cita.servicio}. Veterinario: {cita.veterinario}")
                
            indice = int(input("Seleccione el número de la cita a actualizar: ").strip()) -1
            if indice < 0 or indice >= len(mascota.historial_citas):
                raise ValueError("Selección invalida")
            
            cita = mascota.historial_citas[indice]
            
            print("Deje en blanco los campos que no desea actualizar")
            nueva_fecha = input("Nueva fecha (AAAA-MM-DD): ").strip()
            nueva_hora = input("Nueva hora (HH:MM): ").strip()
            nuevo_servicio = input("Nuevo servicio: ").strip()
            nuevo_veterinario = input("Nuevo veterinario: ").strip()
            
            if nueva_fecha:
                datetime.strptime(nueva_fecha, "%Y-%m-%d")
                cita.actualizar(fecha = nueva_fecha)
            if nueva_hora:
                datetime.strptime(nueva_hora, "%H:%M")
                cita.actualizar(hora = nueva_hora)
            if nuevo_servicio:
                cita.actualizar(servicio = nuevo_servicio)
            if nuevo_veterinario:
                cita.actualizar(veterinario = nuevo_veterinario)
            
            print("¡Cita actualizada con éxito!")
        except ValueError as e:
            print(f"Error: {e}")

    # Función para cancelar una cita de una mascota - Edinson
    def cancelar_cita(self):
        pass

    # Función para consultar historial según una mascota específica
    def consultar_historial(self):
        try:
            nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
            nombre_mascota = input("Ingrese el nombre de la mascota: ").strip()
            
            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente), None)
            if not cliente:
                raise ValueError("Cliente no encontrado.")

            mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)
            if not mascota:
                raise ValueError("Mascota no encontrada.")
            
            historial = mascota.obtener_historial()
            if not historial:
                print("No hay historial disponible para esta mascota. ")
            else:
                for entrada in historial:
                    print(f"Fecha: {entrada.fecha}. Hora: {entrada.hora}. Servicio: {entrada.servicio}. Veterinario: {entrada.veterinario}")
        except ValueError as e:
            print(f"Error: {e}")

    # Función para buscar citas según una fecha específica - Edinson
    def buscar_citas_por_fecha(self):
        pass

    # Función para generar un reporte de clientes con sus respectivas mascotas
    def generar_reporte_clientes(self):
        print("\n🔹 Reporte de Clientes y sus Mascotas 🔹")
        for cliente in self.clientes:
            print(f"\nCliente: {cliente.nombre}, Contacto: {cliente.contacto}, Dirección: {cliente.direccion}")
            if cliente.mascotas:
                for mascota in cliente.mascotas:
                    print(f"  - Mascota: {mascota.nombre}, Especie: {mascota.especie}, Raza: {mascota.raza}, Edad: {mascota.edad}")
            else:
                print("  - No tiene mascotas registradas.")

    # While para crear opciones - Edinson
    def iniciar(self):
        pass

# Punto de entrada del programa
if __name__ == "__main__":
    sistema = SistemaVeterinaria()
    sistema.iniciar()