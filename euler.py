def e_cuadratica(n):
    ''' Funcion que calcula una aproximacion al valor de euler de forma cuadratica
		E: un numero entero positivo
		S: el valor de euler
		R: debe ser positivo
	'''
    if (n<0):
        return "Error: valor no valido"
    elif (n==0):
        return 1
    else:
        result = 1
        while n>0:
            result = result + (1/factorial(n))
            n = n-1
        return result


def e_lineal(n):
    ''' Funcion que calcula una aproximacion al valor de euler de forma cuadratica
        E: un numero entero positivo
		S: el valor de euler
		R: debe ser positivo
    '''
    result = 1
    if (n<0):
        return "Error: valor no valido"
    else:
        while n>0:
            i = n
            fact = 1
            while i>0:
                fact = fact*i        
                i = i-1
            n = n-1
            result = result + (1/fact)
        return result
    
def factorial(n):
	''' Funcion que calcula el factorial de un numero
		E: un numero entero positivo
		S: el factorial de ese numero (numero entero)
		R: debe ser positivo
	'''
	if (n<0):
		print ("Error: valor ingresado no valido")
	elif (n==0):
		return 1
	else:
		result=1
		while n>0:
			result = result * n
			n = n-1
		return result
		
	
