"""para importar una libreria que se llama tkinter para 
trabajar python de forma grafica"""

import tkinter as tk
from tkinter import ttk


#Crear la ventana de la aplicación
ventana = tk.Tk()
ventana.title('Conversor de monedas')
ventana.geometry('600x400')
ventana.configure(background='#ececec') # Fondo gris claro
ventana.resizable(False, False) # Es para evitar redimensionar la ventana.


    # Crear etiqueta para la entrar la cantidad
etiqueta_cantidad = tk.Label(ventana, text= 'Cantidad: ', font= ('Arial', 14))
etiqueta_cantidad.grid (column= 0, row = 0, padx= 10, pady= 10)

entrada_cantidad = tk.Entry(ventana, width= 10, font= ('Arial', 14))
entrada_cantidad.grid(column= 1, row= 0, padx= 10, pady= 10)

    # Crear etiqueta para el resultado
etiqueta_resultado = tk.Label(ventana, text= 'Resultado: ', font= ('Arial', 14))
etiqueta_resultado.grid (column= 0, row= 2, padx= 10, pady= 10)

resultado = tk.Entry(ventana, width= 10, font= ('Arial', 14))
resultado.grid(column= 1, row= 2, padx= 10, pady= 10)

opcion_origen = tk.StringVar()
opcion_origen.set ("COP")

opcion_destino = tk.StringVar()
opcion_destino.set ("USD")

    #RadioButtons para las opciones de origen
radio_cop = tk.Radiobutton(ventana, text= 'COP', variable= opcion_origen, value= "COP", font= ('Arial', 12))
radio_cop.grid(column= 0, row= 1, padx= 10, pady= 10)

radio_usd = tk.Radiobutton(ventana, text= 'USD', variable= opcion_origen, value= "USD", font= ('Arial', 12))
radio_usd.grid(column= 1, row= 1, padx= 10, pady= 10)

radio_eur = tk.Radiobutton(ventana, text= 'EUR', variable= opcion_origen, value= "EUR", font= ('Arial', 12))
radio_eur.grid(column= 2, row= 1, padx= 10, pady= 10)

radio_jpy = tk.Radiobutton(ventana, text= 'JPY', variable= opcion_origen, value= "JPY", font= ('Arial', 12))
radio_jpy.grid(column= 3, row= 1, padx= 10, pady= 10)

    #RadioButtons para las opciones de destino
radio_cop_dest = tk.Radiobutton(ventana, text= 'COP', variable= opcion_destino, value= "COP", font= ('Arial', 12))
radio_cop_dest.grid(column= 0, row= 3, padx= 10, pady= 10)

radio_usd_dest = tk.Radiobutton(ventana, text= 'USD', variable= opcion_destino, value= "USD", font= ('Arial', 12))
radio_usd_dest.grid(column= 1, row= 3, padx= 10, pady= 10)

radio_eur_dest = tk.Radiobutton(ventana, text= 'EUR', variable= opcion_destino, value= "EUR", font= ('Arial', 12))
radio_eur_dest.grid(column= 2, row= 3, padx= 10, pady= 10)

radio_jpy_dest = tk.Radiobutton(ventana, text= 'JPY', variable= opcion_destino, value= "JPY", font= ('Arial', 12))
radio_jpy_dest.grid(column= 3, row= 3, padx= 10, pady= 10)

    #Tasas de cambio
COP_to_USD = 0.00027
COP_to_JPY = 0.037
COP_to_EUR = 0.00023

USD_to_COP = 3700
USD_to_JPY = 136
USD_to_EUR = 0.85

JPY_to_COP = 27
JPY_to_USD = 0.0074
JPY_to_EUR = 0.0062

EUR_to_COP = 4350
EUR_to_USD = 1.18
EUR_to_JPY = 162

    #Funsion del boton convertir
def convertir():
    cantidad = entrada_cantidad.get()
    if cantidad:
        cantidad = float(cantidad)
        origen = opcion_origen.get()
        destino = opcion_destino.get()
        
        if origen == "COP":
            if destino == "COP":
                resultado_monto = cantidad
            elif destino == "USD":
                resultado_monto = cantidad * COP_to_USD
            elif destino == "EUR":
                resultado_monto = cantidad * COP_to_EUR
            elif destino == "JPY":
                resultado_monto = cantidad * COP_to_JPY
        
        elif origen == "USD":
            if destino == "COP":
                resultado_monto = cantidad * USD_to_COP
            elif destino == "USD":
                resultado_monto = cantidad
            elif destino == "EUR":
                resultado_monto = cantidad * USD_to_EUR
            elif destino == "JPY":
                resultado_monto = cantidad * USD_to_JPY
        
        elif origen == "EUR":
            if destino == "COP":
                resultado_monto = cantidad * EUR_to_COP
            elif destino == "USD":
                resultado_monto = cantidad * EUR_to_USD
            elif destino == "EUR":
                resultado_monto = cantidad
            elif destino == "JPY":
                resultado_monto = cantidad * EUR_to_JPY
        
        elif origen == "JPY":
            if destino == "COP":
                resultado_monto = cantidad * JPY_to_COP
            elif destino == "USD":
                resultado_monto = cantidad * JPY_to_USD
            elif destino == "EUR":
                resultado_monto = cantidad * JPY_to_EUR
            elif destino == "JPY":
                resultado_monto = cantidad
        
        resultado.delete(0, tk.END)
        resultado.insert(0, str(resultado_monto))
        
    #Crear boton para crear la conversión
botton_convertir = ttk.Button(ventana, text= "convertir", command= convertir)
botton_convertir.grid (column= 1, row= 6, sticky= 'nsew')
    

ventana.mainloop()

