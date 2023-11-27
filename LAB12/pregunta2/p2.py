from PIL import Image
import matplotlib.pyplot as plt

def calcular_histograma_imagen(nombre_imagen, imagen):
    # Convertir la imagen a escala de grises si es a color
    imagen_gris = imagen.convert('L')

    # Calcular el histograma
    histograma = imagen_gris.histogram()

    # Graficar el histograma
    plt.figure()
    plt.title(f'Histograma de {nombre_imagen}')
    plt.hist(histograma, bins=256, range=(0, 256), color='gray', alpha=0.7)
    plt.xlabel('Intensidad de píxeles')
    plt.ylabel('Frecuencia')
    plt.savefig(f'{nombre_imagen}_histograma.png')  # Guardar el histograma como imagen .png
    plt.close()

def calcular_histogramas():
    # Rutas de las 4 imágenes
    rutas_imagenes = ['imagen1.jpg', 'imagen2.jpg', 'imagen3.jpg', 'imagen4.jpg']

    # Calcular histograma para cada imagen
    for ruta_imagen in rutas_imagenes:
        nombre_imagen = ruta_imagen.split('.')[0]  # Obtener el nombre de la imagen sin extensión

        # Abrir y procesar la imagen usando PIL dentro de un bloque with open()
        with open(ruta_imagen, 'rb') as archivo_imagen:
            imagen = Image.open(archivo_imagen)
            calcular_histograma_imagen(nombre_imagen, imagen)

# Llamada a la función para calcular los histogramas de las 4 imágenes
calcular_histogramas()
