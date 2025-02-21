import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import tkinter as tk
from tkinter import simpledialog
import pandas as pd

class Visualizer:
    def plot_graph(self, data, predictions, prediccion_usuario, output_pdf='resultados.pdf'):
        with PdfPages(output_pdf) as pdf:
            # Graficar los datos reales y las predicciones para cada variable independiente
            for column in data.columns:
                if column != 'Nota Final':
                    plt.figure(figsize=(10, 6))
                    plt.scatter(data[column], data['Nota Final'], color='blue', label='Datos Reales')
                    plt.plot(data[column], predictions, color='red', label='Predicciones')
                    plt.xlabel(column)
                    plt.ylabel('Nota Final')
                    plt.title(f'Regresión Lineal: {column} vs Nota Final')
                    plt.legend()
                    pdf.savefig()  # Guarda la figura actual en el PDF
                    plt.close()
            
            # Graficar todas las variables juntas
            plt.figure(figsize=(10, 6))
            for column in data.columns:
                if column != 'Nota Final':
                    plt.scatter(data[column], data['Nota Final'], label=f'Datos Reales - {column}')
            plt.plot(data.index, predictions, color='red', label='Predicciones')
            plt.xlabel('Índice')
            plt.ylabel('Nota Final')
            plt.title('Regresión Lineal: Variables Independientes vs Nota Final')
            plt.legend()
            pdf.savefig()  # Guarda la figura actual en el PDF
            plt.close()
            
            # Agregar una conclusión predefinida al PDF
            plt.figure(figsize=(10, 6))
            plt.axis('off')  # Ocultar los ejes
            conclusion = (
                "Conclusión:\n\n"
                "El modelo de regresión lineal muestra que las horas de estudio tienen un impacto significativo "
                "en la nota final de los estudiantes. A medida que aumentan las horas de estudio, la nota final "
                "tiende a mejorar. Otros factores como la asistencia a clases y las calificaciones anteriores "
                "también contribuyen al éxito académico, las calificaciones anteriores son bastante relevantes. "
                "Este modelo puede ser útil para identificar áreas de mejora y ayudar a los estudiantes a"
                "  planificar su tiempo de estudio de manera más efectiva.\n\n"
                f"Predicción de la Nota Final para los valores ingresados: {prediccion_usuario[0]}"
            )
            plt.text(0.5, 0.5, conclusion, ha='center', va='center', wrap=True, fontsize=12)
            pdf.savefig()  # Guarda la figura actual en el PDF
            plt.close()

    def solicitar_valores_gui(self, columnas):
        root = tk.Tk()
        root.title("Formulario de Entrada de Datos")
        
        entries = {}
        for columna in columnas:
            frame = tk.Frame(root)
            frame.pack(fill='x')
            label = tk.Label(frame, text=columna, width=20)
            label.pack(side='left')
            entry = tk.Entry(frame)
            entry.pack(side='left', fill='x', expand=True)
            entries[columna] = entry
        
        def on_submit():
            valores = {columna: [float(entry.get())] for columna, entry in entries.items()}
            self.valores_usuario = pd.DataFrame(valores)
            root.destroy()
        
        submit_button = tk.Button(root, text="Enviar", command=on_submit)
        submit_button.pack(fill='x')
        
        root.mainloop()
        return self.valores_usuario
