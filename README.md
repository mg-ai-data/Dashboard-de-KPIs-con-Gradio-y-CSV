# 📊 Dashboard de KPIs con Gradio

Este proyecto permite subir un archivo CSV y visualizar un dashboard de KPIs de manera automática.  
Detecta columnas de fecha y métricas comunes (**ventas**, **tráfico**, **performance**) y genera un gráfico interactivo.

## 🚀 Funcionalidades
- Subida de CSV vía interfaz.
- Detección automática de columnas:
  - Fecha (`fecha`, `date`)
  - Métricas (`ventas`, `tráfico`, `performance`)
- Gráfico automatizado con Matplotlib.
- Interfaz simple y portable con Gradio.

## ▶️ Instalación
```bash
pip install -r requirements.txt
