flota = []

n_aeronaves = int(input("Numero de aeronaves: "))    
while n_aeronaves < 3:
    print("Ingresa minimo 3 aeronaves")
    n_aeronaves = int(input("Numero de aeronaves: "))

for _ in range(n_aeronaves):
    matricula = input("Matricula: ")
    modelo = input("Modelo: ")
    horas_vuelo = float(input("Horas de vuelo: "))

    componentes = []
    n_componentes = int(input("Numero de componentes: "))

    for _ in range(n_componentes):
        nombre = input("Componente: ")
        horas_uso = float(input("Horas de uso: "))
        limite = float(input("Limite de horas: "))
        componentes = componentes + [{"nombre": nombre, "horas_uso": horas_uso, "limite": limite}]

    flota = flota + [{"matricula": matricula, "modelo": modelo, "horas_vuelo": horas_vuelo, "componentes": componentes}]

print("\n REPORTE")
for aeronave in flota:
    for componente in aeronave["componentes"]:
        if componente["horas_uso"] >= componente["limite"]:
            print(f"¡ALERTA!: {aeronave['matricula']} - {componente['nombre']}")
