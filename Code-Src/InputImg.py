#Importamos la libreria de OpenCV
from pathlib import Path
import cv2


#**********Funciones*****************
#Funcion para visualizar imagen con OpenCV
def VisulizarImagen(Path_Input):
    #Leer imagen (PNG,JPG,...)
    imagen=cv2.imread(Path_Input)
    #Mostrar imagen
    cv2.imshow("ventana",imagen)
    #Mostrar infinitamente la imagen hasta presionar cualquier tecla
    cv2.waitKey(0)
    #Destrui la ventana
    cv2.destroyAllWindows()
#**********************************************


def main():
    #ngresa la ruta donde se almacena tu imagen
    Path="/home/jetson/Open-CV-Servicio/Img-Src/Cirulo-Color.png"   
    VisulizarImagen(Path)


if __name__ == "__main__":
    main()

