flota = []

n_aeronaves = int(input("Numero de aeronaves: "))

aeronave_actual = 0
while aeronave_actual < n_aeronaves:
    matricula = input("Matricula: ")
    modelo = input("Modelo: ")
    horas_vuelo = float(input("Horas de vuelo: "))

    componentes = []
    n_componentes = int(input("Numero de componentes: "))

    componente_actual = 0
    while componente_actual < n_componentes:
        nombre = input("Componente: ")
        horas_uso = float(input("Horas de uso: "))
        limite = float(input("Limite de horas: "))
        componentes = componentes + [{"nombre": nombre, "horas_uso": horas_uso, "limite": limite}]
        componente_actual += 1

    flota = flota + [{"matricula": matricula, "modelo": modelo, "horas_vuelo": horas_vuelo, "componentes": componentes}]
    aeronave_actual += 1

print("\n REPORTE")
aeronave_actual = 0
while aeronave_actual < n_aeronaves:
    componente_actual = 0
    while componente_actual < n_componentes:
        comp = flota[aeronave_actual]["componentes"][componente_actual]
        if comp["horas_uso"] >= comp["limite"]:
            print(f"ALERTA: {flota[aeronave_actual]['matricula']} - {comp['nombre']}")
        componente_actual += 1
    aeronave_actual += 1