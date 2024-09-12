# Usa una imagen base oficial de Python
FROM python:3.12-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo requirements.txt en el directorio de trabajo
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido del proyecto en el directorio de trabajo
COPY . .

# Expone el puerto en el que la aplicación correrá
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "todolist.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]