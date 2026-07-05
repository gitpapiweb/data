# Usamos una imagen base ligera de Python
FROM python:3.12-slim

# Directorio de trabajo
WORKDIR /app

# Instalamos dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- PASO CRÍTICO: Registramos el kernel de Jupyter ---
RUN python -m ipykernel install --user --name python3 --display-name "Python 3"

# Copiamos el resto del proyecto
COPY . .

# Comando para ejecutar el cuaderno y convertirlo a HTML
CMD ["jupyter", "nbconvert", "--to", "html", "--execute", "Baez_Edgardo_Anselmo_Comisión_2026_TPI_Data_Analytics.ipynb", "--output", "report.html"]
