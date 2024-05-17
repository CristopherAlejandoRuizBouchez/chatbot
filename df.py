import pandas as pd
from datetime import datetime

def df_nuevo(numero_dato, tipo_reporte):
    try:
        df = pd.read_csv('Sesver.csv', encoding='latin-1')
        print("Datos leídos correctamente del archivo 'Sesver.csv'")
    except FileNotFoundError:
        print("ERROR: No se pudo encontrar el archivo 'Sesver.csv'")
        return

    df_nuevo = df[df["No. DE EQUIPO"] == numero_dato]
    df_nuevo["Tipo de Reporte"] = tipo_reporte

    # Guardar en el mismo archivo CSV
    with open('df_nuevo1.csv', 'a') as f:
        df_nuevo.to_csv(f, header=f.tell()==0, index=False)

def mostrar_menu():
    print("Hola, te estás comunicando con el asistente virtual de Soprorim. ¿Cómo puedo ayudarte el día de hoy?\n")
    print("Por favor, selecciona una de las siguientes opciones:")
    print("1. Solicitud de Toner")
    print("2. Reportar una Falla")
    print("3. Hablar con un Colaborador")
    print("4. Salir\n")

def obtener_opcion():
    while True:
        opcion = input("Ingrese el número correspondiente a su elección: ")
        if opcion in ("1", "2", "3", "4"):
            return opcion
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.\n")

# Mostrar el menú inicial
mostrar_menu()

# Obtener la opción del usuario
opcion_elegida = obtener_opcion()

# Procesar la opción elegida por el usuario
if opcion_elegida in ("1", "2"):
    numero_dato = input("Por favor, proporcione el número de control de su equipo: ")
    if opcion_elegida == "1":
        tipo_reporte = "Solicitud de Toner"
    else:
        tipo_reporte = "Reporte de Falla"
    df_nuevo(numero_dato, tipo_reporte)
    fecha = datetime.now() # guardar fecha 
    if opcion_elegida == "1":
        print("¡La solicitud de tóner ha sido registrada exitosamente!")
    else:
        print("¡La falla ha sido registrada exitosamente!")

elif opcion_elegida == "3":
    print("Conectando con un colaborador humano...")

elif opcion_elegida == "4":
    print("Gracias por usar el asistente virtual de Soprorim. ¡Hasta luego!")
