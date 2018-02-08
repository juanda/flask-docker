# Proyecto (package) básico python

## Desarrollo en un entorno virtual

Crear un entorno virtual:

    # mkvirtualenv mypackage -p /usr/bin/python3
    
Instalar las dependencias en modo desarrollo:
    
    # pip install -e .
    
Ejecutar la aplicación:

    # python bin/run.py
    
También se puede ejecutar con ``gunicorn``:

    # gunicorn pruebaapp.pruebaapp:app -b 0.0.0.0:8000
    

## Desarrollo con docker

Construir la image a partir del Dockerfile:

    # docker build -t flask-skeleton .


Una vez construida la imagen podemos crear nuevos contenedores con:

    # docker run --name myapp -d -p 8080:8080 flask-skeleton
    
Y se puede acceder a la aplicación en 

    # http://localhost:8080
    
O si usamos vagrant:

    # http://192.168.33.10:8080
    
Si queremos desarrollar es fundamental montar en el contenedor el volumen
del host, para que al hacer cambios en el código el contenedor los vea:

    # docker run -d \
    -p 8080:8080 \
    --name myapp \
    --mount type=bind,source="$(pwd)",target=/app \
    flask-skeleton

Una vez que tenemos creado el contenedor para desarrollo con esta última instrucción,
podemos pararlo:

    # docker stop myqapp (o <container-id>)

Y volverlo a arrancar cuando queramos:

    # docker start myapp (o <container-id>)


## Creación de paquete wheel para instalación en producción

    # python setup.py bdist_wheel

Se crea un package wheel en el directorio ``dist`` que puede ser desplegado
con pip:

    # pip install 
A wheel package is created in ``dist`` directory which can be deployed
in a virtualenv (or whatever) with ``pip``:

    # pip install pruebaapp-0.1.0-py3-none-any.whl

Se definen la siguiente variable de entorno siguiente para que flask sepa
donde tiene que cargar la configuración:

    APP_CONFIG_FILE=/path/to/config/file.py
    
Y se ejecuta con gnunicorn:
    
    gunicorn pruebaapp.pruebaapp:app -b 0.0.0.0:8000




