# script simple pour lancer l'app orbit d'un coup
import uvicorn
import webbrowser
import threading
import time

def ouvrir_navigateur():
    # attend 1.5 seconde que le serveur demarre et ouvre la page web
    time.sleep(1.5)
    webbrowser.open("http://localhost:8033")

if __name__ == "__main__":
    print("------------------------------------------------------------------")
    print(" 🌐  Lancement de ORBIT Geospatial Exposure UI on port 8033")
    print(" Ouverture du navigateur sur http://localhost:8033")
    print("------------------------------------------------------------------")
    
    # ouvrir la page automatiquement
    threading.Thread(target=ouvrir_navigateur, daemon=True).start()
    
    # demarrage du serveur web fastapi
    uvicorn.run("orbit_geospatial_exposure.api:app", host="127.0.0.1", port=8033, reload=True)
