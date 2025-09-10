# Usamos Python slim para reducir tamaño
FROM python:3.10-slim

# Directorio de trabajo
WORKDIR /app

# Copiamos requirements y instalamos
COPY requirements.txt .

# Instalamos pip actualizado y dependencias de Python
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del proyecto
COPY . .

# Puerto que Render asigna
ENV PORT 5000

# Comando para levantar la app
CMD ["python", "app.py"]