# Para llevar un proyecto con Git y GitHub, sigue estos pasos:

1. **Configuración del proyecto**: Inicializa Git en la carpeta del proyecto que deseas llevar. Configura tu nombre de usuario y correo electrónico de GitHub:

   ```
   git config --global user.name "TU NOMBRE"
   git config --global user.email "TU CORREO DE GITHUB"
   ```
   [Source 8]**(https://soloelectronicos.com/2021/10/17/como-subir-un-proyecto-local-a-github/)**

2. **Añade todos los archivos al área de preparación**:

   ```
   git add .
   ```
   [Source 8](https://soloelectronicos.com/2021/10/17/como-subir-un-proyecto-local-a-github/)

3. **Realiza el primer commit**:

   ```
   git commit -m "Primer commit"
   ```
   [Source 8](https://soloelectronicos.com/2021/10/17/como-subir-un-proyecto-local-a-github/)

4. **Crea un repositorio en GitHub**: Ve a [GitHub](https://github.com) y crea un nuevo repositorio. Dale un nombre, descripción y selecciona si será público o privado. No marca la casilla "Crear README" si no lo deseas.

5. **Agrega el repositorio remoto a tu repositorio local**:

   ```
   git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
   ```
   [Source 9](https://www.freecodecamp.org/espanol/news/comandos-basicos-de-git-como-usar-git-en-un-proyecto-real/)

6. **Realiza el push al repositorio**:

   ```
   git push -u origin main
   ```
   [Source 9](https://www.freecodecamp.org/espanol/news/comandos-basicos-de-git-como-usar-git-en-un-proyecto-real/)

Después de estos pasos, tu proyecto se habrá subido a GitHub. Para realizar cambios en el proyecto, sigue estos pasos:

1. **Añade los cambios**:

   ```
   git add .
   ```
   [Source 9](https://www.freecodecamp.org/espanol/news/comandos-basicos-de-git-como-usar-git-en-un-proyecto-real/)

2. **Realiza un commit**:

   ```
   git commit -m "Nuevo commit"
   ```
   [Source 9](https://www.freecodecamp.org/espanol/news/comandos-basicos-de-git-como-usar-git-en-un-proyecto-real/)

3. **Sube los cambios al repositorio**:

   ```
   git push
   ```
   [Source 9](https://www.freecodecamp.org/espanol/news/comandos-basicos-de-git-como-usar-git-en-un-proyecto-real/)

Para eliminar o añadir archivos en el repositorio, puedes utilizar los comandos `git rm` y `git add`, respectivamente. Para eliminar un archivo, ejecuta:

   ```
   git rm archivo.txt
   ```
   Luego, ejecuta `git add .` para agregar el cambio al área de preparación. Finalmente, realiza un commit y un push para actualizar el repositorio en GitHub.

   [Source 9](https://www.freecodecamp.org/espanol/news/comandos-basicos-de-git-como-usar-git-en-un-proyecto-real/) 