#Reconocedor facial para encontrar a personas desaparecidas 
<p>
Para este proyecto vamos a usar la version de python 3.11.4 y vamos a instalar opencv y imutils para esto ejecutamos los siguientes comandos:
OpenCv
**pip install opencv-python**
imutils
**pip install imutils**
</p>

### Estructura del proyecto

<p>
El poyecto esta estructurado de la siguiente forma:

**Capturador_Rostros.py** .- Encargado de capturar las imagenes. 
**Entrenador.py** .- Entrena el modelo LBPH para usarlo en el reconocimiento
**main.py** .- Es la clase principal el cual ejecuta por medio de una interfaz todo el proyecto
**Reconocedor_Facial.py** .- Esta clase se encarga de ejecutar el modelo y empieza a hacer reconocimiento.

La forma de ejecturarlo por una interfaz en ejecutar el main.py
La otra forma es:
Primero: **Capturador_Rostros.py**
Segundo: **Entrenador.py**
Tercero: **Reconocedor_Facial.py**
</p>

![1](https://github.com/RichardAgr/Vision-artificial/assets/136004365/f487204a-68a5-41b9-b15f-4c4ca574ff47)

##Posibles errores
<p>
Si aparece este error es por que la camara del dispositivo no esta siendo reconocido:

0: Este argumento indica el índice de la cámara que deseas usar. En la mayoría de las computadoras, el índice 0 se refiere a la cámara web predeterminada. Si tienes varias cámaras conectadas a tu computadora, puedes cambiar este número a 1, 2, etc., para seleccionar una cámara diferente.

este error puede aparecer al momento de ejecutar las clases: **Capturador_Rostros.py, Reconocedor_Facial.py**

![2](https://github.com/RichardAgr/Vision-artificial/assets/136004365/c4f5879c-e16b-495b-89cc-b580706bd041)

Esto a que cambiar en el codigo:
**Capturador_Rostros.py**

![3](https://github.com/RichardAgr/Vision-artificial/assets/136004365/895c70c2-e206-48be-939f-8adb3a38806c)

** Reconocedor_Facial.py**

![4](https://github.com/RichardAgr/Vision-artificial/assets/136004365/56432ceb-e9f7-4805-8999-ff2b05b8dfec)

Otro posible error que pueda suceder es cuando no se tiene actualizado el openCv, este proyecto esta trabajando con una version de opencv 4.9.0.

para saber que version de opencv se tiene, se puede ejecutar el siguiente codigo en python:
</p>

```
import cv2
print(cv2.__version__)
```

<p>
Para actualizar el openCv se ejecuta el siguiente comando en cmd:
**pip install opencv-python --upgrade** 
</p>

#La interfaz

![5](https://github.com/RichardAgr/Vision-artificial/assets/136004365/3909d1c6-8794-4820-9f7c-26b598e471c7)

Para ejecutar: 
primero: **Registrar persona desaparecida**
segundo: **Entrenar Modelo**
tercero: **Buscar persona(Finaliza ESC)**

Para poder cerrar la interfaz solo presionamos el boton **ESC**
