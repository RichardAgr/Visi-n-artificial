import cv2
import os
import numpy as np

dataPath ='C:\\Users\\asus\\OneDrive\\Escritorio\\Vision-artificial\\Data' 
#Listado de carpetas
peopleList = os.listdir(dataPath)
print('Lista de personas: ', peopleList)

labels = []
facesData = []
label = 0

for nameDir in peopleList:
	personPath = dataPath + '/' + nameDir
	print('Leyendo las imágenes')

	for fileName in os.listdir(personPath):
		print('Rostros: ', nameDir + '/' + fileName)
		labels.append(label)
		
		#Leer la imagen y convertirla a escala de grises
		facesData.append(cv2.imread(personPath+'/'+fileName,0))
		image = cv2.imread(personPath+'/'+fileName,0)
		cv2.imshow('image',image)
		cv2.waitKey(10)
		
	label = label + 1

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Entrenando el reconocedor de rostros
print("Entrenando...")
face_recognizer.train(facesData, np.array(labels))

# Almacenando el modelo obtenido

face_recognizer.write('modeloLBPHFace.xml')
print("Modelo almacenado correcatamente...")