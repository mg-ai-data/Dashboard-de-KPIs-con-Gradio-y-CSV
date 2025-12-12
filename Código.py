!pip install gradio pandas matplotlib --quiet

import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt

def mostrar_dashboard(file):
    try:
        # Leer el CSV (usa .name para compatibilidad con Gradio)
        df = pd.read_csv(file.name)
        
        # Estandarizar nombres de columnas
        df.columns = df.columns.str.lower().str.strip()
        
        # Buscar una columna de fecha
        posibles_fechas = ['fecha', 'date', 'día', 'dia']
        col_fecha = next((c for c in df.columns if c in posibles_fechas), None)
        
        if col_fecha:
            df[col_fecha] = pd.to_datetime(df[col_fecha])
        else:
            return "❌ No se encontró columna de fecha ('fecha' o 'date')."
        
        # Buscar una métrica principal (ventas, tráfico, performance)
        posibles_metricas = ['ventas', 'tráfico', 'trafico', 'performance']
        col_metricas = [c for c in df.columns if c in posibles_metricas]
        
        if not col_metricas:
            return f"❌ No se encontraron columnas de métricas ({posibles_metricas}).\nColumnas detectadas: {list(df.columns)}"
        
        # Crear gráfico
        plt.figure(figsize=(6,4))
        for m in col_metricas:
            plt.plot(df[col_fecha], df[m], marker='o', label=m.capitalize())
        
        plt.title("📊 Dashboard de KPIs")
        plt.xlabel("Fecha")
        plt.ylabel("Valor")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        return plt.gcf()
    
    except Exception as e:
        return f"❌ Error leyendo CSV: {e}"

demo = gr.Interface(
    fn=mostrar_dashboard,
    inputs=gr.File(label="Subí tu CSV (con columnas: fecha, ventas, tráfico, performance...)"),
    outputs=gr.Plot(label="Dashboard de KPIs"),
)

demo.launch(share=True)
