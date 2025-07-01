def primos_return(lista):
    primos=[]
    
    for i in lista:
        if not isinstance(i,int):
            continue
        resultados=[]
        for c in range(i+1):
            if c!=0:
                if i%c==0:
                    resultados.append(c)
        if len(resultados)==2:
            primos.append(i)

    print(primos)
lista=list(map(int,input("Ingresa una lista de numeros seprada por comas ").split(",")))
primos_return(lista)

