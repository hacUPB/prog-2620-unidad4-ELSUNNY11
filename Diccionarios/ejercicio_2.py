# Base de datos de flota
flota = {
    "N123AA": {
        "modelo": "Boeing 787-9",
        "año": 2018,
        "horas_vuelo": 12500,
        "ciclos": 1350,
        "estado": "En servicio",
        "base": "DFW",
        "proxima_revision": "2023-07-15"
    },
    "N456AA": {
        "modelo": "Boeing 777-300ER",
        "año": 2014,
        "horas_vuelo": 26800,
        "ciclos": 2940,
        "estado": "En mantenimiento",
        "base": "MIA",
        "proxima_revision": "2023-03-30"
    }
}

# Añadir nueva aeronave
flota["N789AA"] = {
    "modelo": "Airbus A321neo",
    "año": 2022,
    "horas_vuelo": 1200,
    "ciclos": 420,
    "estado": "En servicio",
    "base": "LAX",
    "proxima_revision": "2024-01-10"
}

# Que el usuario agregue una nueva aeronave
placa = input("Ingrese la placa de la aeronave: ")
mod = input("Ingrese el modelo de la aeronave: ")
añ = input("Ingrese el año de la aeronave: ")
ho = input("Ingrese las horas de vuelo de la aeronave: ")
cic = input("Ingrese los ciclos de la aeronave: ")
est = input("Ingrese el estado de la aeronave: ")
bas = input("Ingrese la base de la aeronave: ")
prox = input("Ingrese cuando es al próxima revisión de la aeronave: ")

temp = {}
temp["modelo"] = mod
temp["año"] = añ
temp["horas_vuelo"] = ho
temp["ciclos"] = cic
temp["estado"] = est
temp["base"] = bas
temp["proxima_revision"] = prox

flota[placa] = temp

# Mostrar información detallada
for matricula, datos in flota.items():
    print(f"Aeronave: {matricula}")
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")