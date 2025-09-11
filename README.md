# Simple Hero API

Desarrollo de una REST API básica que crea, consulta, actualiza y elimina heroes de película.

<hr>

## Para ejecutar:

1. Crea tu entorno virtual

  Comando: <p>python -m venv venv</p>
   
2. Activa el entorno virtual

  Comando: <p>.\venv\Scripts\activate</p>

3. Crea tu archivo .env y configura tus credenciales de BD.

4. Ejecutar el proyecto con el comando: fastapi dev main.py

<hr>

## Endpoints

### 1. Consultar un listado de heroes (GET)
   http://localhost:8000/heroes/
   <img width="922" height="562" alt="image" src="https://github.com/user-attachments/assets/f07c3399-55bb-4e79-95e9-15ed7225ef60" />

### 2. Consultar un heroe de manera individual (GET)
http://localhost:8000/heroes/{id}
   <img width="914" height="389" alt="image" src="https://github.com/user-attachments/assets/60e90b98-f556-45e4-9b45-68c951aa12cc" />

### 3. Crear un nuevo heroe (POST)
http://localhost:8000/heroes/
   <img width="911" height="516" alt="image" src="https://github.com/user-attachments/assets/0a71e14e-65f2-4c4e-966b-c6aac2484030" />

### 4. Actualizar características de un heroe 
http://localhost:8000/heroes/{id}
<img width="927" height="404" alt="image" src="https://github.com/user-attachments/assets/50b0745c-20f9-4f8f-8ecf-2178d055f74b" />



Consultamos...

<img width="308" height="125" alt="image" src="https://github.com/user-attachments/assets/69a6f846-883f-42a1-b645-7dc884397813" />

### 5. Eliminar un heroe
http://localhost:8000/heroes/{id}
<img width="925" height="394" alt="image" src="https://github.com/user-attachments/assets/e562ca51-5cf2-49ab-99ef-53fa41537a46" />

<hr>

### Dependencias usadas
* FastAPI
* Typing
* SQLModel

  <hr>

### Comando de instalación FastAPI y SQL Model
* <p>pip install "fastapi[standard]" sqlmodel</p>

