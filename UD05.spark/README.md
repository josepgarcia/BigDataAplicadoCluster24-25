# UD 05

## Descargar spark (without hadoop)

https://archive.apache.org/dist/spark/spark-3.3.0/spark-3.3.0-bin-without-hadoop.tgz
Debes guardarlo en la raíz de esta carpeta

# Construir la imagen

docker build -t ud05-imagen .

# Creamos un contenedor que utilice la imagen creada

## Abrir puerto 4040 para spark

docker run -it --name ud05-container \
 -p 9870:9870 \
 -p 8088:8088 \
 -p 9000:9000 \
 -p 8042:8042 \
 -p 4040:4040 \
 ud05-imagen

# Creamos un contenedor que se borra al cerrar

docker run -it --rm --name ud05-container \
 -p 9870:9870 \
 -p 8088:8088 \
 -p 9000:9000 \
 -p 8042:8042 \
 -p 4040:4040 \
 ud05-imagen
