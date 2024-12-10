# Imagen UD00

- Debian
- Herramientas básicas
- bash
- usuario "user" password "123123"
- sudo

## Construir la imagen

docker build -t ud00-imagen .

## Creamos el contenedor

### Lo dejamos en ejecución

docker run -d --name ud00-contenedor -p 2222:22 ud00-imagen

### Entramos en el contenedor a través de docker

docker exec -it ud00-contenedor /bin/bash

### Entramos a través de ssh

ssh user@localhost -p 2222

### Mapear puerto ssh

- El puerto ssh (22) queda expuesto y pasa a ser el 2222

docker run -it --name ud00container -p 2222:22 -v ./compartida:/mnt/host ud00
