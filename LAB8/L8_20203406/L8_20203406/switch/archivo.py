
SOCK_BUFFER = 128
def RetornaGruposSock(Ubicaciontxt):
    global SOCK_BUFFER
    with open(Ubicaciontxt,'r') as archivo_leido:
        lineas = archivo_leido.readlines()
        archivo_leido.close()
    lineas_separadas = []
    for linea in lineas:
        linea_arreglada = (linea.replace('[',' ').replace(']',' ')).split(' ')
        if linea == '*****\n':
            lineas_separadas.append(linea)
        else:
            if (linea_arreglada[6] == 'B040') or  (linea_arreglada[6] == 'B020') or  (linea_arreglada[6] == 'B013') or  (linea_arreglada[6] == 'B012') or  (linea_arreglada[6] == 'B010'):
                lineas_separadas.append(linea)

    grupos_sock_buffer = []
    grupo_individual = ''
    for linea in lineas_separadas:
        if len(linea) + len(grupo_individual) < SOCK_BUFFER:
            grupo_individual = grupo_individual + linea
        else:
            bits_necesarios = SOCK_BUFFER - (len(grupo_individual) - 1)
            grupo_individual = grupo_individual + linea[0:bits_necesarios-1]
            grupos_sock_buffer.append(grupo_individual)
            grupo_individual = linea[bits_necesarios-1: len(linea)]
    grupos_sock_buffer.append(grupo_individual)
    return grupos_sock_buffer

print(RetornaGruposSock('./transacciones-2023_autA.txt'))