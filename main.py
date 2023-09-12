import pandas as pd
from fastapi import FastAPI
import uvicorn
import joblib
from enum import Enum

indicadores = pd.read_csv('indicadores.csv')

modelo = joblib.load('modelo_migracion.pkl')

app = FastAPI()

#class Pais(Enum):
 #   Argentina = [5, 6, 8, 5, 7, 4]
  #  Brasil = [7, 8, 6, 2, 1, 5]
   # Chile = [5.2, 8.3, 2.1, 100, 75, 78.5]

#@app.get("/Modelo de prediccion")
#def prediccion_flujo(crecimiento_pib,tasa_desempleo,inflacion_pib,muertes_conflicto,control_corrupcion,esperanza_vida):
 #   datos_prediccion = {}
  #  datos_prediccion = [[crecimiento_pib, tasa_desempleo, inflacion_pib, muertes_conflicto, control_corrupcion, esperanza_vida]]
   # df = pd.DataFrame(datos_prediccion)
   # prediccion = modelo.predict(df)
   # return prediccion[0]

#@app.get("/modelo2")
#def prediccion_flujo1(pais: Pais):
 #   datos_prediccion = {}
  #  datos_prediccion = [[pais[0], pais[1], pais[2], pais[3], pais[4], pais[5]]]
   # df = pd.DataFrame(datos_prediccion)
   # prediccion = modelo.predict(df)
    #return prediccion[0]

#@app.get("/modelo3")
#def prediccion_flujo1(pais: Pais):
 #   datos_prediccion = [[*pais.value]]  # Convierte los valores del Enum en una lista
  #  df = pd.DataFrame(datos_prediccion)
   # prediccion = modelo.predict(df)
    #return prediccion[0]

class Pais(str, Enum):
    Argentina = 'Argentina'
    Brasil = 'Brasil'
    Chile = 'Chile'

# Esta función te permitirá obtener los datos asociados a un país
def obtener_datos_por_pais(pais):
    if pais == Pais.Argentina:
        return (5, 6, 8, 5, 7, 4)
    elif pais == Pais.Brasil:
        return (7, 8, 6, 2, 1, 5)
    elif pais == Pais.Chile:
        return (5.2, 8.3, 2.1, 100, 75, 78.5)
    else:
        raise ValueError("País no válido")

@app.get("/modelo2")
def prediccion_flujo1(pais: Pais):
    datos_prediccion = obtener_datos_por_pais(pais)
    df = pd.DataFrame([datos_prediccion])
    prediccion = modelo.predict(df)
    return prediccion[0]