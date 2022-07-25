#NOMBRE
  Aerolineas BSV 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#DESCRIPCION 
  Es una web de gestion de aerolineas en la cual se van a ir registrando vuelos, pilotos, aviones, paises y destinos disponibles. Dichos registros lo puede hacer solamente el usuario ADMIN

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#INSTALACIONES
-. En Github copiamos en code copiamos el https:
  
  ![image](https://user-images.githubusercontent.com/97635405/180776369-d1f342f2-5610-442a-a998-01ed2872b0c3.png)

-. Creamos una carpeta y dentro de la misma realizamos lo siguiente:

  ![image](https://user-images.githubusercontent.com/97635405/180777778-a16cdc87-73b8-4837-846c-91fa5f9a978f.png)
  
-. Clonamos el repositorio de la siguiente manera:

  ![image](https://user-images.githubusercontent.com/97635405/180778328-bf0ae77b-093a-45ed-848e-5ee2807bd2a4.png)

-. Abrimos la carpeta creada con Visual Studio Code

-. Instalar django con el siguiente comando:
   python pip install django
   python -m pip install django

-. Aplicar modelos de BD y migraciones:
   comando --> python manage.py makemigrations
   comando --> python manage.py migrate
   
-. Crear usuario administrador, el mismo solicita nombre usuario, correo electronico (opcional) y contraseña.
   comando --> python manage.py createsuperuser

-. Iniciamos servidor: 
   comando --> python manage.py runserver
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#USO QUE HACE NUESRTA PAGINA:

http://127.0.0.1:8000/- Ruta que deriva en el inicio de la web - Nav Bar interactiva, botones de inicio, Paises/Destino,
Vuelos, Aviones, Sobre Nosotros, Registro, Iniciar Sesión. Si se es usuario admin, se activa boton para editar, agregar 
y eliminar dichas instrucciones. 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
http://127.0.0.1:8000/paises/ - Muestra los paises creados

http://127.0.0.1:8000/paises/create/ - Formulario para crear paises (solo el usuario admin puede hacerlo)

http://127.0.0.1:8000/paises/edit/pais_id - Editar informacion de un pais (solo el usuario admin puede hacerlo)

http://127.0.0.1:8000/paises/delete/pais_id - Eliminar un pais (solo el usuario admin puede hacerlo)

http://127.0.0.1:8000/paises/delete/pais_id - Editar informacion de un pais (solo el usuario admin puede hacerlo)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
http://127.0.0.1:8000/paises/pais_id/ - Muesrta destino/pais

http://127.0.0.1:8000/destinos/pais_id/create - Crear destino en base al pais creado (solo el usuario admin puede hacerlo)

http://127.0.0.1:8000/destinos/edit/destino_id - Editar informacion de un destino  (solo el usuario admin puede hacerlo)

http://127.0.0.1:8000/destinos/delete/destino_id - Eliminar destino  (solo el usuario admin puede hacerlo)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
http://127.0.0.1:8000/vuelos/ - Muestra todos los vuelos disponibles

http://127.0.0.1:8000/vuelos/create/ - Muestra los destinos creados (solo el usuario admin puede hacerlo) 

http://127.0.0.1:8000/vuelos/create/vuelo_id - Crear nuevo vuelo de destino (solo el usuario admin puede hacerlo)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
http://127.0.0.1:8000/aviones/ - Muestra todos los aviones cargados

http://127.0.0.1:8000/mostrar_avion/avion_id - Muestra los datos cargados de cada avion

http://127.0.0.1:8000/crear_aviones/ - Crear nuevo avion (solo el usuario admin puede hacerlo)

http://127.0.0.1:8000/editar_aviones/avion_id - Editar datos de un avion (solo el usuario admin puede hacerlo)

http://127.0.0.1:8000/eliminar_aviones/avion_id - Eliminar avion cargado (solo el usuario admin puede hacerlo)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
http://127.0.0.1:8000/registro/ - Nos dirige al formulario para registrar usuario

http://127.0.0.1:8000/inicio_sesion/ - Nos lleva al formulario para iniciar sesion

http://127.0.0.1:8000/cerrar_sesion/ - Cierra la sesion del usuario

http://127.0.0.1:8000/modificar_user/user_id - Permite modificar los datos del usuario

http://127.0.0.1:8000/mostrar_user/user_id - Muestra los datos cargados del usuario

http://127.0.0.1:8000/ - Pagina de inicio donde se muestran los comentarios realizado por los usuarios y los ultimos tres aviones cargados.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
http://127.0.0.1:8000/about/ - Sobre los autores del proyecto

http://127.0.0.1:8000/crear_articulo/ - Nos dirige al formulario para dejar un comentario de la pagina (titulo y descripcion)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#TAREAS REALIZADAS 

Facundo Sanchez. => Modelos de Pais, Destino, Vuelo con todo lo que despliega 
Facundo Battaglino. => Modelo de Avion, Readme, Test, Vista de "Sobre Nosotros"
Ernesto Vega. => Login, registro usuario, modificacion de perfil, eliminar, crear articulo, restricciones, modelo de VueloPasajero







