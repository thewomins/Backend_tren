
#devuelve 1 entidad con sus atributos
def tren_entity(item) -> dict:
    return {
        "id": str(item["numero_serie"]),
        "velocidad": item["velocidad"],
        "asientos_por_vagon": item["asientos_por_vagon"],
        "vagones": item["vagones"]
    }

#devuelve una lista de entidades en este caso tren llamando la funcion anterior
def tren_entity(entity) -> list:
    return [tren_entity(item) for item in entity]