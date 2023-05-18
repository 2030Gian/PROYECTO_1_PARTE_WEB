# Nombre de proyecto: Trántor


# Integrantes:
- Mathias Pariona Mego
- Adriano Raffo Mariaca
- Gian Marco Arteaga Álvarez

# Descripción del Proyecto:
Ofrecemos cursos online en matemáticas, programación y comunicación, dirigido a estudiantes universitarios con planes free y premium. Nos centramos en enseñar habilidades fundamentales para los estudiantes y brindarles mas conocimiento.

# Objetivos principales 
-Proporcionar cursos en línea de alta calidad en las áreas de matemáticas, comunicación y programación.
-Facilitar el acceso a la educación en estas áreas.
-Fomentar el aprendizaje continuo y el desarrollo de habilidades en matemáticas, comunicación y programación.

## Misión

Nuestra misión es proporcionar una plataforma en línea que ofrezca cursos de matemáticas, comunicación y programación de alta calidad. para que todos puedan aprender y desarrollar habilidades clave en un entorno flexible y conveniente.

## Visión

Nuestra visión es ser reconocidos como líderes en la educación en línea de matemáticas, comunicación y programación. Nos esforzamos por ser la opción preferida de estudiantes de todas las edades y niveles, brindando cursos de calidad, recursos interactivos y un entorno de aprendizaje colaborativo.

## Librerias
FLASK: es un marco de desarrollo web escrito en Python que se caracteriza por su ligereza y flexibilidad. Ofrece herramientas y funcionalidades para crear aplicaciones web eficientes y de manera rápida. Lo usamos para la importación de los módulos necesarios: Los módulos de Flask necesarios se importan al comienzo del código. Estos incluyen Flask, render_template, redirect, request y url_for del módulo flask, así como SQLAlchemy y Migrate para manejar la base de datos.

FLASK-SQLALCHEMY: es una extensión de Flask que simplifica la integración y el uso de la biblioteca SQLAlchemy para interactuar con bases de datos en aplicaciones Flask. Lo usamos para la configuración de la base de datos: Se configura la URI de la base de datos PostgreSQL utilizando la línea app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/educaweb1'. Esta línea establece la conexión con la base de datos PostgreSQL utilizando la URI proporcionada.

UUID: es un sistema de identificación único ampliamente utilizado en software. Se representa como una cadena alfanumérica de 128 bits, que garantiza una baja probabilidad de colisión entre identificadores generados. En el código proporcionado, se utiliza el módulo uuid para generar identificadores únicos (UUID) para los campos id de las tablas Usuario y Cursos. 

DATETIME: n módulo en Python que proporciona clases y funciones para manipular y trabajar con fechas y horas de manera eficiente. En la clase Usuario, se utiliza el tipo de columna db.Date() de SQLAlchemy para representar la fecha de nacimiento y en la clase Cursos, se utiliza el tipo de columna db.DateTime de SQLAlchemy para representar la fecha y hora de creación del curso:

HTML: es un estándar utilizado para crear páginas web. Define la estructura y el contenido de una página utilizando etiquetas y elementos que los navegadores interpretan para mostrar el contenido correctamente. En este proyecto se usa html para diseñas las plantillas web y procesar la informacion a la base de datos.

CSS: es utilizado para definir la apariencia y presentación de documentos HTML. Permite controlar aspectos visuales como el diseño, los colores, las fuentes y otros efectos visuales de una página web. Lo empleamos para personalizar el aspecto de la plataforma para que tenga consistencia.

## El nombre del script a ejecutar para iniciar la base de datos con datos:
server.py

## Host:
localhost

## Puerto: 
5432

## Cómo ejecutar el sistema: 
- git clone https://github.com/2030Gian/PROYECTO_1_PARTE_WEB.git
- Correr en el terminal para instalar todas las dependencias: pip install -r requerimientos.txt
- Correr server.py
