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

# Clase base abstracta para representar a una mascota registrada en la veterinaria
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


# Clase concreta que representa a un cliente de la veterinaria
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

# Clase concreta que representa una cita médica de una mascota
class CitaMascota(Cita):
    def actualizar(self, **kwargs):
        for clave, valor in kwargs.items():
            if hasattr(self, clave):
                setattr(self, clave, valor)

# Clase principal que administra el sistema de la veterinaria
class SistemaVeterinaria:
    def __init__(self):
        self.clientes = [] # Lista de clientes registrados en la veterinaria

    # Función para registrar clientes
    def registrar_cliente(self):
        try:
            nombre = input("Ingrese el nombre del cliente: ").strip() 
            contacto = input("Ingrese el contacto: ").strip()
            direccion = input("Ingrese la dirección: ").strip()

            if not nombre or not contacto or not direccion:
                raise ValueError("Todos los campos son obligatorios.")

            cliente = Cliente(nombre, contacto, direccion) 
            self.clientes.append(cliente) 
            print("¡Cliente registrado con éxito!")
        except ValueError as e:
            print(f"Error: {e}")

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

    # Función para actualizar información del cliente
    def actualizar_cliente(self):
        try:
            nombre_cliente = input("Ingrese el nombre del cliente a actualizar: ").strip()
            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente), None)

            if not cliente:
                raise ValueError("Cliente no encontrado.")

            print("Deje en blanco los campos que no desea actualizar.")
            nuevo_contacto = input("Nuevo contacto: ").strip()
            nueva_direccion = input("Nueva dirección: ").strip()

            if nuevo_contacto:
                cliente.contacto = nuevo_contacto
            if nueva_direccion:
                cliente.direccion = nueva_direccion

            print("¡Información del cliente actualizada con éxito!")
        except ValueError as e:
            print(f"Error: {e}")

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

    # Función para eliminar el registro de una mascota, ya sea por error en el registro o fallecimiento de la mascota
    def eliminar_mascota(self):
        try:
            nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
            nombre_mascota = input("Ingrese el nombre de la mascota a eliminar: ").strip()

            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente), None)
            if not cliente:
                raise ValueError("Cliente no encontrado.")

            mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)
            if not mascota:
                raise ValueError("Mascota no encontrada.")

            cliente.mascotas.remove(mascota)
            print(f"Mascota '{nombre_mascota}' eliminada con éxito.")
        except ValueError as e:
            print(f"Error: {e}")

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

    # Función para programar una cita
    def programar_cita(self):
        try:
            nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
            nombre_mascota = input("Ingrese el nombre de la mascota: ").strip()

            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente), None)
            if not cliente:
                raise ValueError("Cliente no encontrado.")

            mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)
            if not mascota:
                raise ValueError("Mascota no encontrada.")

            fecha = input("Ingrese la fecha (AAAA-MM-DD): ").strip()
            hora = input("Ingrese la hora (HH:MM): ").strip()
            servicio = input("Ingrese el servicio (consulta, vacunación, etc.): ").strip()
            veterinario = input("Ingrese el nombre del veterinario: ").strip()

            datetime.strptime(fecha, "%Y-%m-%d")
            datetime.strptime(hora, "%H:%M")
            
            if not servicio or not veterinario: 
                raise ValueError("Detalles de la cita inválidos.")

            cita = CitaMascota(fecha, hora, servicio, veterinario)
            mascota.agregar_al_historial(cita)
            print("¡Cita programada con éxito!")
        except ValueError as e:
            print(f"Error: {e}")
    
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

    # Función para cancelar una cita de una mascota
    def cancelar_cita(self):
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
                raise ValueError("No hay citas registradas para esta mascota.")

            print("Citas disponibles para cancelar:")
            for i, cita in enumerate(mascota.historial_citas):
                print(f"{i + 1}: {cita.fecha} - {cita.hora} - {cita.servicio} - {cita.veterinario}")

            indice = int(input("Seleccione el número de la cita a cancelar: ").strip()) - 1
            if indice < 0 or indice >= len(mascota.historial_citas):
                raise ValueError("Selección inválida.")

            cita_cancelada = mascota.historial_citas.pop(indice)
            print(f"Cita del {cita_cancelada.fecha} a las {cita_cancelada.hora} cancelada con éxito.")
        except ValueError as e:
            print(f"Error: {e}")

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

    # Función para buscar citas según una fecha específica
    def buscar_citas_por_fecha(self):
        try:
            fecha_busqueda = input("Ingrese la fecha a buscar (AAAA-MM-DD): ").strip()

            datetime.strptime(fecha_busqueda, "%Y-%m-%d")  # Validar formato de fecha

            citas_encontradas = []
            for cliente in self.clientes:
                for mascota in cliente.mascotas:
                    for cita in mascota.historial_citas:
                        if cita.fecha == fecha_busqueda:
                            citas_encontradas.append((cliente.nombre, mascota.nombre, cita))

            if not citas_encontradas:
                print("No hay citas en esa fecha.")
            else:
                print("\nCitas encontradas:")
                for cliente, mascota, cita in citas_encontradas:
                    print(f"Cliente: {cliente}, Mascota: {mascota}, Servicio: {cita.servicio}, Veterinario: {cita.veterinario}")
        except ValueError as e:
            print(f"Error: {e}")

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

    # While para crear opciones
    def iniciar(self):
        while True:
            print("\nSistema de Gestión Veterinaria")
            print("1. Registrar Cliente")
            print("2. Eliminar Cliente")
            print("3. Actualizar Cliente")
            print("4. Registrar Mascota")
            print("5. Eliminar Mascota")
            print("6. Actualizar Mascota")
            print("7. Programar Cita")
            print("8. Actualizar Cita")
            print("9. Cancelar Cita")
            print("10. Consultar Historial")
            print("11. Consultar Citas por Fecha")
            print("12. Generar Reporte de Clientes")
            print("13. Salir")
            
            opcion = input("Ingrese su opción: ").strip()
            
            if opcion == "1":
                self.registrar_cliente()
            elif opcion == "2":
                self.eliminar_cliente()
            elif opcion == "3":
                self.actualizar_cliente()
            elif opcion == "4":
                self.registrar_mascota()
            elif opcion == "5":
                self.eliminar_mascota()
            elif opcion == "6":
                self.actualizar_mascota()
            elif opcion == "7":
                self.programar_cita()
            elif opcion == "8":
                self.actualizar_cita()
            elif opcion == "9":
                self.cancelar_cita()
            elif opcion == "10":
                self.consultar_historial()
            elif opcion == "11":
                self.buscar_citas_por_fecha()
            elif opcion == "12":
                self.generar_reporte_clientes()
            elif opcion == "13":
                print("Saliendo del sistema. ¡Adiós!")
                break
            else:
                print("Opción inválida. Por favor, intente de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    sistema = SistemaVeterinaria()
    sistema.iniciar()