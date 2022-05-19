
#devuelve 1 entidad con sus atributos
def linea_entity(item) -> dict:
    return {
        "nombre": str(item["nombre"]),
        "estaciones": list(item["nombre_estacion"],item["kilometro"],item["grados"]),
        "horarios": list(item["partida"],item["llegada"],item["tren_uso"])
    }

#devuelve una lista de entidades en este caso tren llamando la funcion anterior
def linea_entity(entity) -> list:
    return [linea_entity(item) for item in entity]