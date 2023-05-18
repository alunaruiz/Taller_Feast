# Imagen base
FROM python:3.9-slim
# Directorio de trabajo
WORKDIR /notebook

# Actualizar el sistema operativo y las bibliotecas
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        git \
        build-essential \
        libssl-dev \
        libffi-dev \
        python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Variables de entorno para Feast
ENV FEAST_VERSION=0.12.1
ENV FEAST_SERVING_URL=0.0.0.0:6566
ENV FEAST_CORE_URL=0.0.0.0:6565
ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

# Instalar Feast
RUN pip install --no-cache-dir feast==$FEAST_VERSION

# Instalar Jupyter Notebook
RUN pip install jupyter

# Copiar los archivos de configuración de Feast
#COPY . .
COPY feast/ /app/feast/

# Exponer los puertos necesarios
EXPOSE 6565 6566
EXPOSE 8888 8888

# Comando para iniciar un shell interactivo
CMD jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root && feast start --serving_url $FEAST_SERVING_URL --core_url $FEAST_CORE_URL


