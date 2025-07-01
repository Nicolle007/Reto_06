
def sumatotal (lista):
    magnitud1=lista[0]
    magnitud2=lista[1]
    contador1=0
    contador=1
    suma=0
    while contador!=len(lista):
        suma2=magnitud1+magnitud2
        if suma2>=suma:
            suma=suma2
        contador=contador+1
        contador1=contador1+1
        if contador==len(lista):
            break
        magnitud1=lista[contador1]
        magnitud2=lista[contador]
    print(suma)



if __name__ == "__main__":
    while True: 
        try:
            entrada_usuario = input("Ingresa una lista de números separada por comas: ")
            if not entrada_usuario.strip():
                print("Error: No se ingresó ningún número. Por favor, inténtalo de nuevo.")
            else:
                continue
            lista_str = entrada_usuario.split(",")
            lista_numeros = []
            for item in lista_str:
                
                lista_numeros.append(int(item.strip())) 
            sumatotal(lista_numeros) 
            break

        except ValueError as e:
            print(f"Error en la entrada: '{e}'. Asegúrate de ingresar solo números separados por comas. Inténtalo de nuevo.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}. Por favor, inténtalo de nuevo.")
        finally:
            print("Fin")
