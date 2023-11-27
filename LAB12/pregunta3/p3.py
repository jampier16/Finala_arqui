import random

def calcular_pi(num_muestras):
    muestras_dentro_circulo = 0

    for _ in range(num_muestras):
        # Generar coordenadas aleatorias en el rango [-1, 1]
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Verificar si la muestra está dentro del círculo
        distancia_al_centro = x ** 2 + y ** 2
        if distancia_al_centro <= 1:
            muestras_dentro_circulo += 1

    # Calcular Pi usando la fórmula de Monte Carlo
    pi_aproximado = (4 * muestras_dentro_circulo) / num_muestras
    return pi_aproximado

def main():
    num_muestras = 10000000  # Número de muestras
    pi_calculado = calcular_pi(num_muestras)
    print(f'El valor aproximado de Pi con {num_muestras} muestras es: {pi_calculado}')

if __name__ == "__main__":
    main()