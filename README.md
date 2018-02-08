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
    

## Creación de paquete wheel para instalación en producción

    # python setup.py bdist_wheel

Se crea un package wheel en el directorio ``dist`` que puede ser desplegado
con pip:

    # pip install 
A wheel package is created in ``dist`` directory which can be deployed
in a virtualenv (or whatever) with ``pip``:

.. code-block:: bash

    pip install pruebaapp-0.1.0-py3-none-any.whl

Se definen la siguiente variable de entorno siguiente para que flask sepa
donde tiene que cargar la configuración:

    APP_CONFIG_FILE=/path/to/config/file.py
    
Y se ejecuta con gnunicorn:
    
    gunicorn pruebaapp.pruebaapp:app -b 0.0.0.0:8000




