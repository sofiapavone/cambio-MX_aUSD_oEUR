"""
Problema: Empresa Mexicana pierde dinero porque las transacciones desde moneda internacional les resultan
complejas para realizar calculos a mano para pasar de Euro a Mex y de Dolar a Mex

Algoritmo: 
0) Definir el valor del euro y dolar en relación al peso mexicano
1) Preguntar al usuario el tipo de conversion (Eur - Mex) o (USD - Mex)
2) Solicitar el monto a convertir
3) Realizar la conversión utilizando el tipo de cambio correspondiente
4) Mostrar el resultado de la conversión al usuario

Pseudocodigo: 
Inicio 
    Definir tipo_cambio_eur_a_mxn = 23.70 
    Definir tipo_cambio_eur_a_usd = 20.75

Mostrar mensaje: "Ingrese la moneda origen para la conversión" 

Mostrar mensaje: "Ingrese el monto a convertir"

Realizar la conversion correspondiente, 
Si tipo de conversion == EUR
    Calcular el resultado = monto_a_convertir * tipo_cambio_eur_a_mxn
    Mostrar el resultado de  Resultado

    Si no si tipo de conversion es == USD
    Calcular el resultado = monto_a_convertir * tipo_cambio_usd_a_mxn
    Mostrar el resultado de usd a mx

    Si no No esta disponible el tipo de conversión actualmente.
"""

tipo_cambio_eur_a_mxn = 23.70
tipo_cambio_usd_a_mxn = 20.75

tipo_conversion = input("¿El monto a convertir es EUR o USD?")
monto_a_convertir = float(input("Ingrese el monto a convertir: "))

if tipo_conversion.upper() == "EUR":
    resultado = tipo_cambio_eur_a_mxn * monto_a_convertir
    print (resultado)
elif tipo_conversion.upper() == "USD":
        resultado = tipo_cambio_usd_a_mxn * monto_a_convertir
        print (resultado)     
else: 
      print("No esta disponible el tipo de conversión")