import pandas as pd

class DataLoader:
    def __init__(self, archivo='exito_estudiantil.csv'): #change the path to the path of your
        self.archivo = archivo
    
    def cargar_datos(self):
        """Cargar los datos desde un archivo CSV"""
        try:
            data = pd.read_csv(self.archivo)
            print(f"Datos cargados desde {self.archivo}")
            return data
        except FileNotFoundError:
            print(f"El archivo {self.archivo} no se encuentra.")
            return None
    
    def guardar_datos(self, datos):
        """Guardar los datos en un archivo CSV"""
        datos.to_csv(self.archivo, index=False)
        print(f"Datos guardados en {self.archivo}")
