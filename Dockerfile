# Utiliza una imagen base de PostgreSQL
FROM postgres

# Variables de entorno para configurar la base de datos
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_DB=${POSTGRES_DB}
RUN echo ${POSTGRES_DB}
# Copia los archivos SQL de inicialización al contenedor
COPY init.sql /docker-entrypoint-initdb.d/

# Expone el puerto 5432 (puerto predeterminado de PostgreSQL)
EXPOSE 5432
#docker run --name postgres-container -e POSTGRES_USER=usuario -e POSTGRES_PASSWORD=contra123 -e POSTGRES_DB=api_db -p 5432:5432 -d mi-apidb