def operaciones (num1,num2,operacion):
    match operacion:
        case"+":
            Resultado=num1+num2
        case"-":
            Resultado=num1-num2
        case"*":
            Resultado=num1*num2
        case"/":
            if num2 == 0:
                raise ZeroDivisionError("No se puede dividir por cero.")
            else:
                Resultado = num1 / num2
        case _: 
            raise ValueError(f"Operación no válida: '{operacion}'. Use '+', '-', '*' o '/'.")
    return Resultado 


while True: 
        try:
            entrada = input("Ingresa los números y la operación separados por una coma, ej: 1,2,+ ").split(",")

            if len(entrada) != 3:
                raise ValueError("Formato de entrada incorrecto. Por favor, usa 'numero 1, numero 2, operacion'.")
            else:
                x = float(entrada[0].strip())
                y=  float(entrada[1].strip())# .strip() para eliminar espacios que siento no amerita un error propio
                z = entrada[2].strip()
                resultado_operacion = operaciones(x, y, z)
                break 

        except ValueError as e:
            print(f"Error de entrada: {e}. Intente de nuevo.")
        except ZeroDivisionError as e:
            print(f"Error de cálculo: {e}. Intente de nuevo.")
        finally:
            print("Fin") 
           
