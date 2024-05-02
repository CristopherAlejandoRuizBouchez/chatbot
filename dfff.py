
import pandas as pd
import datetime

def df_nuevo(numero_dato):
    df = pd.read_csv('SESVER1.csv', encoding='latin-1')
    df_nuevo = df[df["No. DE EQUIPO"] == numero_dato]

    with open('df_nuevo1.csv', 'a') as f:
        df_nuevo.to_csv(f, header=f.tell()==0, index=False)

    

print("Hola, te estás comunicando con el asistente virtual de Soprorim. ¿Cómo puedo ayudarte el día de hoy?\n")
print("Por favor, selecciona una de las siguientes opciones:")
print("1. Solicitud de Toner")
print("2. Servicio de Mantenimiento")
print("3. Servicio Técnico")
print("4. Hablar con un Colaborador\n")



while True:
    opcion = input("Ingrese el número correspondiente a su elección: ")
    # Procesar la selección del usuario
    if opcion == "1":
        numero_dato = int(input("Podria proporcionarme el numero de control de su equipo\n"))
        df_nuevo(numero_dato)
        fecha = datetime.now() # guardar fecha 
        break

    elif opcion == "2":
        numero_dato = int(input("Podria proporcionarme el numero de control de su equipo\n"))
        df_nuevo(numero_dato)
        fecha = datetime.now() # guardar fecha 
        #descripcion = str(input("Podria descrivir el problema:\n"))
        break

    elif opcion == "3":
        numero_dato = int(input("Podria proporcionarme el numero de control de su equipo\n"))
        df_nuevo(numero_dato)
        fecha = datetime.now() # guardar fecha 
        descripcion = str(input("Podria descrivir el problema:\n"))
        break

    elif opcion == "4":
        # Alerta  
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.\n")


# Se debe modificar la funcion para que agregue 4 columnas extras , reporte , hora , fecha , descripcion 