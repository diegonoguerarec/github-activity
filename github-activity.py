import argparse, requests, json

def main():
    
    # Configurar parser
    parser = argparse.ArgumentParser(description="Muestra actividades de un usuario de github")
    parser.add_argument("nombre", type=str, help="Nombre de usuario de github")
    
    args = parser.parse_args()

    # Nombre de usuario de github
    nombre = args.nombre

    # Peticion
    r = requests.get(f"https://api.github.com/users/{nombre}/events")

    if r.status_code == 200:
        actividad = r.json()
        print(actividad)

        with open("actividad.json", mode="w") as f:
            json.dump(actividad, f, indent=4)
    
    else:
        print("Error al obtener datos...")


if __name__ == "__main__":
    main()