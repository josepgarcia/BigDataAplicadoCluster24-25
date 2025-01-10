# UD 01

## Descargar hive

Ponerlo dentro de la carpeta software

https://archive.apache.org/dist/hive/hive-2.3.9/apache-hive-2.3.9-bin.tar.gz

# Construir la imagen

docker build -t ud04-imagen .

# Creamos un contenedor que utilice la imagen creada

docker run -it --name ud04-container \
 -p 9870:9870 \
 -p 8088:8088 \
 -p 9000:9000 \
 -p 8042:8042 \
 ud04

# Creamos un contenedor que se borra al cerrar

docker run -it --rm --name ud04-container \
 -p 9870:9870 \
 -p 8088:8088 \
 -p 9000:9000 \
 -p 8042:8042 \
 ud04
