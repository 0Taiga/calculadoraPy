primeiro_numero = int(input())
operador = input()
segundo_numero = int(input())
resultado = 0

if operador == "+":
    resultado = primeiro_numero + segundo_numero
    elif operador == "-":
        resultado = primeiro_numero - segundo_numero
        elif operador == "*":
           resultado = primeiro_numero * segundo_numero
            elif operador== "/":
               resultado = primeiro_numero / segundo_numero
    print(resultado)
