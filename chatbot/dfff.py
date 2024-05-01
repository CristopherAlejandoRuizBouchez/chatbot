
import pandas as pd

def df_nuevo(numero_dato):

    df = pd.read_csv('SESVER1.csv', encoding='latin-1')

    df_nuevo = df[df["No. DE EQUIPO"] == numero_dato]

    with open('df_nuevo.csv', 'a') as f:
        df_nuevo.to_csv(f, header=f.tell()==0, index=False)


numero_dato = 7
df_nuevo(numero_dato)

