import pandas as pd
from fastapi import FastAPI
import uvicorn
import joblib

indicadores = pd.read_csv('indicadores.csv')

modelo = joblib.load('modelo_migracion.pkl')

app = FastAPI()

@app.get("/Modelo de prediccion")
def prediccion_flujo(crecimiento_pib,tasa_desempleo,inflacion_pib,muertes_conflicto,control_corrupcion,esperanza_vida):
    datos_prediccion = {}
    datos_prediccion = [[crecimiento_pib, tasa_desempleo, inflacion_pib, muertes_conflicto, control_corrupcion, esperanza_vida]]
    df = pd.DataFrame(datos_prediccion)
    prediccion = modelo.predict(df)
    return prediccion[0]