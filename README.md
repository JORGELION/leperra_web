# leperra_web

- Tener instalado python. (Actualmente lla version 3.10.7)
- Estanto en el directorio de la carpeta ejecutar este comando: 

pip install virtualenv

-Luego:

virtualenv venv

-Se creara un entorno virtual aislado en una carpeta llamada venv. Luego:

.\venv\Scripts\activate

-Activaremos el entorno virtual. Luego ejecutar este comando:

pip install -r requirements.txt

-Instalara todas las dependencias. Para correr el servidor ejecutas el siguiente comando:

.\manage.py runserver 

y luego presionar ctrl al link que genere el servidor. Por defecto es: http://127.0.0.1:8000/
