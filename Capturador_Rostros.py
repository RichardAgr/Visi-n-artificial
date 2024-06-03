import cv2
import os
import imutils


name = input('Inserte el nombre de la persona: ')

#El nombre del video debe ser acompañado del la extenxion .mp4
# Ejemplo.mp4
#video= input('Inserte el nombre o la direccion del video: ')

personaName= name + ' !DESAPARECIDO!'  

#Almacenar las fotos
#La direcion cambia segun el lugar de almacenamiento
dataPath='C:\\Users\\asus\\OneDrive\\Escritorio\\Visi-n-artificial\\Data' 
personPath = dataPath +'\\'+ personaName
if not os.path.exists(personPath):
    print('Carpeta creada: ',personPath)
    os.makedirs(personPath)

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('Riki.mp4')
faceClassif=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count=0
while True:

	ret, frame = cap.read()
	if ret == False: break
	frame =  imutils.resize(frame, width=640)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	auxFrame = frame.copy()

	faces = faceClassif.detectMultiScale(gray,1.3,5)

	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
		rostro = auxFrame[y:y+h,x:x+w]
		rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
		cv2.imwrite(personPath + '/rotro_{}.jpg'.format(count),rostro)
		count = count + 1
	cv2.imshow('frame',frame)

	k =  cv2.waitKey(1)
	if k == 27 or count >= 400: #Numero de Rostros capturaados
		break

cap.release()
cv2.destroyAllWindows()


