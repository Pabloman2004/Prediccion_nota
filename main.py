import os
import pandas as pd
from data_loader import DataLoader
from exitoEstudiantilData import ExitoEstudiantilData
from model import LinearRegressionModel
from visualizer import Visualizer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import tkinter as tk
from tkinter import simpledialog

def main():
    archivo_csv = "datos_estudiantes.csv"
    
    # Verificar si el archivo CSV existe
    if not os.path.exists(archivo_csv):
        print(f"El archivo {archivo_csv} no existe. Generando datos...")
        exito_data = ExitoEstudiantilData(num_estudiantes=100, archivo=archivo_csv)
        exito_data.generar_datos()
    
    # Cargar los datos
    loader = DataLoader(archivo_csv)
    data = loader.cargar_datos()
    
    if data is not None:
        # Verificar las columnas del DataFrame
        print("Columnas del DataFrame:", data.columns)
        
        # Usar todas las columnas excepto 'Nota Final' como variables independientes
        X_columns = data.columns.drop('Nota Final')
        y_column = 'Nota Final'
        
        if all(col in data.columns for col in X_columns) and y_column in data.columns:
            # Crear y entrenar el modelo
            model = LinearRegressionModel()
            model.train(data[X_columns], data[y_column])
            
            # Solicitar valores al usuario y hacer una predicción
            visualizer = Visualizer()
            valores_usuario = visualizer.solicitar_valores_gui(X_columns)
            prediccion_usuario = model.predict(valores_usuario)
            print(f"La predicción de la Nota Final para los valores ingresados es: {prediccion_usuario[0]}")
            
            # Visualizar los resultados y agregar la predicción al PDF
            visualizer.plot_graph(data, model.predict(data[X_columns]), prediccion_usuario, valores_usuario)
        else:
            print(f"Las columnas '{X_columns}' y/o '{y_column}' no se encuentran en los datos.")
    else:
        print("No se pudieron cargar los datos.")

if __name__ == "__main__":
    main()

