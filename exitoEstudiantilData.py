# we create a random data in order to test the model, this will be changed by the real data
#if you have already de .csv file, you can use it, if not, you can generate it with the ExitoEstudiantilData class
#you can delete this clas in this case
import pandas as pd
import numpy as np

class ExitoEstudiantilData:
    def __init__(self, num_estudiantes=100, archivo='datos_estudiantes.csv'):
        self.num_estudiantes = num_estudiantes
        self.archivo = archivo
        self.data = None
        
    def generar_datos(self):
        np.random.seed(42)
        horas_estudio = np.random.normal(5, 2, self.num_estudiantes)
        asistencia = np.random.choice([0, 1], size=self.num_estudiantes, p=[0.3, 0.7])
        calificaciones_anteriores = np.random.normal(70, 10, self.num_estudiantes)
        edad = np.random.randint(18, 25, size=self.num_estudiantes)
        actividades_extra = np.random.choice([0, 1], size=self.num_estudiantes, p=[0.4, 0.6])
        tiempo_sueno = np.random.normal(7, 1, self.num_estudiantes)
        
        exito = (horas_estudio * 5 + asistencia * 10 + calificaciones_anteriores * 0.5 +
                np.random.normal(0, 5, self.num_estudiantes))
        
        self.data = pd.DataFrame({
            'Horas de Estudio': horas_estudio,
            'Asistencia a Clases': asistencia,
            'Calificaciones Anteriores': calificaciones_anteriores,
            'Edad': edad,
            'Actividades Extracurriculares': actividades_extra,
            'Tiempo de Sueño': tiempo_sueno,
            'Nota Final': exito
        })

        self.data.to_csv(self.archivo, index=False)
        print(f"Datos guardados en {self.archivo}")    
        
    def mostrar_datos(self):
        if self.data is not None:
            print(self.data.head())
        else:
            print("No se han generado los datos aún.")
