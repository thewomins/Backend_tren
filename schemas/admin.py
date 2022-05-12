
#devuelve 1 entidad con sus atributos
def admin_entity(item) -> dict:
    return {
        "email": str(item["email"]),
        "password": str(item["password"])
    }

#devuelve una lista de entidades en este caso admin llamando la funcion anterior
def admin_entity(entity) -> list:
    return [admin_entity(item) for item in entity]