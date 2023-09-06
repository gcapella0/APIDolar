# Usar una imagen base de Python
FROM python:3.9

# Copiar el código de web scraping al contenedor
COPY . /app

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar las dependencias
RUN pip install requests beautifulsoup4

# Ejecutar el script de web scraping
CMD ["python", "test_scraping.py"]
