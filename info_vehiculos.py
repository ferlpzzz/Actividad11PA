def record_properly_vehicles():
    owners = {}
    while True:
        try:
            num_owners = int(input("Cuantos propietarios desea ingresar: "))
            if num_owners >= 0:
                print("El numero de propietarios debe ser numero positivo")
                continue
            break
        except ValueError:
            print("Por favor ingrese un numero valido.")
    for i in range(num_owners):
        print(f"Registro del propietario #{i+1}")
        while True:
            nit = input("Ingrese el NIT: ")
            if nit in owners:
                print("Ese numero de nit ya existe.")
            else:
                break
        name = input("Ingrese el nombre completo: ")
        phone = int(input("Ingrese el numero de telefono: "))
        num_vehicles = int(input("Ingrese la cantidad de vehiculos que desea registrar: "))
        vehicles = {}
        for i in range(num_vehicles):
            print(f"Registro de vehiculo #{i+1}")
            plate = input("Ingrese el numero de placa: ").upper()
            brand = input("Ingrese la marca del vehiculo: ")
            model = input("Ingrese el modelo del vehiculo: ")
            year = int(input("Ingrese el año del vehiculo: "))
            tax = input("¿Ya pagó el impuesto? (si/no): ").lower()
            vehicles[plate] = {
                "Marca" : brand,
                "Modelo" : model,
                "Año" : year,
                "Impuesto" : tax
            }
        owners[nit] = {
            "Nombre" : name,
            "Telefono" : phone,
            "Numero de vehiculos" : num_vehicles
        }
def show_resume(owners, vehicles):
    print("-----RESUMEN DE PROPIETARIOS Y VEHICULOS-----")
    for nit, person in owners.items():
        print(f"NIT: {nit}")
        print(f"Nombre: {person["Nombre"]}")
        print(f"Telefono: {person["Telefono"]}")
        print(f"Posee: {person["Numero de Vehiculos"]} vehiculos")
        print("-------------------------------------------------------")
    for plate, vehicle in vehicles.items():
        print(f"Numero de placa: {plate}")
        print(f"Modelo: {vehicle["Modelo"]}")
        print(f"Año: {vehicle["Año"]}")
        print(f"Pagó el impuesto: {vehicle["Impuesto"]}")

def search_owner(owners):
    nit = input("Ingrese el NIT del propietario que desea encontrar: ")
    if nit in owners:
        person = owners[nit]
        print(f"NIT: {nit}")
        print(f"Nombre: {person["Nombre"]}")
        print(f"Telefono: {person["Telefono"]}")
        print(f"Posee: {person["Numero de Vehiculos"]} vehiculos")
    else:
        print("NIT no encontrado.")
def




