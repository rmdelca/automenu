import json
from random import randint

class Menu:

    def __init__(self) -> None:
        with open(r"platillos.json", "r") as platillos_json :
            self.platillos = json.load(platillos_json)

    def load_menu(self, fp):
        with open(fp) as platillos_json :
            self.platillos = json.load(platillos_json)

    def random_menu_3_comidas(self, showmenu=True):
        """Genera un menu aleatorio que tiene 3 platillos por tiempo"""
        # Abrimos y cargamos la planitlla
        with open(r"empty_menu.json", "r") as plantilla_json:
            plantilla = json.load(plantilla_json)
        
        # Abrimos los platillos 
        platillos = self.platillos
        
        # Definicion de los tres tiempos
        tiempos = ["desayuno", "comida", "cena"]
        
        # Escogemos las tres nuevas comidas
        nuevas_comidas = dict()
        for i in tiempos:
            nuevas_comidas[i] = list()
        # Van a ser tres platillos por tiempo 
        for tiempo in tiempos:
            while len(nuevas_comidas[tiempo]) < 3:
                random_platillo = randint(0,len(platillos[tiempo])-1)
                platillo_al_azar = platillos[tiempo][random_platillo]
                if platillo_al_azar not in nuevas_comidas:
                    nuevas_comidas[tiempo].append(platillo_al_azar)
            # # Nomas para ver como quedo el nuevo menu
            # self.dict_style_print(nuevas_comidas)
            # Llenar la plantilla con los nuevo platillos
            for dia in plantilla.keys():
                if dia in ["lunes", "martes", "miercoles"]:
                    plantilla[dia][tiempo] = nuevas_comidas[tiempo][0] 
                if dia in ["jueves", "viernes"]:
                    plantilla[dia][tiempo] = nuevas_comidas[tiempo][1]
                if dia in ["sabado", "domingo"]:
                    plantilla[dia][tiempo] = nuevas_comidas[tiempo][2]                 
        
        if showmenu:
            self.menu_print(plantilla)
        
        # Guardaa el nuevop menu en un archivo 
        with open(r"menu_random.json", "w") as nuevo_menu_json:
            json.dump(plantilla, nuevo_menu_json, indent=2)

    def menu_print(self, menu):
        print("\nMenu:\n{")
        for i in menu.keys():
            print(f"  \"{i}\" :")
            for j in menu[i]:
                print(f"    {j} : \"{menu[i][j]}\"")
        print("}")
                
def main():
    menu_rando = Menu()
    menu_rando.random_menu_3_comidas()

if __name__ == "__main__": 
    main()