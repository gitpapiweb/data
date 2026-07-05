# Usamos una imagen base ligera de Python
FROM python:3.12-slim

# Directorio de trabajo
WORKDIR /app

# Instalamos dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del proyecto
COPY . .

# Comando para ejecutar el cuaderno y convertirlo a HTML
# NB: El comando nbconvert ejecutará el cuaderno y generará un nuevo index.html
CMD jupyter nbconvert --to html --execute Baez_Edgardo_Anselmo_Comisión_2026_TPI_Data_Analytics.ipynb --output index.html
