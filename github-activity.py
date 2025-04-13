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

    print()
    if r.status_code == 200:
        actividades = r.json()
        
        for actividad in actividades: ## Ciclo para pasar por todos los eventos
            if actividad["type"] == "PushEvent": ## Si es un evento de push
                cantidad_commits = len(actividad["payload"]["commits"])
                nombre_repo = actividad["repo"]["url"]

                # Detalles de los commits
                print("-"*90)
                print(f"Push de {cantidad_commits} commits a -> {nombre_repo}")
                print(f"\t {"Autor"[:10]:<11} {"Mensaje"[:50]:<51}")
                print("\t"+"-"*82)
                for commit in actividad["payload"]["commits"]:
                    print(f"\t {commit["author"]["name"][:10]:<11} {commit["message"][:50]:<51}")

            print()

        with open("actividad.json", mode="w") as f:
            json.dump(actividades, f, indent=4)
    
    else:
        print("Error al obtener datos...")


if __name__ == "__main__":
    main()