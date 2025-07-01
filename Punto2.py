def palindromos(palabra):
    palindromo=bool
    if not palabra:
        print("Vacio")
        return
    magnitud1=palabra[len(palabra)-1]
    magnitud2=palabra[0]
    contador1=(len(palabra)-1)
    contador=0
    while contador!=(len(palabra)-1):
        if magnitud1==magnitud2:
            palindromo=True
        else:
            palindromo=False
            print("No es palindroma")
            break
        contador=contador+1
        contador1=contador1-1
        magnitud2=palabra[contador]
        magnitud1=palabra[contador1]
    if palindromo==True:
        print("La palabra es palindroma")
if __name__ == "__main__":
    while True:
        try:
            entrada_str = input("Ingresa una palabra: ")
            entrada = list(entrada_str) 
            palindromos(entrada)
            break

        except Exception as e:
            print(f"Ocurrió un error: {e}. Por favor, inténtalo de nuevo.")
        finally:
            print("Fin")
