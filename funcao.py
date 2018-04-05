import cv2
import glob

def analiza_varias(imagens):
    classificador = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
    imagem = cv2.imread(imagens)
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    facesDetectadas = classificador.detectMultiScale(imagemCinza)

    print(len(facesDetectadas))

    print(facesDetectadas)

    for (x, y, l, a) in facesDetectadas:
        print(x, y, l, a)
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
        # cv2.rectangle(imagem, x, y, (0, 0, 255), thickness=1, lineType=8, shift=0)

    cv2.imshow("Faces encontradas", imagem)
    cv2.waitKey()

todosarquivos = glob.glob('pessoas/*.jpg')

#print(todosarquivos)

for l in todosarquivos:
    analiza_varias(l)

#analiza_varias('pessoas/beatles.jpg')






