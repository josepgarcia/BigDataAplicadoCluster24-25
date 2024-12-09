# UD 01

## Descargar hadoop

https://archive.apache.org/dist/hadoop/core/hadoop-3.4.1/hadoop-3.4.1.tar.gz

## Descargar java

https://download.java.net/java/GA/jdk11/13/GPL/openjdk-11.0.1_linux-x64_bin.tar.gz

# Construir la imagen

docker build -t ud02 .

# Creamos un contenedor que utilice la imagen creada

docker run -it --name ud02-container \
 -p 9870:9870 \
 -p 8088:8088 \
 -p 9000:9000 \
 -p 8042:8042 \
 ud02
