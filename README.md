# Docker-compose-flask-DB

1. debemos descargar una versión estable de Docker compose, yo lo hice en Kali Linux con el siguiente comando: sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

2. asignamos permisos: sudo chmod +x /usr/local/bin/docker-compose

3. creamos el archivo de configuración docker-compose.yml, creamos el app.py, el dockerfile y además el requirements

4. ejecutamos la aplicación con en el Docker-compose con el comando docker-compose up --build

para ingresar a la imagen se usa docker exec - it flask_app bash

--para agregar una nueva persona a la tabla lo hacemos con 

curl -X POST http://localhost:5000/add_item \
-H "Content-Type: application/json" \
-d '{"name": "Mario", "email": "mario@gmail.com"}'
