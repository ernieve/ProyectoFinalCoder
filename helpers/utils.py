def normalize_fecha(fecha):
    fecha_split = fecha.split("/")
    return f"{fecha_split[2]}-{fecha_split[0]}-{fecha_split[1]}"