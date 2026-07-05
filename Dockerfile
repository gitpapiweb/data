# Usamos una imagen base ligera de Python
FROM python:3.12-slim

# Instalamos dependencias del sistema necesarias para Quarto
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gdebi-core \
    && curl -LO https://quarto.org/download/latest/quarto-linux-amd64.deb \
    && gdebi -n quarto-linux-amd64.deb \
    && rm quarto-linux-amd64.deb \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Directorio de trabajo
WORKDIR /app

# Instalamos dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del proyecto
COPY . .

# Comando para renderizar el cuaderno con Quarto
CMD ["quarto", "render", "Baez_Edgardo_Anselmo_Comisión_2026_TPI_Data_Analytics.ipynb", "--to", "html"]
