# construir la build
docker build -t proyecto_bd1 .

# ejecutar la build
docker run -d -p 80:8000 proyecto_bd1
