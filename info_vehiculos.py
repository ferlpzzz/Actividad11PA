def record_properly_vehicles():
    owners = {}
    while True:
        try:
            num_owners = int(input("Cuantos propietarios desea ingresar: "))
            if num_owners <= 0:
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
        while True:
            try:
                phone = int(input("Ingrese el numero de telefono: "))
                break
            except ValueError:
                print("Ingrese un numero valido")
        while True:
            try:
                num_vehicles = int(input("Ingrese la cantidad de vehiculos que desea registrar: "))
                if num_vehicles < 0:
                    print("Debe ingresar un numero valido")
                    continue
                break
            except ValueError:
                print("Ingrese un numero valido")
        vehicles = {}
        for j in range(num_vehicles):
            print(f"Registro de vehiculo #{j+1}")
            plate = input("Ingrese el numero de placa: ").upper()
            brand = input("Ingrese la marca del vehiculo: ")
            model = input("Ingrese el modelo del vehiculo: ")
            year = int(input("Ingrese el año del vehiculo: "))
            tax = input("¿Ya pagó el impuesto? (si/no): ").lower()
            while tax not in ["si", "no"]:
                print("Favor ingresar ´si´ o ´no´")
                tax = input("Pagó el impuesto (si/no)").lower()
            vehicles[plate] = {
                "Marca" : brand,
                "Modelo" : model,
                "Año" : year,
                "Impuesto" : tax
            }
        owners[nit] = {
            "Nombre" : name,
            "Telefono" : phone,
            "Vehiculos" : vehicles
        }
    return owners


def show_resume(owners):
    print("----- RESUMEN DE PROPIETARIOS Y VEHÍCULOS -----")
    for nit, person in owners.items():
        print(f"\nNIT: {nit}")
        print(f"Nombre: {person['Nombre']}")
        print(f"Teléfono: {person['Telefono']}")
        print(f"Vehículos registrados: {len(person['Vehiculos'])}")
        for plate, vehicle in person['Vehiculos'].items():
            print(f"\nPlaca: {plate}")
            print(f"Marca: {vehicle['Marca']}")
            print(f"Modelo: {vehicle['Modelo']}")
            print(f"Año: {vehicle['Año']}")
            print(f"Impuesto pagado: {'Sí' if vehicle['Impuesto'] == 'si' else 'No'}")
def search_owner(owners):
    nit = input("Ingrese el NIT del propietario que desea encontrar: ")
    if nit in owners:
        person = owners[nit]
        print(f"NIT: {nit}")
        print(f"Nombre: {person['Nombre']}")
        print(f"Telefono: {person['Telefono']}")
        print(f"Vehiculos registrados: {len(person['Vehiculos'])}")
        for plate, vehicle in person['Vehiculos'].items():
            print(f"\n  Placa: {plate}")
            print(f"  Marca: {vehicle['Marca']}")
            print(f"  Modelo: {vehicle['Modelo']}")
            print(f"  Año: {vehicle['Año']}")
            print(f"  Impuesto pagado: {'Sí' if vehicle['Impuesto'] == 'si' else 'No'}")
    else:
        print("NIT no encontrado.")
def count_taxes(owners):
    paid = 0
    not_paid = 0
    for data in owners.values():
        for vehicle in data["Vehiculos"].values():
            if vehicle["Impuesto"] == "si":
                paid += 1
            else:
                not_paid += 1
    print(f"-----RESUMEN DE IMPUESTOS-----")
    print(f"Vehículos con impuesto pagado: {paid}")
    print(f"Vehículos con impuesto pendiente: {not_paid}")
registered_owners = record_properly_vehicles()
show_resume(registered_owners)
search_owner(registered_owners)
count_taxes(registered_owners)