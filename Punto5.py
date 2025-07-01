def encontrar_caracteres(lista_Palabras):
    resultados = []
    n = len(lista_Palabras)

    for i in range(n):
        palabra1 = lista_Palabras[i]
        letras_ordenadas1 = sorted(palabra1)

        for j in range(i + 1, n):
            palabra2 = lista_Palabras[j]
            letras_ordenadas2 = sorted(palabra2)

            if letras_ordenadas1 == letras_ordenadas2:
                if palabra1 not in resultados:
                    resultados.append(palabra1)
                if palabra2 not in resultados:
                    resultados.append(palabra2)

    if resultados:
        print("Palabras con los mismos caracteres:", resultados)
    else:
        print("No hay palabras con los mismos caracteres")

entrada_usuario = input("Ingresa una lista de palabras separadas por comas")
lista_de_palabras = [palabra.strip() for palabra in entrada_usuario.split(',')]
encontrar_caracteres(lista_de_palabras)