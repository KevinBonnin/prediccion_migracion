import pandas as pd
from fastapi import FastAPI
import uvicorn
import joblib
from enum import Enum

indicadores = pd.read_csv('indicadores.csv')

modelo = joblib.load('modelo_migracion.pkl')

app = FastAPI()

class Pais(str, Enum):
    Argentina = 'Argentina'
    Brasil = 'Brasil'
    Chile = 'Chile'

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