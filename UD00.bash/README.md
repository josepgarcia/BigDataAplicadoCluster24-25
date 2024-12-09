# Imagen UD00

- Debian
- Herramientas básicas
- bash
- usuario "user" password "123123"
- sudo

## Construir la imagen

docker build -t ud00 .

## Creamos el contenedor

docker run -it --name ud00-container ud00
