
#devuelve 1 entidad con sus atributos
def estaciones_entity(item) -> dict:
    return {
        "nombre": str(item["nombre"]),
        "ciudad": str(item["ciudad"])
    }

#devuelve una lista de entidades en este caso estaciones llamando la funcion anterior
def estaciones_entity(entity) -> list:
    return [estaciones_entity(item) for item in entity]